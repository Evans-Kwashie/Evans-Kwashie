#!/usr/bin/env python3
"""Refresh the live block in README.md with the latest commit of each recently pushed public repo."""
import datetime as dt
import json
import os
import re
import sys
import urllib.request

USER = os.environ.get("GH_USER", "Evans-Kwashie")
TOKEN = os.environ.get("GH_TOKEN", "")


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-updater"}
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def ago(ts):
    then = dt.datetime.strptime(ts, "%Y-%m-%dT%H:%M:%SZ")
    secs = max(0, int((dt.datetime.utcnow() - then).total_seconds()))
    for size, unit in ((86400 * 30, "mo"), (86400, "d"), (3600, "h"), (60, "m")):
        if secs >= size:
            return f"{secs // size}{unit} ago"
    return "just now"


repos = [
    r for r in api(f"/users/{USER}/repos?sort=pushed&per_page=30&type=owner")
    if not r["fork"] and r["name"].lower() != USER.lower()
]

rows = []
for repo in repos[:6]:
    try:
        commit = api(f"/repos/{USER}/{repo['name']}/commits?per_page=1")[0]
    except Exception:
        continue
    msg = commit["commit"]["message"].splitlines()[0][:44]
    rows.append((commit["sha"][:7], repo["name"][:26], ago(commit["commit"]["author"]["date"]), msg))

if not rows:
    sys.exit("no commits found, leaving README untouched")

body = "\n".join(f"{sha}  {name:<26} {when:>8}  {msg}" for sha, name, when, msg in rows)
stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
block = (
    "<!-- LIVE:START -->\n```text\n"
    "$ git log --oneline   # latest commit per repo\n"
    f"{body}\n```\n<sub>refreshed {stamp} UTC by a scheduled workflow</sub>\n"
    "<!-- LIVE:END -->"
)

with open("README.md", encoding="utf-8") as fh:
    text = fh.read()
updated, n = re.subn(r"<!-- LIVE:START -->.*?<!-- LIVE:END -->", lambda _: block, text, flags=re.S)
if n != 1:
    sys.exit("live markers not found")
with open("README.md", "w", encoding="utf-8") as fh:
    fh.write(updated)
print(block)
