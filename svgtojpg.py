from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

drawing = svg2rlg("maze.svg")
renderPM.drawToFile(drawing, "maze.jpg", fmt="JPG")