#!/usr/bin/env python3
"""Regenerate ttyd's vector and raster icons: python3 scripts/generate-icons.py (Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1] / 'src'
ICONS = ROOT / 'icons'
ICONS.mkdir(exist_ok=True)
BACKGROUND = '#18282e'
FOREGROUND = '#f5f8f8'
ACCENT = '#7dd3c7'
STROKES = [(FOREGROUND, [(152, 176), (232, 256), (152, 336)]),
           (ACCENT, [(280, 336), (360, 336)])]
svg = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512">',
       '  <title>ttyd</title>', f'  <path fill="{BACKGROUND}" d="M0 0h512v512H0z"/>']
for color, points in STROKES:
    commands = 'M' + ' L'.join(f'{x} {y}' for x, y in points)
    svg.append(f'  <path d="{commands}" fill="none" stroke="{color}" stroke-width="32" stroke-linecap="round" stroke-linejoin="round"/>')
svg.append('</svg>')
(ICONS / 'terminal.svg').write_text('\n'.join(svg) + '\n')
canvas = Image.new('RGB', (2048, 2048), BACKGROUND)
draw = ImageDraw.Draw(canvas)
for color, points in STROKES:
    draw.line([(x * 4, y * 4) for x, y in points], fill=color, width=128)
    for x, y in points:
        draw.ellipse(((x - 16) * 4, (y - 16) * 4, (x + 16) * 4, (y + 16) * 4), fill=color)
for name, size in [('apple-touch-icon', 180), ('icon-192', 192), ('icon-512', 512)]:
    canvas.resize((size, size), Image.Resampling.LANCZOS).save(ICONS / f'{name}.png')
canvas.resize((32, 32), Image.Resampling.LANCZOS).save(ROOT / 'favicon.png')
