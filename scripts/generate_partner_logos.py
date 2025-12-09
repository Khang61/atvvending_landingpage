#!/usr/bin/env python3
"""Generate SVG placeholder logos for partners"""

import os

partners = [
    # Row 1 - 20 partners
    ("luxshare-ict", "Luxshare ICT"),
    ("foxconn", "Foxconn"),
    ("shunyun", "Shunyun"),
    ("mc-electronic", "M.C Electronic"),
    ("uil-vietnam", "UIL Việt Nam"),
    ("samsung", "Samsung"),
    ("sdv", "SDV"),
    ("semv", "SEMV"),
    ("tenma", "Tenma"),
    ("inoac", "Inoac"),
    ("toyota", "Toyota"),
    ("dong-tau-dai-duong", "Đóng Tàu Đại Dương"),
    ("bv-phuc-yen", "BV Phúc Yên"),
    ("bv-viet-duc", "BV Việt Đức"),
    ("bv-ung-buou", "BV Ung Bướu"),
    ("bao-tang-lich-su", "Bảo Tàng LS"),
    ("keangnam", "Keangnam"),
    ("pvi", "PVI"),
    ("tt-hoi-nghi-qg", "TT Hội Nghị QG"),
    ("khoa-huy-hoang", "Khóa Huy Hoàng"),
    # Row 2 - 19 partners
    ("terumo", "Terumo"),
    ("vietnam-post", "Vietnam Post"),
    ("mitsubishi", "Mitsubishi"),
    ("matsuo", "Matsuo"),
    ("fukang", "Fukang"),
    ("kyocera", "Kyocera"),
    ("yazaki", "Yazaki"),
    ("shin-etsu", "Shin-Etsu"),
    ("pegatron", "Pegatron"),
    ("kcn-vietnam", "KCN Việt Nam"),
    ("nakashima", "Nakashima"),
    ("tkr", "TKR"),
    ("sakura", "Sakura"),
    ("kyoei", "Kyoei"),
    ("dh-thuong-mai", "ĐH Thương Mại"),
    ("hv-chinh-sach", "HV Chính Sách"),
    ("dh-su-pham", "ĐH Sư Phạm 2"),
    ("gach-catalan", "Gạch Catalan"),
    ("gach-ttc", "Gạch TTC"),
]

svg_template = '''<svg xmlns="http://www.w3.org/2000/svg" width="160" height="60" viewBox="0 0 160 60">
  <rect width="160" height="60" fill="#1a1a1a" rx="8"/>
  <text x="80" y="35" text-anchor="middle" fill="#FF6B00" font-family="Montserrat, Arial, sans-serif" font-size="12" font-weight="700">{name}</text>
</svg>'''

output_dir = r"d:\WORK\atvvending\images\partners"
os.makedirs(output_dir, exist_ok=True)

for filename, display_name in partners:
    svg_content = svg_template.format(name=display_name)
    filepath = os.path.join(output_dir, f"{filename}.svg")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Created: {filepath}")

print(f"\nTotal: {len(partners)} logos created")
