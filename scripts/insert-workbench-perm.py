# -*- coding: utf-8 -*-
from pathlib import Path

path = Path(r"d:\Q2\role-permissions.html")
text = path.read_text(encoding="utf-8")

marker = '    <motion class="perm-root space-y-3">\n      <section class="perm-module border border-slate-200 rounded-lg overflow-hidden bg-white shadow-sm">\n        <div class="bg-slate-50 flex items-center justify-between px-3 py-2.5 border-b border-slate-200">\n          <span class="text-sm font-semibold text-slate-800">客户中心</span>'
marker = marker.replace("<motion ", "<div ")

workbench = r'''    <div class="perm-root space-y-3">
      <section class="perm-module border border-slate-200 rounded-lg overflow-hidden bg-white shadow-sm" data-module="workbench">
        <div class="bg-slate-50 flex items-center justify-between px-3 py-2.5 border-b border-slate-200">
          <span class="text-sm font-semibold text-slate-800">工作台</span>
          <label class="inline-flex items-center gap-2 text-xs text-slate-600 cursor-pointer select-none">
            <input type="checkbox" class="js-mod-select-all h-3.5 w-3.5 rounded border-slate-300 text-blue-600">
            全选
          </label>
        </div>
        <div class="divide-y divide-slate-100">
          <div class="flex flex-wrap items-center gap-y-2 py-2.5 text-sm px-2">
            <label class="flex w-36 shrink-0 items-center gap-2 px-2 cursor-pointer">
              <input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">
              <span class="text-slate-800">快捷入口</span>
            </label>
            <motion class="hidden sm:block w-px h-5 bg-slate-200 shrink-0 mx-1"></motion>
            <div class="flex flex-1 flex-wrap gap-x-4 gap-y-1 text-slate-600 pl-1 sm:pl-0">
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">快速录入线索</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">新增跟进说明</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">发起合同签署</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">添加客户维护</label>
            </div>
          </div>
          <div class="flex flex-wrap items-center gap-y-2 py-2.5 text-sm px-2">
            <label class="flex w-36 shrink-0 items-center gap-2 px-2 cursor-pointer">
              <input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600" checked>
              <span class="text-slate-800">数据概览</span>
            </label>
            <div class="hidden sm:block w-px h-5 bg-slate-200 shrink-0 mx-1"></div>
            <div class="flex flex-1 flex-wrap gap-x-4 gap-y-1 text-slate-600 pl-1 sm:pl-0">
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600" checked>业绩进度</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600" checked>户数进度</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600" checked>续费进度</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600" checked>线索转化</label>
            </div>
          </div>
          <div class="flex flex-wrap items-center gap-y-2 py-2.5 text-sm px-2">
            <label class="flex w-36 shrink-0 items-center gap-2 px-2 cursor-pointer">
              <input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">
              <span class="text-slate-800">工作简报</span>
            </label>
            <div class="hidden sm:block w-px h-5 bg-slate-200 shrink-0 mx-1"></div>
            <motion class="flex flex-1 flex-wrap gap-x-4 gap-y-1 text-slate-600 pl-1 sm:pl-0">
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">新增线索</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">有效线索</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">跟进中</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">合同审核</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">合同待签</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">订单未支付</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">工商未派单</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">代账未派单</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">代账到期</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">地址到期</label>
            </div>
          </div>
          <div class="flex flex-wrap items-center gap-y-2 py-2.5 text-sm px-2">
            <label class="flex w-36 shrink-0 items-center gap-2 px-2 cursor-pointer">
              <input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">
              <span class="text-slate-800">业务速览</span>
            </label>
            <div class="hidden sm:block w-px h-5 bg-slate-200 shrink-0 mx-1"></div>
            <div class="flex flex-1 flex-wrap gap-x-4 gap-y-1 text-slate-600 pl-1 sm:pl-0">
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">代账总户数</label>
              <label class="inline-flex items-center gap-1.5 cursor-pointer"><input type="checkbox" class="h-3.5 w-3.5 rounded border-slate-300 text-blue-600">政务服务（条）</label>
            </div>
          </div>
        </div>
      </section>

      <section class="perm-module border border-slate-200 rounded-lg overflow-hidden bg-white shadow-sm">
        <div class="bg-slate-50 flex items-center justify-between px-3 py-2.5 border-b border-slate-200">
          <span class="text-sm font-semibold text-slate-800">客户中心</span>'''

workbench = workbench.replace("<motion ", "<div ").replace("</motion>", "</motion>")

old = '    <div class="perm-root space-y-3">\n      <section class="perm-module border border-slate-200 rounded-lg overflow-hidden bg-white shadow-sm">\n        <div class="bg-slate-50 flex items-center justify-between px-3 py-2.5 border-b border-slate-200">\n          <span class="text-sm font-semibold text-slate-800">客户中心</span>'

if old not in text:
    print("marker not found")
else:
    text = text.replace(old, workbench, 1)
    text = text.replace("</motion>", "</div>")
    path.write_text(text, encoding="utf-8", newline="\n")
    print("done")
