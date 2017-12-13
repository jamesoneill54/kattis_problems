import sys

# must use only the given operators and four 4's
# to make value for each line in the input. 
# output 'no solution' if not possible. 

operators = ['//', '*', '-', '+']
output_ops = ['/', '*', '-', '+']

# start on '4 + 4 + 4 + 4' and end on '4 / 4 / 4 / 4'

expressions = {}

i = 0
while i < len(operators):
   j = 0
   while j < len(operators):
      k = 0
      while k < len(operators):
         express = '4 {:s} 4 {:s} 4 {:s} 4'.format(output_ops[i],output_ops[j],output_ops[k])
         evaluation = eval('4 {:s} 4 {:s} 4 {:s} 4'.format(operators[i],operators[j],operators[k]))
         expressions[evaluation] = express
         k += 1
      j += 1
   i += 1


line_num = int(sys.stdin.readline().strip())
inc = 0
while inc < line_num:
   n = int(sys.stdin.readline().strip())
   if n in expressions:
      print('{:s} = {:d}'.format(expressions[n], n))
   else:
      print('no solution')

   inc += 1