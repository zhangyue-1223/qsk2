# -*- coding: utf-8 -*-
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
USER = """        <div class="flex items-center gap-3 shrink-0">
          <button type="button" class="w-9 h-9 rounded-full bg-slate-100 text-slate-500 hover:bg-slate-200" aria-label="通知"><i class="fa-regular fa-bell"></i></button>
          <div class="flex items-center">
            <img class="w-9 h-9 rounded-full object-cover" src="https://images.unsplash.com/photo-1556157382-97eda2d62296?auto=format&fit=crop&w=80&q=80" alt="用户头像">
            <div class="ml-2 hidden sm:block">
              <p class="text-sm font-medium text-slate-700">朱总</p>
              <p class="text-xs text-slate-400">企业管理员</p>
            </div>
          </div>
        </div>"""

broken_pat = re.compile(
    r'(<header class="h-16[^"]*"[^>]*>\s*<div class="flex items-center gap-2 min-w-0 flex-1">\s*'
    r'<button type="button" id="btn-sidebar-toggle"[^>]*>.*?</button>\s*'
    r'(<motion class="text-sm text-slate-500 min-w-0 truncate">.*?</motion>)'
    r'\s*)</header>',
    re.DOTALL,
)
broken_pat2 = re.compile(
    r'(<header class="h-16[^"]*"[^>]*>\s*<div class="flex items-center gap-2 min-w-0 flex-1">\s*'
    r'<button type="button" id="btn-sidebar-toggle"[^>]*>.*?</button>\s*'
    r'(<div class="text-sm text-slate-500 min-w-0 truncate">.*?</motion>)'
    r'\s*)</header>',
    re.DOTALL,
)

for name in ["address-management.html", "knowledge-base.html"]:
    p = ROOT / name
    t = p.read_text(encoding="utf-8")
    m = broken_pat.search(t) or broken_pat2.search(t)
    if not m:
        # simpler: missing close div + user
        old = re.search(
            r'(<header class="h-16.*?</button>\s*<div class="text-sm text-slate-500 min-w-0 truncate">.*?</div>)\s*</header>',
            t,
            re.DOTALL,
        )
        if old:
            block = old.group(1)
            block = re.sub(
                r"(<div class=\"flex items-center gap-2 min-w-0 flex-1\">)\s*<button",
                r"\1\n          <button",
                block,
                count=1,
            )
            block = re.sub(
                r"</button>\s*<div class=\"text-sm",
                "</button>\n          <div class=\"text-sm",
                block,
                count=1,
            )
            new = block + "\n        </div>\n" + USER + "\n      </header>"
            t = t[: old.start()] + new + t[old.end() :]
            p.write_text(t, encoding="utf-8", newline="\n")
            print("fixed", name)
        else:
            print("no match", name)
        continue
    inner = m.group(1)
    inner = re.sub(r"\n        <button", "\n          <button", inner, count=1)
    inner = re.sub(r"\n        <div class=\"text-sm", "\n          <motion class=\"text-sm", inner, count=1)
    inner = inner.replace('<motion class="text-sm', '<div class="text-sm')
    new = inner.rstrip() + "\n        </motion>\n" + USER + "\n      </header>"
    new = new.replace("</motion>", "</div>")
    t2 = t[: m.start()] + new + t[m.end() :]
    p.write_text(t2, encoding="utf-8", newline="\n")
    print("fixed", name)

p = ROOT / "customer-items.html"
t = p.read_text(encoding="utf-8")
if "rounded-full bg-slate-100 text-slate-500 hover:bg-slate-200" not in t.split("</header>")[0]:
    t = t.replace(
        '<header class="h-16 bg-white border-b border-slate-200 px-4 sm:px-6 gap-2 flex items-center">',
        '<header class="h-16 bg-white border-b border-slate-200 px-4 sm:px-6 gap-2 flex items-center justify-between shrink-0">',
    )
    t = t.replace(
        '        <button type="button" id="btn-sidebar-toggle"',
        '          <button type="button" id="btn-sidebar-toggle"',
        1,
    )
    t = t.replace(
        '        <div class="text-sm text-slate-500 min-w-0 truncate">客户中心 / <span class="text-slate-700 font-medium">客户物品</span></div>\n        </div>\n      </header>',
        '          <div class="text-sm text-slate-500 min-w-0 truncate">客户中心 / <span class="text-slate-700 font-medium">客户物品</span></div>\n        </div>\n'
        + USER
        + "\n      </header>",
    )
    p.write_text(t, encoding="utf-8", newline="\n")
    print("fixed customer-items")

for html in ROOT.glob("*.html"):
    if html.name in ("login.html", "index.html"):
        continue
    t = html.read_text(encoding="utf-8")
    t2 = re.sub(
        r"\bh-9 px-4 rounded bg-blue-600\b",
        "h-9 px-4 rounded-md bg-blue-600 hover:bg-blue-700 cursor-pointer",
        t,
    )
    if t2 != t:
        html.write_text(t2, encoding="utf-8", newline="\n")
        print("buttons", html.name)
