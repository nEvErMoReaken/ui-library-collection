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
    "Shadcn 核心生态",
    "Shadcn 兼容扩展",
    "独立非 Shadcn 库",
    "纯 CSS / 其他",
]

CATEGORY_DESC = {
    "Shadcn 核心生态": "深度绑定 shadcn/ui：必须先用 `shadcn` CLI 初始化项目，组件通过 `npx shadcn add` 安装，代码风格/约定与 shadcn 一致。",
    "Shadcn 兼容扩展": "独立组件库，但额外提供 shadcn CLI 作为可选安装通道；不依赖 shadcn 项目也能用（可直接 copy-paste）。",
    "独立非 Shadcn 库": "完全自成体系，与 shadcn 无关，有自己的安装方式和设计语言。",
    "纯 CSS / 其他": "不依赖特定框架的样式方案，或不属于以上三类的其他库。",
}



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
        if cat in CATEGORY_DESC:
            lines.append(f"> {CATEGORY_DESC[cat]}")
            lines.append("")
        lines.append("| 名称 | 框架 | 链接 | 说明 | 收费 | 标签 | 来源 | 添加日期 |")
        lines.append("|---|---|---|---|---|---|---|---|")
        for lib in sorted(groups[cat], key=lambda x: x.get("name", "").lower()):
            name = lib.get("name", "")
            framework = lib.get("framework", "-")
            url = lib.get("url", "")
            desc = lib.get("description", "")
            pricing = lib.get("pricing", "Unknown")
            tags = ", ".join(lib.get("tags", []))
            source = lib.get("source", "")
            source_md = f"[link]({source})" if source else ""
            added = lib.get("added_date", "")
            lines.append(f"| {name} | {framework} | [{url}]({url}) | {desc} | {pricing} | {tags} | {source_md} | {added} |")
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
