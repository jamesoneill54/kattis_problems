import sys

def cool_translate(line):
   translations = {
   'a':'@', 'b':'8',
   'c':'(', 'd':'|)',
   'e':'3', 'f':'#',
   'g':'6', 'h':'[-]',
   'i':'|', 'j':'_|',
   'k':'|<', 'l':'1',
   'm':'[]\/[]', 'n':'[]\[]',
   'o':'0', 'p':'|D',
   'q':'(,)', 'r':'|Z',
   's':'$', 't':'\'][\'',
   'u':'|_|', 'v':'\/',
   'w':'\/\/', 'x':'}{',
   'y':'`/', 'z':'2'
   }

   line = line.strip().lower()
   new_line = ''
   for l in line:
      if l in translations:
         l = translations[l]
      new_line += l
   return new_line

line_in = sys.stdin.readline()
print(cool_translate(line_in))