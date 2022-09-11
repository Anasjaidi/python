s = 'anas jaidi'
li = [1, 2, 3]

for c in s:
  print(c, end='') # anas jaidi% 

print('')
for num in li:
  if num != li[-1]:
    print(num, end='\t')
  else:
    print(num)
