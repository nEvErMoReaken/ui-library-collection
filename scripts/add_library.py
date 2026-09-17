#!/usr/bin/env python3
"""Add a UI library entry to data/libraries.json and regenerate README.

Usage:
    python3 scripts/add_library.py --url URL [--name NAME] [--category CAT]
        [--description DESC] [--tags a,b,c]

If --name/--category/--description are omitted, sensible defaults are used
so this can be scripted from an automated pipeline; refine manually in
data/libraries.json afterwards if needed.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import date
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, "data", "libraries.json")


def load():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save(libs):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(libs, f, ensure_ascii=False, indent=2)
        f.write("\n")


def guess_name(url):
    path = urlparse(url).path.strip("/")
    if path:
        return path.split("/")[-1]
    return urlparse(url).netloc


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", required=True)
    p.add_argument("--name", default=None)
    p.add_argument("--category", default="独立非 Shadcn 库",
                    choices=["Shadcn 核心生态", "Shadcn 兼容扩展", "独立非 Shadcn 库", "纯 CSS / 其他"])
    p.add_argument("--framework", default="React",
                    help="e.g. React / Vue / Svelte / Angular / Framework-agnostic")
    p.add_argument("--description", default="")
    p.add_argument("--pricing", default="Unknown",
                    help="e.g. Free / Freemium / Paid / Open Source")
    p.add_argument("--tags", default="")
    args = p.parse_args()

    libs = load()
    if any(l.get("url") == args.url for l in libs):
        print(f"已存在，跳过: {args.url}")
        return

    entry = {
        "name": args.name or guess_name(args.url),
        "url": args.url,
        "category": args.category,
        "framework": args.framework,
        "description": args.description,
        "pricing": args.pricing,
        "tags": [t.strip() for t in args.tags.split(",") if t.strip()],
        "added_date": date.today().isoformat(),
    }
    libs.append(entry)
    save(libs)
    print(f"已添加: {entry['name']} -> {args.category}")

    subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "generate_readme.py")],
        check=True,
    )


if __name__ == "__main__":
    main()
