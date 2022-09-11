


_ = ['anas', 'jaidi']
print(_) # ['anas', 'jaidi']
_[0:2] = ['robin', 'hood']
print(_) # ['robin', 'hood']
print('hood' in _) # True

_.insert(0, 'mqawed')
print(_) # ['mqawed', 'robin', 'hood']
_.append('asat')
print(_) # ['mqawed', 'robin', 'hood', 'asat']
_.extend('asat')
print(_) # ['mqawed', 'robin', 'hood', 'asat', 'a', 's', 'a', 't']

_.pop(0) #? pop by index
print(_) # ['robin', 'hood', 'asat', 'a', 's', 'a', 't']
_.pop() #? pop the last
print(_) # ['robin', 'hood', 'asat', 'a', 's', 'a']
_.remove('a') #? pop by value the first ocuured
print(_) # ['robin', 'hood', 'asat', 's', 'a']
_.clear() #? clear the list values
print(_) # []

#! LOOP
_ = ['anas', 'jaidi']

for i in range(len(_)):
  print(_[i]) # anas \n jaidi
for item in _:
  print(item) # anas \n jaidi
i = -1
while (i < len(_)):
  print(_[i]);i += 1 # anas \n jaidi
  

print('*' * 10)
_.append('mqawd')
new_ = [print(x) for x in _ if 'd'  in x] # jaidi \n mqawd
print(new_) # [None, None]
new_ = [print(x) or x for x in _ if 'd'  in x] # jaidi \n mqawd
print(new_) # [jaidi, mqawed]
new_.sort()
print(new_) # ['jaidi', 'mqawd']
new_.sort(reverse = True)
print(new_) # ['mqawd', 'jaidi']
new_.reverse()
print(new_) # ['jaidi', 'mqawd']


#? copy
print('*' * 10)
new__ = new_.copy()
new___ = list(new__)
print(new___) # ['jaidi', 'mqawd']

#? join

_new = new_ + new__
print(_new) # ['jaidi', 'mqawd', 'jaidi', 'mqawd']
