# Kattis problem link: https://open.kattis.com/problems/cudoviste
import sys

rows = []
first_line = True
for line in sys.stdin:
    if first_line:
        first_line = False
        continue
    rows.append(line.strip())

crushed = [0] * 5
for i in range(len(rows) - 1):
    line_a, line_b = rows[i], rows[i + 1]
    for j in range(len(line_a) - 1):
        four_square = line_a[j: j + 2] + line_b[j: j + 2]
        if '#' in four_square:
            continue
        else:
            crushed[four_square.count('X')] += 1

for c in crushed:
    print(c)
