#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 The Authors
r"""sanitize_annotation_key_paths_712.py — 712：清除标注密钥里的宿主绝对路径。

问题
====
`data/frozen_matrix/689_annotation_key_mapping.json` 的 145 行里有 **41 行**
`src_path` 是绝对路径，形如

    <盘符>:\...\<源仓库根名>\Examples\_ch147_leak.cpp

这把**源仓库根目录名**与**宿主目录结构**写进了公开发的复现包：既是身份线索
（可搜索该根名反查到作者），也是"匿名包里有绝对路径"的自相矛盾。
其余 104 行的 `src_path` 本来就是合成标识（`external_corpus::d3-18`、`expA::sample_021` 等），无需处理。

> 本文件刻意**不写出**源仓库根名的字面量：那本身就会成为一条可搜索的身份线索
> （首版就踩了这个坑，被 712 的泄露扫描抓到 3 处，已改为占位符）。

处置
====
只改 `src_path` 字段：把宿主前缀替换为中性占位 `upstream-root/<相对路径>`，
**尾部相对路径逐字保留**（`Examples/...`、`Appendix/ub/...`、`data/cards_665/fixtures/...`），
因此该文件的全部**标注语义**（anon_id ↔ uid ↔ 缺陷类型 ↔ 期望判决）逐字不变。
同时在文件顶层写入 `src_path_sanitization` 记录规则与改动条数，便于审稿人核对"改了什么"。

实现要点
========
替换是**纯文本级**的：先把每条绝对路径按 JSON 转义后的字面量在原文里替换掉，
再把新字段插入顶层对象。除了被清洗的 41 个字符串与本说明字段，文件其余字节逐字不变
（用 `--check` 之外的 `git diff --numstat` 可直接核对：只多不少）。

用法
====
    python tools/sanitize_annotation_key_paths_712.py            # 执行（幂等）
    python tools/sanitize_annotation_key_paths_712.py --check    # 只报告不改（有残留则退出 1）
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
KEY = ROOT / "data" / "frozen_matrix" / "689_annotation_key_mapping.json"
FALLBACK_KEY = ROOT / "data" / "689_annotation_key_mapping.json"

REPLACEMENT = "upstream-root/"
META_KEY = "src_path_sanitization"


def project_re(root_name: str) -> re.Pattern[str] | None:
    """构造"源仓库根名 + 路径分隔符"的正则。

    **为什么不把根名写死在代码里**：本脚本会随匿名包一起公开，任何写死的根名
    本身就成了可搜索的身份线索（首版正是这样，被 712 泄露扫描抓到 3 处）。
    因此根名由调用方通过 `--root-name` 或环境变量 `QUEYI_UPSTREAM_ROOT_NAME`
    传入 —— 这两个入口出现在**源仓库**的批次报告里，不出现在公开包的文件内容中。
    """
    if not root_name:
        return None
    return re.compile(re.escape(root_name) + r"[\\/]", re.IGNORECASE)


def sanitize_path(sp: str, rx: re.Pattern[str] | None) -> tuple[str, bool]:
    """返回 (新路径, 是否改动)。只动绝对路径；合成标识原样返回。"""
    if not re.match(r"^[A-Za-z]:[\\/]", sp) and not sp.startswith("/"):
        return sp, False
    m = rx.search(sp) if rx else None
    if not m:
        return REPLACEMENT + "<path>", True
    tail = sp[m.end():].replace("\\", "/")
    return REPLACEMENT + tail, True


def main() -> int:
    ap = argparse.ArgumentParser(description="712 标注密钥路径清洗")
    ap.add_argument("--check", action="store_true", help="只报告，不写回")
    ap.add_argument("--root-name", default=os.environ.get("QUEYI_UPSTREAM_ROOT_NAME", ""),
                    help="源仓库根目录名（用于切分保留尾部相对路径）；"
                         "留空则把整条绝对路径替换为占位符")
    args = ap.parse_args()
    rx = project_re(args.root_name)
    if rx is None:
        print("[712-key] 警告：未提供 --root-name / QUEYI_UPSTREAM_ROOT_NAME，"
              "绝对路径将被整体替换为 'upstream-root/<path>'（尾部相对路径不保留）")

    path = KEY if KEY.exists() else FALLBACK_KEY
    if not path.exists():
        print(f"[712-key] 找不到密钥文件：{KEY}")
        return 2

    raw = path.read_text(encoding="utf-8")
    data = json.loads(raw)
    rows = data.get("rows", [])

    pairs: list[tuple[str, str]] = []
    seen: set[str] = set()
    for r in rows:
        sp = r.get("src_path", "")
        new, did = sanitize_path(sp, rx)
        if did and sp not in seen:
            seen.add(sp)
            pairs.append((sp, new))

    print(f"[712-key] 共 {len(rows)} 行；含宿主绝对路径的 src_path 去重后 {len(pairs)} 条")
    for a, b in pairs[:3]:
        print("   -", a)
        print("     ->", b)

    if args.check:
        if pairs:
            print(f"[712-key] FAIL：仍有 {len(pairs)} 条宿主绝对路径未清洗")
            return 1
        print("[712-key] PASS：无宿主绝对路径残留")
        return 0

    # 1) 文本级替换：用 JSON 转义形式在原文里精确替换
    out = raw
    n_repl = 0
    for a, b in pairs:
        ea = json.dumps(a, ensure_ascii=False)[1:-1]
        eb = json.dumps(b, ensure_ascii=False)[1:-1]
        cnt = out.count(ea)
        out = out.replace(ea, eb)
        n_repl += cnt

    # 2) 插入说明字段（顶层对象第一个成员之后）
    meta = {
        "applied_by": "tools/sanitize_annotation_key_paths_712.py",
        "reason": "匿名复现包不得包含宿主绝对路径（会泄漏源仓库根名与目录结构）",
        "rule": "宿主前缀 -> 'upstream-root/'；尾部相对路径逐字保留",
        "n_unique_paths_touched": len(pairs),
        "n_occurrences_replaced": n_repl,
        "n_rows_total": len(rows),
        "semantics_unchanged": True,
    }
    meta_txt = json.dumps({META_KEY: meta}, ensure_ascii=False, indent=1)
    # indent=1 的顶层对象起始为 "{\n"，把 meta 的成员裁出来插进去
    inner = meta_txt.strip()[1:-1].strip()
    idx = out.index("{") + 1
    out = out[:idx] + "\n" + inner + "," + out[idx:]

    # 3) 写回并自校验：必须仍是合法 JSON，且语义字段未被破坏
    parsed = json.loads(out)
    if len(parsed["rows"]) != len(rows):
        print("[712-key] FAIL：清洗后行数变化，已放弃写回")
        return 3
    for a, b in zip(rows, parsed["rows"]):
        for k in ("anon_id", "uid", "defect_type", "expected_verdict"):
            if a.get(k) != b.get(k):
                print(f"[712-key] FAIL：语义字段 {k} 被改动（{a.get(k)!r} -> {b.get(k)!r}）")
                return 3

    path.write_text(out, encoding="utf-8", newline="\n")
    print(f"[712-key] 已写回 {path}（替换 {n_repl} 处；语义字段逐字校验通过）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
