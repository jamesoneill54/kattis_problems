import sys
from math import sqrt

first_line = True

for line in sys.stdin:
   if first_line:
      box_dimensions = [int(n) for n in line.strip().split()[1:]]
      max_len = sqrt((box_dimensions[0] ** 2) + (box_dimensions[1] ** 2))
      first_line = False
      continue
   else:
      if int(line.strip()) <= max_len:
         print('DA')
      else:
         print('NE')