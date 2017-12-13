import sys

usr_in = sys.stdin.readline().strip()
sorta_sort = []

while usr_in != '0':


   # if it's a new test
   if usr_in.isdigit():
      if sorta_sort:
         for i in range(len(sorta_sort) - 1):
            print(sorta_sort[i])
         print(sorta_sort[-1] + '\n')
      sorta_sort = []


   # else it's a name
   else:
      name = usr_in
      i = 0
      while i < len(sorta_sort) and name[:2] >= sorta_sort[i][:2]:
         i += 1
      if i < len(sorta_sort):
         sorta_sort.insert(i, name)
      else:
         sorta_sort.append(name)
   

   usr_in = sys.stdin.readline().strip() 


if sorta_sort:
      for i in range(len(sorta_sort)):
         print(sorta_sort[i])