import sys
from math import sqrt

def len_line(x1, y1, x2, y2):
   return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def midpoint(x1, y1, x2, y2):
   mid_x = (x1 + x2) / 2
   mid_y = (y1 + y2) / 2
   return mid_x, mid_y


line = int(sys.stdin.readline())
while line != 0:
   