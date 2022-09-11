t = ('anas', 'jaidi', 'robin', 'hood')
print(t)  # ('anas', 'jaidi', 'robin', 'hood')
# * tupples are not changable can be sliced because they are indexed

print(t[0])  # 'anas' #? accesed by index

# * if we need to insert or remove we hard code it \
# * by transform it to array and operate then return it to tupple
tab = list(t)
tab.insert(0, 'the me')
t = tuple(tab)
print(t) # ('the me', 'anas', 'jaidi', 'robin', 'hood')

#? unpack tuple

(the_me, anas, jaidi, *nickname) = t
print(the_me, anas, jaidi, nickname) # the me anas jaidi ['robin', 'hood']