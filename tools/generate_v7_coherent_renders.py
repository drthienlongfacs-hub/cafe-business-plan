#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import math
import random
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "images"
W, H = 1600, 1000
AA = 2

FONT = "/System/Library/Fonts/Supplemental/Arial.ttf"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(BOLD if bold else FONT, size * AA)


def canvas(bg: str = "#f5f1e8") -> tuple[Image.Image, ImageDraw.ImageDraw]:
    img = Image.new("RGB", (W * AA, H * AA), bg)
    return img, ImageDraw.Draw(img, "RGBA")


def save(img: Image.Image, path: Path) -> None:
    img = img.resize((W, H), Image.Resampling.LANCZOS)
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path, optimize=True)


def pts(points: Iterable[tuple[float, float]]) -> list[tuple[int, int]]:
    return [(round(x * AA), round(y * AA)) for x, y in points]


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    text: str,
    size: int = 26,
    color: str = "#1f2937",
    bold: bool = False,
    anchor: str | None = None,
    align: str = "left",
) -> None:
    kwargs = {"font": font(size, bold), "fill": color, "align": align}
    if anchor:
        kwargs["anchor"] = anchor
    draw.text((xy[0] * AA, xy[1] * AA), text, **kwargs)


class Iso:
    def __init__(self, ox: float = 1000, oy: float = 145, scale: float = 30) -> None:
        self.ox = ox
        self.oy = oy
        self.scale = scale

    def p(self, x: float, y: float, z: float = 0) -> tuple[float, float]:
        s = self.scale
        return (
            self.ox + (x - y) * s * 0.78,
            self.oy + (x + y) * s * 0.42 - z * s * 0.95,
        )


COLORS = {
    "plot": "#dfead0",
    "lawn": "#7faa61",
    "path": "#cfc8bb",
    "wall": "#ede8dd",
    "wall_side": "#d6cec1",
    "glass": (108, 148, 162, 96),
    "glass_edge": "#334155",
    "roof": "#bd5b3e",
    "roof_dark": "#87402f",
    "roof_light": "#e69a69",
    "wood": "#b88755",
    "wood_dark": "#6f4e37",
    "floor_fb": "#d9d0c1",
    "floor_kids": "#e6d9bd",
    "kids": "#f2cf85",
    "fb": "#b9c7a5",
}


def poly(draw: ImageDraw.ImageDraw, points, fill, outline=None, width=1) -> None:
    draw.polygon(pts(points), fill=fill)
    if outline:
        draw.line(pts(list(points) + [points[0]]), fill=outline, width=width * AA, joint="curve")


def line(draw: ImageDraw.ImageDraw, points, fill="#334155", width=2) -> None:
    draw.line(pts(points), fill=fill, width=width * AA, joint="curve")


def soft_shadow(draw: ImageDraw.ImageDraw, iso: Iso, bx=2.5, by=6, bw=10, bl=20) -> None:
    corners = [iso.p(bx, by, 0), iso.p(bx + bw, by, 0), iso.p(bx + bw, by + bl, 0), iso.p(bx, by + bl, 0)]
    off = [(x + 28, y + 24) for x, y in corners]
    poly(draw, off, (0, 0, 0, 35))


def draw_plot(draw: ImageDraw.ImageDraw, iso: Iso, detailed=True) -> None:
    plot = [iso.p(0, 0), iso.p(15, 0), iso.p(15, 35), iso.p(0, 35)]
    poly(draw, plot, COLORS["plot"], "#9ca77c", 3)

    # Road and canal in front, locked to the same master plan.
    road = [iso.p(-2, -3), iso.p(17, -3), iso.p(17, 1.2), iso.p(-2, 1.2)]
    canal = [iso.p(-2, -7), iso.p(17, -7), iso.p(17, -3.5), iso.p(-2, -3.5)]
    poly(draw, road, "#b6b4ad", "#8b8d85", 2)
    poly(draw, canal, "#7aa5a8", "#4e767d", 2)
    for t in range(0, 18, 2):
        line(draw, [iso.p(t, 1.15), iso.p(t + 0.9, 0.2)], "#eee7dc", 2)

    # Loop paths around the 10x20m building.
    path_polys = [
        [iso.p(2.0, 4.8), iso.p(13.0, 4.8), iso.p(13.0, 6.0), iso.p(2.0, 6.0)],
        [iso.p(1.3, 6.0), iso.p(2.5, 6.0), iso.p(2.5, 27.0), iso.p(1.3, 27.0)],
        [iso.p(12.5, 6.0), iso.p(13.7, 6.0), iso.p(13.7, 27.0), iso.p(12.5, 27.0)],
        [iso.p(2.0, 26.0), iso.p(13.0, 26.0), iso.p(13.0, 27.3), iso.p(2.0, 27.3)],
    ]
    for p in path_polys:
        poly(draw, p, COLORS["path"], "#a7a095", 1)

    if not detailed:
        return

    random.seed(7)
    for _ in range(80):
        x = random.uniform(0.6, 14.4)
        y = random.uniform(2.0, 34.2)
        if 2.0 < x < 13.0 and 4.8 < y < 27.3:
            continue
        sx, sy = iso.p(x, y, 0.05)
        r = random.uniform(2.5, 6.5) * AA
        color = random.choice(["#497a3b", "#5f8d4f", "#315f38", "#9bbf74"])
        draw.ellipse((sx * AA - r, sy * AA - r, sx * AA + r, sy * AA + r), fill=color)

    for x, y in [(3, 2.8), (5.4, 2.8), (9.8, 2.7), (12.1, 2.8), (1.2, 12), (13.9, 13), (3.6, 31), (11.8, 31)]:
        draw_table(draw, iso, x, y, 0.0, s=0.65)

    # Outdoor sand/play patch always at the same front-right corner.
    sand = [iso.p(10.8, 2.2), iso.p(14.2, 2.2), iso.p(14.2, 4.6), iso.p(10.8, 4.6)]
    poly(draw, sand, "#ead7b6", "#b99b6b", 2)
    draw_slide(draw, iso, 12.1, 3.1, 0, s=0.55)


def draw_table(draw: ImageDraw.ImageDraw, iso: Iso, x: float, y: float, z: float = 0, s: float = 1) -> None:
    cx, cy = iso.p(x, y, z + 0.22 * s)
    r = 12 * s * AA
    draw.ellipse((cx * AA - r, cy * AA - r * 0.55, cx * AA + r, cy * AA + r * 0.55), fill="#c79a63", outline="#6f4e37", width=max(1, int(AA)))
    for dx, dy in [(-0.45, 0), (0.45, 0), (0, -0.45), (0, 0.45)]:
        px, py = iso.p(x + dx * s, y + dy * s, z + 0.08)
        rr = 5 * s * AA
        draw.ellipse((px * AA - rr, py * AA - rr, px * AA + rr, py * AA + rr), fill="#b88755")


def draw_slide(draw: ImageDraw.ImageDraw, iso: Iso, x: float, y: float, z: float, s: float = 1) -> None:
    base = [iso.p(x, y, z), iso.p(x + 1.0 * s, y, z), iso.p(x + 1.0 * s, y + 0.8 * s, z), iso.p(x, y + 0.8 * s, z)]
    poly(draw, base, "#deb777", "#7a5435", 1)
    roof = [iso.p(x - 0.1 * s, y - 0.1 * s, z + 1.0 * s), iso.p(x + 0.5 * s, y - 0.25 * s, z + 1.5 * s), iso.p(x + 1.1 * s, y - 0.1 * s, z + 1.0 * s)]
    poly(draw, roof, "#b87945", "#6f4e37", 1)
    ramp = [iso.p(x + 0.8 * s, y + 0.55 * s, z + 0.45 * s), iso.p(x + 1.8 * s, y + 1.2 * s, z + 0.05), iso.p(x + 1.55 * s, y + 1.45 * s, z + 0.05), iso.p(x + 0.55 * s, y + 0.8 * s, z + 0.45 * s)]
    poly(draw, ramp, "#d49a5a", "#7a5435", 1)


def wall(draw: ImageDraw.ImageDraw, iso: Iso, a, b, h=3.8, fill=None, outline="#6b7280", width=2) -> None:
    fill = fill or COLORS["wall"]
    p = [iso.p(a[0], a[1], 0), iso.p(b[0], b[1], 0), iso.p(b[0], b[1], h), iso.p(a[0], a[1], h)]
    poly(draw, p, fill, outline, width)


def draw_floor(draw: ImageDraw.ImageDraw, iso: Iso) -> None:
    fb = [iso.p(2.5, 6), iso.p(12.5, 6), iso.p(12.5, 19), iso.p(2.5, 19)]
    kids = [iso.p(2.5, 19), iso.p(12.5, 19), iso.p(12.5, 26), iso.p(2.5, 26)]
    poly(draw, fb, COLORS["floor_fb"], "#a69b8c", 2)
    poly(draw, kids, COLORS["floor_kids"], "#b89f6b", 2)
    for x in [4.5, 6.5, 8.5, 10.5]:
        line(draw, [iso.p(x, 6), iso.p(x, 26)], (255, 255, 255, 45), 1)
    for y in [8, 10, 12, 14, 16, 18, 20, 22, 24]:
        line(draw, [iso.p(2.5, y), iso.p(12.5, y)], (255, 255, 255, 45), 1)


def draw_walls(draw: ImageDraw.ImageDraw, iso: Iso, cut_front=True, glass=True) -> None:
    h = 3.8
    if cut_front:
        wall(draw, iso, (2.5, 26), (12.5, 26), h, COLORS["wall"])
        wall(draw, iso, (2.5, 6), (2.5, 26), h, COLORS["wall_side"])
        wall(draw, iso, (12.5, 6), (12.5, 26), h, "#dfd7cb")
    else:
        wall(draw, iso, (2.5, 6), (12.5, 6), h, COLORS["wall"])
        wall(draw, iso, (2.5, 6), (2.5, 26), h, COLORS["wall_side"])
        wall(draw, iso, (12.5, 6), (12.5, 26), h, "#dfd7cb")
        wall(draw, iso, (2.5, 26), (12.5, 26), h, COLORS["wall"])

    # Full-width acoustic glass partition at y=19, same in every render.
    p = [iso.p(2.5, 19, 0), iso.p(12.5, 19, 0), iso.p(12.5, 19, h), iso.p(2.5, 19, h)]
    poly(draw, p, COLORS["glass"], COLORS["glass_edge"], 2)
    for x in [4.5, 6.5, 8.5, 10.5]:
        line(draw, [iso.p(x, 19, 0.05), iso.p(x, 19, h)], COLORS["glass_edge"], 1)

    if glass:
        for y in [8, 11, 14, 22, 24.5]:
            line(draw, [iso.p(12.52, y, 0.2), iso.p(12.52, y, 3.4)], "#1f2937", 2)
        for x in [4.2, 6.4, 8.6, 10.8]:
            line(draw, [iso.p(x, 5.98, 0.2), iso.p(x, 5.98, 3.4)], "#1f2937", 2)


def draw_roof(draw: ImageDraw.ImageDraw, iso: Iso, full=True, alpha=245, lifted=False) -> None:
    h, ridge = 3.85, 5.65
    ox, oy = (-0.2, -0.55) if lifted else (0, 0)
    e1 = (2.0 + ox, 5.6 + oy)
    e2 = (13.0 + ox, 5.6 + oy)
    e3 = (13.0 + ox, 26.4 + oy)
    e4 = (2.0 + ox, 26.4 + oy)
    r1 = (7.5 + ox, 5.6 + oy)
    r2 = (7.5 + ox, 26.4 + oy)
    left_plane = [iso.p(*e1, h), iso.p(*r1, ridge), iso.p(*r2, ridge), iso.p(*e4, h)]
    right_plane = [iso.p(*r1, ridge), iso.p(*e2, h), iso.p(*e3, h), iso.p(*r2, ridge)]
    poly(draw, left_plane, (*hex_to_rgb(COLORS["roof_light"]), alpha), COLORS["roof_dark"], 2)
    if full:
        poly(draw, right_plane, (*hex_to_rgb(COLORS["roof"]), alpha), COLORS["roof_dark"], 2)
    else:
        poly(draw, right_plane, (*hex_to_rgb(COLORS["roof"]), 130), COLORS["roof_dark"], 2)

    # Curved clay tile rows and slightly upturned eaves.
    for y in [6.2, 7.4, 8.6, 9.8, 11.0, 12.2, 13.4, 14.6, 15.8, 17.0, 18.2, 19.4, 20.6, 21.8, 23.0, 24.2, 25.4]:
        line(draw, [iso.p(2.25 + ox, y + oy, h + 0.02), iso.p(7.5 + ox, y + oy, ridge + 0.02), iso.p(12.75 + ox, y + oy, h + 0.02)], (*hex_to_rgb("#7f3529"), 150), 1)
    for x in [3, 4, 5, 6, 8, 9, 10, 11, 12]:
        line(draw, [iso.p(x + ox, 5.7 + oy, h + 0.05), iso.p(7.5 + ox, 5.7 + oy, ridge + 0.05)], (*hex_to_rgb("#f1b17d"), 105), 1)

    # Triangular gable ends at both short sides.
    front = [iso.p(2.0 + ox, 5.6 + oy, h), iso.p(13.0 + ox, 5.6 + oy, h), iso.p(7.5 + ox, 5.6 + oy, ridge)]
    back = [iso.p(2.0 + ox, 26.4 + oy, h), iso.p(13.0 + ox, 26.4 + oy, h), iso.p(7.5 + ox, 26.4 + oy, ridge)]
    poly(draw, front, (239, 226, 205, 225), COLORS["wood_dark"], 2)
    poly(draw, back, (220, 205, 184, 165), COLORS["wood_dark"], 1)
    for a, b in [((2.4, 5.6, h + 0.05), (7.5, 5.6, ridge - 0.1)), ((12.6, 5.6, h + 0.05), (7.5, 5.6, ridge - 0.1)), ((7.5, 5.6, h + 0.05), (7.5, 5.6, ridge - 0.1))]:
        line(draw, [iso.p(*a), iso.p(*b)], COLORS["wood"], 3)


def hex_to_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def draw_interior(draw: ImageDraw.ImageDraw, iso: Iso) -> None:
    # Bar and cashier line in F&B zone.
    bar = [iso.p(3.1, 7.0, 0.15), iso.p(11.4, 7.0, 0.15), iso.p(11.4, 8.15, 0.15), iso.p(3.1, 8.15, 0.15)]
    poly(draw, bar, COLORS["wood"], COLORS["wood_dark"], 2)
    wall_shelf = [iso.p(3.3, 7.15, 1.45), iso.p(11.2, 7.15, 1.45), iso.p(11.2, 7.15, 2.15), iso.p(3.3, 7.15, 2.15)]
    poly(draw, wall_shelf, "#6f4e37", "#3f2a1c", 1)
    for x in [4, 5.4, 6.8, 8.2, 9.6, 10.8]:
        draw_table(draw, iso, x, 11.2, 0, 0.58)
        draw_table(draw, iso, x - 0.3, 15.1, 0, 0.55)

    # Kids area furniture locked to the same back zone.
    draw_slide(draw, iso, 8.2, 22.1, 0, 1.1)
    for x, y in [(4.0, 21.2), (5.2, 23.2), (4.4, 24.4)]:
        shelf = [iso.p(x, y, 0.1), iso.p(x + 1.4, y, 0.1), iso.p(x + 1.4, y + 0.45, 0.1), iso.p(x, y + 0.45, 0.1)]
        poly(draw, shelf, "#bf8f5e", COLORS["wood_dark"], 1)
    for x, y in [(5.3, 20.2), (6.9, 20.4), (5.9, 22.2), (7.2, 24.3)]:
        cx, cy = iso.p(x, y, 0.06)
        draw.ellipse((cx * AA - 8 * AA, cy * AA - 5 * AA, cx * AA + 8 * AA, cy * AA + 5 * AA), fill="#8fb9c2")


def title_block(draw: ImageDraw.ImageDraw, title: str, subtitle: str, badge: str) -> None:
    draw.rounded_rectangle((52 * AA, 44 * AA, 690 * AA, 148 * AA), radius=18 * AA, fill=(255, 255, 255, 218), outline=(180, 158, 124, 180), width=2 * AA)
    draw_text(draw, (80, 64), badge, 17, "#8a4b2d", True)
    draw_text(draw, (80, 91), title, 31, "#1f2937", True)
    draw_text(draw, (80, 127), subtitle, 17, "#475569")


def label(draw: ImageDraw.ImageDraw, xy, text, color="#1f2937") -> None:
    x, y = xy
    draw.rounded_rectangle((x * AA, y * AA, (x + 265) * AA, (y + 48) * AA), radius=10 * AA, fill=(255, 255, 255, 218), outline=(148, 163, 184, 160), width=1 * AA)
    draw_text(draw, (x + 14, y + 13), text, 17, color, True)


def render_master_plan() -> None:
    img, draw = canvas()
    iso = Iso(1015, 120, 29)
    draw_plot(draw, iso, True)
    soft_shadow(draw, iso)
    draw_floor(draw, iso)
    draw_walls(draw, iso, cut_front=True, glass=True)
    draw_interior(draw, iso)
    draw_roof(draw, iso, full=False, alpha=190)
    title_block(draw, "3D Isometric Master Plan", "Một công trình 10×20m trong sân vườn 15×35m", "V7 · VISUAL SSOT")
    label(draw, (1110, 112), "Mái dốc 2 mái đầu hồi tam giác", "#8a4b2d")
    label(draw, (1080, 170), "Ngói cong màu đất nung", "#8a4b2d")
    label(draw, (1020, 705), "F&B 120-130m² / Kids 70-80m²", "#334155")
    save(img, OUT / "v7_master_plan_coherent.png")


def render_exterior() -> None:
    img, draw = canvas("#eee7dc")
    iso = Iso(995, 180, 34)
    draw_plot(draw, iso, detailed=False)
    soft_shadow(draw, iso)
    draw_floor(draw, iso)
    draw_walls(draw, iso, cut_front=False, glass=True)
    draw_roof(draw, iso, full=True, alpha=255)
    for x, y in [(3, 3.2), (5.8, 3.0), (10.8, 3.0), (12.6, 4.4), (1.5, 14), (14.0, 18)]:
        draw_table(draw, iso, x, y, 0, 0.75)
    title_block(draw, "Ngoại Thất Đồng Bộ Master Plan", "Cùng nhà 10×20m, cùng mái ngói cong và sân vườn", "EXTERIOR · V7")
    label(draw, (980, 146), "Đầu hồi tam giác trước/sau", "#8a4b2d")
    label(draw, (1050, 204), "Mái ngói cong, 2 dốc", "#8a4b2d")
    label(draw, (970, 665), "Cửa kính mở ra sân vườn", "#334155")
    save(img, OUT / "v7_exterior_curved_tile_roof.png")


def render_cutaway() -> None:
    img, draw = canvas("#f4efe4")
    iso = Iso(1015, 170, 34)
    draw_plot(draw, iso, detailed=False)
    soft_shadow(draw, iso)
    draw_floor(draw, iso)
    draw_walls(draw, iso, cut_front=True, glass=True)
    draw_interior(draw, iso)
    draw_roof(draw, iso, full=False, alpha=145, lifted=True)
    title_block(draw, "Nội Thất Cắt Mái Đồng Nhất", "Mái được nâng/cắt để thấy đúng layout 65/35", "CUTAWAY · V7")
    label(draw, (1000, 140), "Mái cong cùng ngoại thất", "#8a4b2d")
    label(draw, (1000, 198), "Vách kính cách âm full-width", "#334155")
    label(draw, (980, 735), "Cùng phân khu với mặt bằng", "#334155")
    save(img, OUT / "v7_interior_roof_cutaway.png")


def render_layout() -> None:
    img, draw = canvas("#f8f5ef")
    draw.rounded_rectangle((80 * AA, 70 * AA, 1520 * AA, 930 * AA), radius=28 * AA, fill="#ffffff", outline="#c8b99b", width=3 * AA)
    title_block(draw, "Layout 10×20m Kiểm Soát Đồng Nhất", "Nguồn đối chiếu cho master plan, ngoại thất và cutaway", "LAYOUT · V7")

    x0, y0, scale = 345, 210, 33
    bw, bl = 10 * scale, 20 * scale
    draw.rectangle((x0 * AA, y0 * AA, (x0 + bw) * AA, (y0 + bl) * AA), fill="#efe7d9", outline="#334155", width=4 * AA)
    split = y0 + 13 * scale
    draw.rectangle((x0 * AA, y0 * AA, (x0 + bw) * AA, split * AA), fill="#d8d0c1", outline="#334155", width=3 * AA)
    draw.rectangle((x0 * AA, split * AA, (x0 + bw) * AA, (y0 + bl) * AA), fill="#efd9a6", outline="#334155", width=3 * AA)

    # Full-width glass partition.
    draw.rectangle((x0 * AA, (split - 7) * AA, (x0 + bw) * AA, (split + 7) * AA), fill=(108, 148, 162, 120), outline="#1f2937", width=2 * AA)
    draw_text(draw, (x0 + bw / 2, split - 24), "VÁCH KÍNH CÁCH ÂM TOÀN BỀ NGANG", 17, "#1f2937", True, "mm")

    draw_text(draw, (x0 + bw / 2, y0 + 6.4 * scale), "GLOBAL LOUNGE / F&B\n120-130m²", 25, "#334155", True, "mm", "center")
    draw_text(draw, (x0 + bw / 2, split + 3.5 * scale), "SMART ZONE / CLB\n70-80m²", 24, "#7a4d15", True, "mm", "center")

    # Furniture cues.
    for tx, ty in [(2, 3), (4, 3), (6, 3), (8, 3), (3, 7), (5, 7), (7, 7)]:
        cx, cy = x0 + tx * scale, y0 + ty * scale
        draw.ellipse(((cx - 14) * AA, (cy - 10) * AA, (cx + 14) * AA, (cy + 10) * AA), fill="#b88755")
    draw.rounded_rectangle(((x0 + 1 * scale) * AA, (y0 + 0.7 * scale) * AA, (x0 + 9 * scale) * AA, (y0 + 1.65 * scale) * AA), radius=10 * AA, fill="#b88755", outline="#6f4e37", width=2 * AA)
    draw_text(draw, (x0 + 5 * scale, y0 + 1.18 * scale), "QUẦY BAR", 16, "#ffffff", True, "mm")
    draw.rounded_rectangle(((x0 + 6.7 * scale) * AA, (split + 1.2 * scale) * AA, (x0 + 9.3 * scale) * AA, (split + 4.5 * scale) * AA), radius=12 * AA, fill="#c89555", outline="#6f4e37", width=2 * AA)
    draw_text(draw, (x0 + 8 * scale, split + 2.9 * scale), "NHÀ CHƠI\nGỖ", 16, "#ffffff", True, "mm", "center")

    # Dimensions and roof invariant.
    draw.line(((x0 - 42) * AA, y0 * AA, (x0 - 42) * AA, (y0 + bl) * AA), fill="#1f2937", width=3 * AA)
    draw_text(draw, (x0 - 88, y0 + bl / 2), "20m", 25, "#1f2937", True, "mm")
    draw.line((x0 * AA, (y0 + bl + 42) * AA, (x0 + bw) * AA, (y0 + bl + 42) * AA), fill="#1f2937", width=3 * AA)
    draw_text(draw, (x0 + bw / 2, y0 + bl + 78), "10m", 25, "#1f2937", True, "mm")

    rx, ry = 1040, 325
    roof = [(rx, ry + 130), (rx + 220, ry), (rx + 440, ry + 130), (rx + 390, ry + 162), (rx + 220, ry + 62), (rx + 50, ry + 162)]
    poly(draw, roof, "#bd5b3e", "#87402f", 3)
    for i in range(0, 8):
        yy = ry + 25 + i * 18
        draw.arc(((rx + 35) * AA, yy * AA, (rx + 405) * AA, (yy + 40) * AA), 8, 172, fill="#f0b17f", width=2 * AA)
    draw_text(draw, (1260, 535), "Mái dốc hai mái\nđầu hồi tam giác\nngói cong", 26, "#8a4b2d", True, "mm", "center")
    save(img, OUT / "v7_layout_10x20_roof_ssot.png")


def main() -> None:
    render_master_plan()
    render_exterior()
    render_cutaway()
    render_layout()
    print("Generated v7 coherent render set:")
    for name in [
        "v7_master_plan_coherent.png",
        "v7_exterior_curved_tile_roof.png",
        "v7_interior_roof_cutaway.png",
        "v7_layout_10x20_roof_ssot.png",
    ]:
        print(f"- images/{name}")


if __name__ == "__main__":
    main()
