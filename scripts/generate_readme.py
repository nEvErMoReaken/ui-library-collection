#!/usr/bin/env python3
"""Regenerate README.md from data/libraries.json, grouped by category."""
import json
import os
from collections import defaultdict
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = os.path.join(ROOT, "data", "libraries.json")
README_FILE = os.path.join(ROOT, "README.md")

# Preferred display order for categories; anything else is appended alphabetically after.
CATEGORY_ORDER = [
    "React",
    "Vue",
    "Svelte",
    "Angular",
    "Web Components",
    "CSS / Vanilla",
    "Design System",
    "Icon Library",
    "Animation",
    "Charts & Data Viz",
    "Admin Template",
    "Other",
]


def load_libraries():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def group_by_category(libs):
    groups = defaultdict(list)
    for lib in libs:
        groups[lib.get("category", "Other")].append(lib)
    return groups


def render(libs):
    groups = group_by_category(libs)
    ordered_cats = [c for c in CATEGORY_ORDER if c in groups]
    ordered_cats += sorted(c for c in groups if c not in CATEGORY_ORDER)

    lines = []
    lines.append("# UI Library Collection")
    lines.append("")
    lines.append("个人收集的 UI 库 / 组件库 / 设计系统链接，按分类整理。")
    lines.append("")
    lines.append(f"共收录 **{len(libs)}** 个库，最后更新于 {date.today().isoformat()}。")
    lines.append("")
    lines.append("## 目录")
    lines.append("")
    for cat in ordered_cats:
        anchor = cat.lower().replace(" ", "-").replace("/", "").replace("&", "").replace("--", "-")
        lines.append(f"- [{cat}](#{anchor}) ({len(groups[cat])})")
    lines.append("")

    for cat in ordered_cats:
        lines.append(f"## {cat}")
        lines.append("")
        lines.append("| 名称 | 链接 | 说明 | 收费 | 标签 | 添加日期 |")
        lines.append("|---|---|---|---|---|---|")
        for lib in sorted(groups[cat], key=lambda x: x.get("name", "").lower()):
            name = lib.get("name", "")
            url = lib.get("url", "")
            desc = lib.get("description", "")
            pricing = lib.get("pricing", "Unknown")
            tags = ", ".join(lib.get("tags", []))
            added = lib.get("added_date", "")
            lines.append(f"| {name} | [{url}]({url}) | {desc} | {pricing} | {tags} | {added} |")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("数据源见 [`data/libraries.json`](data/libraries.json)，由脚本 [`scripts/generate_readme.py`](scripts/generate_readme.py) 自动生成本文件，请勿手动编辑表格内容。")
    lines.append("")
    return "\n".join(lines)


def main():
    libs = load_libraries()
    content = render(libs)
    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"README.md regenerated with {len(libs)} libraries.")


if __name__ == "__main__":
    main()
