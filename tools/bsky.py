#!/usr/bin/env python3
"""Bluesky research helper (public AppView API, no auth).

  bsky.py search "<query>" [--limit 50] [--sort top|latest] [--pages 1]
  bsky.py thread <https://bsky.app/profile/<handle>/post/<rkey>> [--depth 6]
  bsky.py author <handle> [--limit 50]      # recent posts by one account
  bsky.py profile <handle>                  # bio / description

Output lines: date | @handle | ♥likes ↻reposts | text | url
"""
import json, sys, urllib.parse, urllib.request, argparse

API = "https://api.bsky.app/xrpc/"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0 Safari/537.36"

def get(method, **params):
    url = API + method + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def fmt(p):
    a = p["author"]["handle"]; r = p["record"]; rk = p["uri"].split("/")[-1]
    txt = r.get("text", "").replace("\n", " / ")
    return f'{r.get("createdAt","")[:10]} | @{a} | ♥{p.get("likeCount",0)} ↻{p.get("repostCount",0)} | {txt} | https://bsky.app/profile/{a}/post/{rk}'

def search(q, limit, sort, pages):
    cursor = None
    for _ in range(pages):
        params = dict(q=q, limit=limit, sort=sort)
        if cursor: params["cursor"] = cursor
        d = get("app.bsky.feed.searchPosts", **params)
        for p in d.get("posts", []): print(fmt(p))
        cursor = d.get("cursor")
        if not cursor: break

def resolve(handle):
    return get("com.atproto.identity.resolveHandle", handle=handle)["did"]

def thread(url, depth):
    parts = url.rstrip("/").split("/")
    handle, rk = parts[-3], parts[-1]
    did = handle if handle.startswith("did:") else resolve(handle)
    d = get("app.bsky.feed.getPostThread", uri=f"at://{did}/app.bsky.feed.post/{rk}", depth=depth, parentHeight=30)
    def show(n, ind=0):
        if "post" not in n: return
        print("  " * ind + fmt(n["post"]))
        for c in n.get("replies", []): show(c, ind + 1)
    t = d["thread"]; chain = []; par = t.get("parent")
    while par and "post" in par: chain.append(par); par = par.get("parent")
    for n in reversed(chain): print(fmt(n["post"]))
    print("--- focus post + replies ---"); show(t)

def author(handle, limit):
    d = get("app.bsky.feed.getAuthorFeed", actor=handle, limit=limit, filter="posts_no_replies")
    for it in d.get("feed", []): print(fmt(it["post"]))

def profile(handle):
    d = get("app.bsky.actor.getProfile", actor=handle)
    print(json.dumps({k: d.get(k) for k in ("handle", "displayName", "description", "followersCount", "postsCount")}, indent=1, ensure_ascii=False))

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("search"); s.add_argument("q"); s.add_argument("--limit", type=int, default=50); s.add_argument("--sort", default="top"); s.add_argument("--pages", type=int, default=1)
    t = sub.add_parser("thread"); t.add_argument("url"); t.add_argument("--depth", type=int, default=6)
    a = sub.add_parser("author"); a.add_argument("handle"); a.add_argument("--limit", type=int, default=50)
    pr = sub.add_parser("profile"); pr.add_argument("handle")
    ns = ap.parse_args()
    if ns.cmd == "search": search(ns.q, ns.limit, ns.sort, ns.pages)
    elif ns.cmd == "thread": thread(ns.url, ns.depth)
    elif ns.cmd == "author": author(ns.handle, ns.limit)
    else: profile(ns.handle)
