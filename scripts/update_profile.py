#!/usr/bin/env python3
"""Refresh the live block in README.md with the public projects, newest push first."""
import datetime as dt
import json
import os
import re
import sys
import urllib.request

USER = os.environ.get("GH_USER", "Evans-Kwashie")
TOKEN = os.environ.get("GH_TOKEN", "")

# Short blurbs shown in the profile. Falls back to the repo description on GitHub.
BLURBS = {
    "UAV-PHMC": "STM32G071 drone payload controller with a ROS 2 digital twin",
    "INA219-Voltage_Sensing_PCB": "4-layer current and power monitor, Kelvin-sense shunt",
    "CH340c-usb-uart-board": "USB to UART board, first fully self-designed PCB",
    "UART-2-RS-485-PCB": "RS-485 converter with differential pairs and TVS protection",
    "Gyroscope-Controlled-Car": "MPU6050 hand-gesture RC car over ESP-NOW",
    "Tiny-Tanks": "dual-board real-time firmware, 3D-printed snap-fit chassis",
    "Esp32-Air-Mouse": "wearable BLE air mouse with a Kalman-filtered IMU",
}


def api(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-updater"}
    if TOKEN:
        headers["Authorization"] = "Bearer " + TOKEN
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


repos = [
    r for r in api(f"/users/{USER}/repos?sort=pushed&per_page=50&type=owner")
    if not r["fork"] and r["name"].lower() != USER.lower()
]

rows = []
for repo in repos[:8]:
    blurb = BLURBS.get(repo["name"]) or (repo.get("description") or "").strip()
    if not blurb:
        blurb = repo.get("language") or "work in progress"
    rows.append((repo["name"][:28], blurb[:62]))

if not rows:
    sys.exit("no repositories found, leaving README untouched")

body = "\n".join(f"{name:<28} {blurb}" for name, blurb in rows)
stamp = dt.datetime.utcnow().strftime("%Y-%m-%d")
block = (
    "<!-- LIVE:START -->\n```text\n"
    "$ ls ~/bench   # public projects, newest push first\n"
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
