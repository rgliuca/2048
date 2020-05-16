from getkey import getch


while True:
  c=getch()
  print(c, ":", chr(c[0]))
  if c==b'\x03':
    break

  

