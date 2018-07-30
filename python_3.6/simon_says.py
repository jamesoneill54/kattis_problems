import sys

def simon_says(line):
   line = line.split()
   if ' '.join(line[:2]) == 'Simon says':
      print(' '.join(line[2:]))

n = int(sys.stdin.readline().strip())
i = 0
while i < n:
   simon_says(sys.stdin.readline().strip())
   i += 1