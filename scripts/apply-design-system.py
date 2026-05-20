# -*- coding: utf-8 -*-
"""Apply unified design system to all HTML pages except login and index."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {"login.html", "index.html"}

HEADER_USER_BLOCK = """        <div class="flex items-center gap-3 shrink-0">
          <button type="button" class="w-9 h-9 rounded-full bg-slate-100 text-slate-500 hover:bg-slate-200" aria-label="通知"><i class="fa-regular fa-bell"></i></button>
          <div class="flex items-center">
            <img class="w-9 h-9 rounded-full object-cover" src="https://images.unsplash.com/photo-1556157382-97eda2d62296?auto=format&fit=crop&w=80&q=80" alt="用户头像">
            <div class="ml-2 hidden sm:block">
              <p class="text-sm font-medium text-slate-700">朱总</p>
              <p class="text-xs text-slate-400">企业管理员</p>
            </div>
          </div>
        </div>"""


def process(path: Path) -> list[str]:
    changes = []
    text = path.read_text(encoding="utf-8")
    orig = text

    if 'class="bg-slate-100 text-slate-700"' in text:
        text = text.replace('class="bg-slate-100 text-slate-700"', 'class="bg-[#f5f7fa] text-slate-700"', 1)
        changes.append("body-bg")

    if "design-system.css" not in text:
        if 'href="./assets/responsive.css"' in text:
            text = text.replace(
                '<link rel="stylesheet" href="./assets/responsive.css">',
                '<link rel="stylesheet" href="./assets/responsive.css">\n  <link rel="stylesheet" href="./assets/design-system.css">',
                1,
            )
            changes.append("css-link")
        elif "font-awesome" in text:
            text = re.sub(
                r'(<link rel="stylesheet" href="https://cdnjs\.cloudflare\.com/ajax/libs/font-awesome/[^"]+">)',
                r'\1\n  <link rel="stylesheet" href="./assets/design-system.css">',
                text,
                count=1,
            )
            if "design-system.css" in text:
                changes.append("css-link")

    text = re.sub(
        r"\bh-9\s+rounded\s+bg-blue-600\b",
        "h-9 rounded-md bg-blue-600 hover:bg-blue-700 cursor-pointer",
        text,
    )
    text = re.sub(
        r"\bh-8\s+px-4\s+rounded\s+bg-blue-600\b",
        "h-9 px-4 rounded-md bg-blue-600 hover:bg-blue-700 cursor-pointer",
        text,
    )
    text = re.sub(
        r"\brounded\s+bg-blue-600\s+px-4\b",
        "rounded-md bg-blue-600 hover:bg-blue-700 cursor-pointer px-4",
        text,
    )
    text = re.sub(
        r"\bh-9\s+rounded\s+border\s+border-slate-200\s+bg-white\b",
        "h-9 rounded-md border border-slate-200 bg-white hover:bg-slate-50 cursor-pointer",
        text,
    )
    text = re.sub(
        r"\bh-9\s+px-4\s+rounded\s+border\s+border-slate-200\b",
        "h-9 px-4 rounded-md border border-slate-200 hover:bg-slate-50 cursor-pointer",
        text,
    )
    text = re.sub(
        r"\bh-9\s+px-5\s+rounded\s+border\s+border-slate-200\b",
        "h-9 px-5 rounded-md border border-slate-200 hover:bg-slate-50 cursor-pointer",
        text,
    )
    text = re.sub(
        r"\bh-9\s+w-full\s+rounded\s+border\s+border-slate-200\b",
        "h-9 w-full rounded-md border border-slate-200",
        text,
    )
    text = re.sub(
        r"\bh-9\s+px-3\s+rounded\s+border\s+border-slate-200\b",
        "h-9 px-3 rounded-md border border-slate-200",
        text,
    )
    text = text.replace(
        "overflow-x-auto rounded border border-slate-200",
        "overflow-x-auto rounded-lg border border-slate-200",
    )
    text = text.replace(
        '<motion class="mt-4 rounded border border-slate-200 overflow-hidden">',
        '<div class="mt-4 rounded-lg border border-slate-200 overflow-hidden shadow-sm">',
    )
    text = text.replace(
        '<div class="mt-4 rounded border border-slate-200 overflow-hidden">',
        '<div class="mt-4 rounded-lg border border-slate-200 overflow-hidden shadow-sm">',
    )
    text = re.sub(
        r"bg-white rounded-xl border border-slate-200 p-5(?!\s+shadow)",
        "bg-white rounded-xl border border-slate-200 p-5 shadow-sm",
        text,
    )

    if path.name == "customer-management.html" and "h-14 bg-white" in text:
        m = re.search(
            r'<header class="h-14[^"]*"[^>]*>.*?<motion class="text-sm text-slate-500">(.*?)</div>',
            text,
            re.DOTALL,
        )
        if not m:
            m = re.search(
                r'<header class="h-14[^"]*"[^>]*>\s*<div class="text-sm text-slate-500">(.*?)</div>',
                text,
                re.DOTALL,
            )
        breadcrumb = m.group(1).strip() if m else '客户中心 / <span class="text-slate-700 font-medium">客户管理</span>'
        new_header = (
            '<header class="h-16 bg-white border-b border-slate-200 px-4 sm:px-6 gap-2 flex items-center justify-between shrink-0">\n'
            '        <div class="flex items-center gap-2 min-w-0 flex-1">\n'
            '          <button type="button" id="btn-sidebar-toggle" class="lg:hidden shrink-0 w-10 h-10 rounded-lg border border-slate-200 bg-white text-slate-600 hover:bg-slate-50 flex items-center justify-center" aria-expanded="false" aria-controls="app-sidebar" aria-label="打开导航菜单"><i class="fa-solid fa-bars text-lg"></i></button>\n'
            f'          <div class="text-sm text-slate-500 min-w-0 truncate">{breadcrumb}</div>\n'
            "        </div>\n"
            + HEADER_USER_BLOCK.replace("<motion class=", "<motion class=").replace("<motion class=", "<div class=").replace("</motion>", "</div>")
            + "\n      </header>"
        )
        text = re.sub(r"<header class=\"h-14.*?</header>", new_header, text, count=1, flags=re.DOTALL)
        changes.append("header-cm")

    if 'id="app-sidebar"' in text and "app-shell.js" not in text and "btn-sidebar-toggle" in text:
        if "function setOpen" not in text and "setOpen(sidebar" not in text:
            text = text.replace("</body>", '  <script src="./assets/app-shell.js"></script>\n</body>', 1)
            changes.append("app-shell")

    text = text.replace("<motion ", "<div ")
    text = text.replace("</motion>", "</div>")

    text = re.sub(r"(cursor-pointer\s+){2,}", "cursor-pointer ", text)
    text = re.sub(r"(hover:bg-blue-700\s+){2,}", "hover:bg-blue-700 ", text)
    text = re.sub(r"(hover:bg-slate-50\s+){2,}", "hover:bg-slate-50 ", text)

    if text != orig:
        path.write_text(text, encoding="utf-8", newline="\n")
    return changes


def main():
    updated = []
    for html in sorted(ROOT.glob("*.html")):
        if html.name in SKIP:
            continue
        ch = process(html)
        if ch:
            updated.append((html.name, ch))
    print(f"Updated {len(updated)} files:")
    for name, ch in updated:
        print(f"  {name}: {', '.join(ch)}")


if __name__ == "__main__":
    main()
