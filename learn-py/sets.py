from hashlib import new


myset = {"apple", "banana", "cherry"}
#* Note: Set items are unchangeable, but you can remove items and add new items.


#? Sets cannot have two items with the same value. {1,1}
myset = {'anas', 'jaidi', 'anas'}
print(myset) # {'anas', 'jaidi'}

print(len(myset)) # 2

#? lop in set
newset = {x for x in myset if x != 'banana'}
print(newset) # {'anas', 'jaidi'}

for item in newset:
  print(item) # jaidi \n anas 
  

#? check if item in set
print('jAidi'.lower() in newset) # True


#? add item to set
newset.add('robin')
newset.update({'anas', 'robin', 'hood'}) #! skip the exsisting values and accept (list, tuple, set, dec)
print(newset)


#? remove
newset.discard('anas') #? remove 'anas'
print(newset) # {'robin', 'hood', 'jaidi'}
newset.pop() #? remove randomly because they are no 
print(newset)
newset.clear()
print(newset)
del newset
# print(newset)