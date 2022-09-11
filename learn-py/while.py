from curses.ascii import isupper


i = -1
def inc(reset): 
  global i
  if reset: i = -1; return -1
  i += 1; return i


s = 'ANAS JAIDI'
tab = list(s)
while inc(0) < len(tab):
  if 65 <= ord(tab[i]) <= 90:
    tab[i] = ord(tab[i]); tab[i] += 32
    tab[i] = chr(tab[i])
else:
  print('exited without break')
s = ''.join(tab)
print(s)