#!/usr/bin/env python3
import cairosvg

input1=input("What do you want line 1 to say?")
input2=input("What do you want line 2 to say?")
input3=input("What do you want line 3 to say?")

svg_contents= """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg version="2" viewBox="0 0 4000 2370" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" xml:space="preserve">
  <!-- per spec x-height (254, from font size 500px), A4 dimensions are approx 11.5 (width), 8.5 (height) ex -->
  <defs>
    <style>
      svg, use, g {
        font-family: British Rail Dark Extended;
        fill: #fff;
        font-size: 500px;
      }
      .slate {
        fill:#f0f0f0;
      }
      .arrow {
        fill:dodgerblue;
      }
      .spacer {
        stroke: none;
        fill: none;
      }
    </style>
</defs>
<rect x="0" y="0" width="16ex" height="9.5ex" fill="#e00000" />

<text x="0" y="2ex"><tspan>    Warning</tspan></text>
<text x="0" y="4.5ex"><tspan>    (input1)</tspan></text>
<text x="0" y="6.5ex"><tspan>    (input2)</tspan></text>
<text x="0" y="8.5ex"><tspan>    (input3)</tspan></text>
</svg>""".replace("(input1)", input1).replace("(input2)",input2).replace("(input3)",input3) 
cairosvg.svg2png(output_width=(512),
    bytestring=(svg_contents), write_to="output.png",)