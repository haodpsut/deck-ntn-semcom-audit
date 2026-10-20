#!/usr/bin/env python3
"""Cây cầu duy nhất từ BÀI sang DECK. Chạy trước khi dựng.

    python3 lay_so.py

Đọc `figures/out/numbers.tex` và các bảng `tab*.tex` của bài `ntn-semcom-realism-audit`,
ghi `so-lieu.json`. Không gõ tay con số nào vào deck.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
BAI = D.parents[1] / "paper-lab" / "hao-paper-2026" / "ntn-semcom-realism-audit"
OUT = BAI / "figures" / "out"


def macro() -> dict:
    ra = {}
    for m in re.finditer(r"\\newcommand\{\\([A-Za-z]+)\}\{(.*?)\}\s*$",
                         (OUT / "numbers.tex").read_text(encoding="utf-8"), re.M):
        ra[m.group(1)] = m.group(2).replace("\\,", "\u202f").strip()
    return ra


def bang(ten, cot_moi=None, giu=None, giu_hang=None, nhan_hang=None, chu_thich=""):
    txt = (OUT / (ten + ".tex")).read_text(encoding="utf-8")
    dong = []
    for l in txt.splitlines():
        l = l.strip()
        if "&" not in l or "cmidrule" in l or "multicolumn" in l:
            continue
        l = re.sub(r"\\\\\s*$", "", l).strip()
        o = []
        for c in l.split("&"):
            c = re.sub(r"\\texttt\{|\\textbf\{|\\emph\{", "", c)
            c = c.replace("\\_", "_").replace("$", "").replace("\\", "").replace("{", "").replace("}", "")
            c = (c.replace("varepsilon", "\u03b5").replace("^-", "^")
                  .replace("10^4", "10\u207b\u2074").replace("10^3", "10\u207b\u00b3")
                  .replace("10^2", "10\u207b\u00b2"))
            o.append(re.sub(r"\s+", " ", c).strip())
        dong.append(o)
    cot, hang = dong[0], dong[1:]
    if giu_hang:
        hang = [hang[i] for i in giu_hang if i < len(hang)]
    if giu:
        cot = [cot[i] for i in giu]
        hang = [[r[i] for i in giu if i < len(r)] for r in hang]
    if cot_moi:
        cot = cot_moi
    d = {"cot": cot, "hang": hang}
    if chu_thich:
        d["chu_thich"] = chu_thich
    if nhan_hang is not None:
        d["nhan_hang"] = nhan_hang
    return d


def main() -> int:
    m = macro()
    so = {
        "so_luot": m["numPasses"],
        "doppler_ka": m["numDopKaMed"] + " kHz",
        "doppler_troi": m["numDopRateMax"] + " kHz/s",
        "quan_the": m["numPop"],
        "doc_duoc": m["numCtrlDocs"],
        "ma_hoa": m["numCoded"],
        "vet_quy_dao": "%s/%s" % (m["numEvCHTRACE"], m["numCoded"]),
        "doppler_bien_thien": "%s/%s" % (m["numEvDOPPLERRATE"], m["numCoded"]),
        "awgn": "%s/%s" % (m["numEvCHAWGN"], m["numCoded"]),
        "chuan_3gpp": "%s/%s" % (m["numEvCHGPP"], m["numCoded"]),
        "sup_vong_ho": m["numDropCfoEb"] + " dB",
        "muc_kiem": m["numChecklist"],
        "chuan_neo": "3GPP TR 38.821",
        # giữ sáu dòng chịu lực, hai dòng cuối là hai con số không
        "bang_kiem_ke": bang("tab2-census", giu_hang=[0, 1, 7, 9, 10, 11],
                             cot_moi=["mã", "hiệu ứng NTN hoặc mô hình kênh",
                                      "nêu ra", "có trong đánh giá"],
                             nhan_hang=4,
                             chu_thich="Cột cuối là số công trình THỰC SỰ đo dưới hiệu ứng đó. "
                                       "Bảng đầy đủ mười hai dòng nằm trong bài."),
        "bang_lech": bang("tab6-mismatch", giu=[0, 1, 3], giu_hang=[0, 1, 2, 4],
                          cot_moi=["điều kiện đánh giá", "huấn luyện một điểm SNR",
                                   "huấn luyện ngẫu nhiên hoá"],
                          chu_thich="Trung vị qua các lần chạy. Đơn vị là chất lượng ảnh khôi phục."),
    }
    (D / "so-lieu.json").write_text(json.dumps(so, ensure_ascii=False, indent=2), encoding="utf-8")
    print("✅ so-lieu.json · %d khoá · nguồn %s" % (len(so), OUT))
    print("   chốt: vệt quỹ đạo %s · Doppler biến thiên %s · AWGN %s"
          % (so["vet_quy_dao"], so["doppler_bien_thien"], so["awgn"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
