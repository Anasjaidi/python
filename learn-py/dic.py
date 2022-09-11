from unicodedata import name


mydic = {
  'name': 'anas jaidi',
  'age': 'x'
}

print(mydic) # {'name': 'anas jaidi', 'age': 'x'}

#? acces
print(mydic.get('name')) # anas jaidi
print(mydic['name']) # anas jaidi
print([x for x in mydic.keys()]) # ['name', 'age']
print([x for x in mydic.values()]) # ['anas jaidi', 'x']
print([x for x in mydic.items()]) # [('name', 'anas jaidi'), ('age', 'x')]


#? update item and add 
mydic['age'] = '19'
print(mydic.get('age')) # 19
mydic.update({'age':'x'})
print(mydic.get('age')) # x


#? delete 
dic = mydic.copy()
print(dic) # {'name': 'anas jaidi', 'age': 'x'}
dic.pop('age') #? remove by key
print(dic) # {'name': 'anas jaidi'}
dic.popitem() #? remove randemly
print(dic) # {}
dic['test'] = True
print(dic) # {'test': True}
dic.clear()