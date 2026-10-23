"""Square PNG -> CK3 coat of arms (docs/heraldry.md): the corner colour as the field, an optional vanilla disc, and the
rest as rectangles of ce_block_02: runs of same-coloured pixels along each row, merged with identical runs in the rows
below. Each rectangle overlaps its neighbours slightly so no seams show.
usage: img2coa.py in.png key res out.txt [--disc]"""
import sys, collections
import numpy as np
from PIL import Image
src,key,res,out=sys.argv[1],sys.argv[2],int(sys.argv[3]),sys.argv[4]; disc='--disc' in sys.argv
im=Image.open(src).convert('RGBA'); W=im.size[0]; assert im.size[0]==im.size[1], 'image must be square'
# transparency (an export's border, say) is flattened onto the image's most common opaque colour
_op=[px[:3] for px in im.getdata() if px[3]==255]
_bg=collections.Counter(_op).most_common(1)[0][0] if _op else (255,255,255)
_flat=Image.new('RGBA',im.size,_bg+(255,)); _flat.alpha_composite(im); im=_flat.convert('RGB')
full=np.asarray(im).reshape(-1,3)
# palette: the dominant colours of the full-size image (anti-aliasing shades fall out)
cnt=collections.Counter(tuple(int(v) for v in px) for px in full[::7])
pal=[]
for c,n in cnt.most_common():
    if all(sum((a-b)**2 for a,b in zip(c,p))>40**2 for p in pal): pal.append(c)   # 40: keeps a dark shade of the field apart
    if len(pal)==6: break
pal=[p for p in pal if cnt[p]>len(full[::7])*0.01]
P=np.array(pal,float)
def snap(arr): return np.argmin(((arr[...,None,:].astype(float)-P)**2).sum(-1),-1)
# field = colour of the corners; disc colour = colour of the centre column's top part inside the disc
big=snap(np.asarray(im))
field=collections.Counter([big[0,0],big[0,-1],big[-1,0],big[-1,-1]]).most_common(1)[0][0]
small=snap(np.asarray(im.resize((res,res),Image.LANCZOS)))
lines=[f'{key} = {{','\tpattern = "pattern_solid.dds"',f'\tcolor1 = rgb {{ {" ".join(map(str,pal[field]))} }}']
under=np.full_like(small,field)
if disc:
    # the disc: the second most common colour, its extent along the middle row of the full image
    dcol=[i for i,_ in collections.Counter(big.ravel()).most_common() if i!=field][0]
    row=np.where(big[W//2]==dcol)[0]; col=np.where(big[:,W//2]==dcol)[0]
    x0,x1,y0,y1=row.min(),row.max()+1,col.min(),col.max()+1
    cx,cy,d=(x0+x1)/2/W,(y0+y1)/2/W,max(x1-x0,y1-y0)/W
    sc=d/(152/256)
    lines+=['\tcolored_emblem = {','\t\ttexture = "ce_circle.dds"',f'\t\tcolor1 = rgb {{ {" ".join(map(str,pal[dcol]))} }}',
            f'\t\tinstance = {{ position = {{ {cx:.4f} {cy:.4f} }} scale = {{ {sc:.4f} {sc:.4f} }} }}','\t}']
    yy,xx=np.mgrid[0:res,0:res]; inside=((xx+.5)/res-cx)**2+((yy+.5)/res-cy)**2<=(d/2)**2
    under=np.where(inside,dcol,field)
n_inst=0
for ci in range(len(pal)):
    if disc and ci==dcol: continue   # the disc is drawn underneath; its colour outside it is only edge noise
    runs=[]
    for y in range(res):
        x=0
        while x<res:
            if small[y,x]==ci and small[y,x]!=under[y,x]:
                x0=x
                while x<res and small[y,x]==ci and small[y,x]!=under[y,x]: x+=1
                runs.append((x0,x,y))
            else: x+=1
    if not runs: continue
    # merge a run with the identical run in the next row(s): (x0, x1, y0, y1)
    rects=[]; open_={}
    for x0,x1,y in runs:
        r=open_.pop((x0,x1,y-1),None)
        if r: r[3]=y+1
        else: r=[x0,x1,y,y+1]; rects.append(r)
        open_[(x0,x1,y)]=r
    OV=0.08   # overlap, in pixels, against seams
    lines+=['\tcolored_emblem = {','\t\ttexture = "ce_block_02.dds"',f'\t\tcolor1 = rgb {{ {" ".join(map(str,pal[ci]))} }}']
    for x0,x1,y0,y1 in rects:
        lines.append(f'\t\tinstance = {{ position = {{ {(x0+x1)/2/res:.4f} {(y0+y1)/2/res:.4f} }} scale = {{ {(x1-x0+OV)/res:.4f} {(y1-y0+OV)/res:.4f} }} }}')
    lines.append('\t}'); n_inst+=len(rects)
lines.append('}')
open(out,'w').write('\n'.join(lines)+'\n')
print('palette',pal,'field',pal[field],'instances',n_inst)
