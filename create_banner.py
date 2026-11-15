
from pathlib import Path
import base64

image_path = Path("banner.jfif")
output_path = Path("banner.svg.svg")

if not image_path.exists():
    raise FileNotFoundError("banner.jfif was not found!")

image_data = base64.b64encode(image_path.read_bytes()).decode("ascii")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="1200" height="360" viewBox="0 0 1200 360">

  <defs>
    <linearGradient id="neon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#A020F0"/>
      <stop offset="50%" stop-color="#176BFF"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>

    <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="5" result="blur"/>
      <feMerge>
        <feMergeNode in="blur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <clipPath id="imageClip">
      <rect x="18" y="18" width="1164" height="324" rx="22"/>
    </clipPath>
  </defs>

  <rect width="1200" height="360" fill="#080610"/>

  <!-- EMBEDDED BANNER IMAGE -->
  <image x="18" y="18"
         width="1164" height="324"
         preserveAspectRatio="xMidYMid slice"
         clip-path="url(#imageClip)"
         href="data:image/jpeg;base64,{image_data}"/>

  <!-- NEON FRAME -->
  <rect x="8" y="8" width="1184" height="344"
        rx="29" fill="none"
        stroke="url(#neon)" stroke-width="4"
        filter="url(#glow)"/>

  <!-- INNER WHITE BORDER -->
  <rect x="17" y="17" width="1166" height="326"
        rx="23" fill="none"
        stroke="#FFFFFF" stroke-opacity="0.75"
        stroke-width="1.5"/>

  <!-- NEON CORNER DETAILS -->
  <g filter="url(#glow)" fill="#FFFFFF">
    <circle cx="29" cy="29" r="3"/>
    <circle cx="1171" cy="29" r="3"/>
    <circle cx="29" cy="331" r="3"/>
    <circle cx="1171" cy="331" r="3"/>
  </g>

</svg>'''

output_path.write_text(svg, encoding="utf-8")

print(f"Successfully created: {output_path}")
