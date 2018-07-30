import sys


for line in sys.stdin:

   # checking if end of input
   if line == '0 0':
      break

   # checking if its a new test case
   if len(line.split()) == 2:
      num_heads, num_knights = int(line.split()[0]), int(line.split()[1])
      heads = []
      knights = []
      coins = 0
      continue

   if num_heads:
      heads.append(int(line))
      num_heads -= 1

   elif num_knights:
      knights.append(int(line))
      num_knights -= 1

   if not num_knights:
      knights = sorted(knights)
      heads = sorted(heads)
      i = 0
      while i < len(knights):
         j = 0
         while j < len(heads) and knights[i] < heads[j]:
            j += 1
         if j < len(heads):
            coins += knights[i]
            del heads[j]
         i += 1
      if heads:
         print('Loowater is doomed!')
      else:
         print(coins)