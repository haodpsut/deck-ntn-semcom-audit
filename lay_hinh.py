#!/usr/bin/env python3
"""Lấy hình của bài về deck dưới dạng SVG GIỮ CHỮ THẬT, không sửa tệp của bài.

    python3 lay_hinh.py

Cách làm: nạp `figures/make_figures.py` của bài rồi **bọc `Figure.savefig`** lại, để mỗi
lần bài lưu PDF thì đồng thời lưu thêm một SVG vào `hinh/` của deck. Đặt
`svg.fonttype = "none"` nên matplotlib ghi chữ ra thẻ `<text>` thật thay vì đường vẽ;
sau đó gỡ khai báo font để chữ THỪA KẾ chữ của deck.

⚠ Không chạm vào tệp của bài. Bài vẫn là một chỗ ở duy nhất của hình và số.
Hình TikZ thì đi đường khác: `kit/tu_tikz.py`.
"""
from __future__ import annotations

import re
import runpy
import sys
from pathlib import Path

D = Path(__file__).resolve().parent
BAI = (D.parents[1] / "paper-lab" / "hao-paper-2026" / "ntn-semcom-realism-audit")
KIT = D.parents[1] / "_templates" / "deck-web" / "kit"
HE_SO_CHU = float(__import__("os").environ.get("HE_SO_CHU", "2.2"))
MAU_BAI = "#d55e00"   # màu nhấn của BÀI, vermillion Okabe-Ito
LAY = {"fig2-orbital", "fig3-pass", "fig4-elevation", "fig5-census",
       "fig6-matrix", "fig7-mismatch", "fig8-blocklen"}


def mau_deck() -> str:
    """Màu nhấn của deck, đọc từ front matter. Hình phải nhuộm theo deck, không
    phải ngược lại. Xem kit/mau.json."""
    import re as _re
    m = _re.search(r'^accent:\s*"?(#[0-9A-Fa-f]{6})', (D / "noi-dung.md").read_text(encoding="utf-8"), _re.M)
    return m.group(1) if m else "#2C6E9B"


def don(svg: str, ten: str) -> str:
    """Gỡ font và đặt tiền tố id, để hình thừa kế deck và không đụng id với hình khác."""
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>", "", svg)
    # ⚠ matplotlib ghi dạng VIẾT TẮT `font: 8px 'DejaVu Serif', serif`, không phải
    # `font-family:`. Phải đổi thành font-size để giữ cỡ mà bỏ họ chữ, nếu không
    # hình vẫn mang chữ có chân của matplotlib và cổng G22 bắt.
    # ⚠ dừng ở dấu chấm phẩy hoặc dấu nháy kép, KHÔNG dừng ở nháy đơn:
    # tên họ chữ nằm trong nháy đơn ('DejaVu Serif') nên dừng ở đó là chừa nó lại.
    svg = re.sub(r'font\s*:\s*([\d.]+)px[^;"]*', r"font-size:\1px", svg)
    svg = re.sub(r"font-family\s*:\s*[^;\"']+;?", "", svg)
    svg = re.sub(r'\sfont-family="[^"]*"', "", svg)
    svg = re.sub(r'\s(width|height)="[\d.]+pt"', "", svg, count=2)
    tien = "m%s-" % re.sub(r"[^a-z0-9]", "", ten.lower())[:10]
    for i in sorted(set(re.findall(r'\sid="([^"]+)"', svg)), key=len, reverse=True):
        svg = svg.replace('id="%s"' % i, 'id="%s%s"' % (tien, i))
        svg = svg.replace('href="#%s"' % i, 'href="#%s%s"' % (tien, i))
        svg = svg.replace("url(#%s)" % i, "url(#%s%s)" % (tien, i))
    sys.path.insert(0, str(KIT))
    import hinhkit as hk
    return hk.doi_mau_nhan(svg.strip(), MAU_BAI, mau_deck())


def ve_giao_thuc():
    """Vẽ LẠI hình giao thức ở đúng khổ slide.

    ⚠ Vì sao không dùng hình TikZ của bài: nó vẽ cho khổ một cột, chữ 7pt, chiếu lên
    chỉ ra 12px. Nâng cỡ chữ bằng tu_tikz --slide thì khối to ra, TikZ tính lại toạ
    độ, và ĐƯỜNG NỐI CẮT QUA KHỐI. Đo được: tỉ lệ hình đổi 3,1%. Nên vẽ lại.
    Số trong khối vẫn lấy từ so-lieu.json nên không lệch với bài.
    """
    import json
    sys.path.insert(0, str(KIT))
    import hinhkit as hk
    so = json.loads((D / "so-lieu.json").read_text(encoding="utf-8"))

    W, H = 1100, 486
    bw, bh, gap = 390, 58, 16
    xa, xb = 70, 640
    y0 = 56
    r = hk.mo(W, H)
    r.append(hk.vung(xa - 22, y0 - 16, bw + 44, 4 * bh + 3 * gap + 32, "đo quỹ đạo"))
    r.append(hk.vung(xb - 22, y0 - 16, bw + 44, 4 * bh + 3 * gap + 32, "đo văn liệu"))

    a = [("TLE Starlink công khai", "dữ liệu mở, không mô phỏng"),
         ("Lan truyền SGP4", "%s lượt bay" % so["so_luot"]),
         ("Hình học từng lượt", "cự ly nghiêng, góc ngẩng"),
         ("Doppler, trôi, quét ngân sách", "và cửa sổ nhìn thấy")]
    b = [("Bảng của chính khảo sát", "công trình đại diện"),
         ("Quần thể %s công trình" % so["quan_the"], "đọc được toàn văn %s" % so["doc_duoc"]),
         ("Tách từng bài", "phần NÊU RA với phần ĐÁNH GIÁ"),
         ("Đối chiếu danh mục kiểm", "neo vào %s" % so["chuan_neo"])]
    ha, ra_a, daya = hk.cot_khoi(a, xa, y0, bw, bh, gap, prop_cuoi=True)
    hb, ra_b, dayb = hk.cot_khoi(b, xb, y0, bw, bh, gap, prop_cuoi=True)
    r.append(ha); r.append(hb)

    yc = daya + 64
    cx = (xa + xb + bw) / 2
    bwc = 620
    r.append(hk.khoi(cx - bwc / 2, yc, bwc, bh, "Khoảng cách ấy trả giá bằng gì",
                     "huấn luyện theo giả định, đánh giá dưới điều kiện đo được"))
    hop = hk.khoi_moi()
    # ⚠ NỐI KHỐI VỚI KHỐI, không gõ toạ độ. Hai mũi tên lệch nhau để không chồng.
    r.append(hk.noi(ra_a[-1], hop, ne=-150))
    r.append(hk.noi(ra_b[-1], hop, ne=150))
    r.append('<text x="%d" y="%d" text-anchor="middle" class="hk-phu" font-size="%d">'
             "hai nhánh không dùng chung một dữ liệu vào</text>"
             % (cx, yc + bh + 28, hk.CO_NHAN))

    if hk.kiem():
        print("⛔ hình giao thức có lỗi hình học, xem phía trên")
    (D / "hinh" / "fig1-protocol.svg").write_text(hk.dong(r), encoding="utf-8")


def main() -> int:
    import matplotlib as mpl
    mpl.use("Agg")
    mpl.rcParams["svg.fonttype"] = "none"

    # ⚠ Nhuộm màu ở TẦNG MATPLOTLIB, không ở tầng SVG. Hình ma trận vẽ bằng ảnh
    # raster nhúng nên thay chuỗi trong SVG không tới được các ô, chỉ đổi được chú
    # giải: nhìn ra chú giải một màu mà ô một màu khác. Chặn ở to_rgba thì mọi chỗ
    # dùng màu ấy đều đổi, kể cả bảng màu dựng từ chuỗi hex.
    import matplotlib.colors as mcolors
    _to_rgba = mcolors.to_rgba
    _bai = _to_rgba(MAU_BAI)

    def _nhuom(c, alpha=None):
        r = _to_rgba(c, alpha)
        return _to_rgba(mau_deck(), alpha) if r[:3] == _bai[:3] else r

    mcolors.to_rgba = _nhuom
    from matplotlib.figure import Figure

    goc = Figure.savefig
    da = []

    import matplotlib.text as mtext

    def phong_chu(fig, he_so):
        """Phóng mọi đối tượng chữ trước khi lưu SVG, rồi trả lại như cũ.

        ⚠ Đây là cái lever mà hình TikZ KHÔNG có: cỡ chữ matplotlib nằm trên từng
        đối tượng Text nên sửa được sau khi hình đã dựng. Hình TikZ thì cỡ chữ
        nằm trong style của chính bài, `every node` thua nó, nên chỉ còn cách cho
        hình một slide trọn vẹn.
        """
        cu = []
        for t in fig.findobj(mtext.Text):
            c = t.get_fontsize()
            cu.append((t, c))
            t.set_fontsize(c * he_so)
        return cu

    def bao(self, fname, *a, **kw):
        kq = goc(self, fname, *a, **kw)
        ten = Path(str(fname)).stem
        if ten in LAY and str(fname).endswith(".pdf"):
            ra = D / "hinh" / (ten + ".svg")
            kw2 = dict(kw); kw2.pop("dpi", None)
            kw2["transparent"] = True   # để nền giấy của deck ăn qua, đừng thành thẻ trắng
            cu = phong_chu(self, HE_SO_CHU)
            goc(self, str(ra), format="svg", **kw2)
            for t, c in cu:
                t.set_fontsize(c)
            ra.write_text(don(ra.read_text(encoding="utf-8"), ten), encoding="utf-8")
            da.append(ten)
        return kq

    Figure.savefig = bao
    sys.argv = ["make_figures.py"]
    runpy.run_path(str(BAI / "figures" / "make_figures.py"), run_name="__main__")
    Figure.savefig = goc

    print("✅ lấy %d hình kết quả sang SVG: %s" % (len(da), " ".join(sorted(da))))

    # hình giao thức là TikZ, đi đường dvisvgm
    sys.path.insert(0, str(KIT))
    import tu_tikz
    ve_giao_thuc()
    return 0


if __name__ == "__main__":
    sys.exit(main())
