print(1 + 2) # 3
print(1 - 2) # -1
print(1 / 2) # 0.5
print(5 // 2) # 2 => devide floor
print(2 ** 2) # 4
print(2 % 2) # 0

x = 1

x += 2 # x = x + 2 
print(x) #  3
x -= 2 # x = x - 2 
print(x) #  -1
x *= 2 # x = x * 2 
print(x) #  2
x /= 2 # x = x / 2 
print(x) #  0.5
x **= 2 # x = x ** 2 
print(x) #  1
x //= 2 # x = x // 2 
print(x) #  0
x %= 2 # x = x % 2 
print(x) #  1


print(bool(1 == 1)) # True
print(bool(1 >= 1)) # True
print(bool(1 <= 1)) # True
print(bool(1 != 1)) # false
print(bool(1 < 1)) # false
print(bool(1 > 1)) # false


print(bool(1 and '')) # false
print(bool(1 or '')) # True
print(bool(not(1))) # False

print('*' * 10)
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # True #? Returns True if both variables are the same object
print(x is y) # False
print(x is not y) # True #? Returns True if both variables are not the same object
print(x == y) # False


print('*' * 10)
print(bool('apple' in x)) # True
print(bool('apple' not in  x)) # False

print('*' * 10)
print(bin(1 & 1)) # 0000001 #? Sets each bit to 1 if both bits are 1
print(bin(1 | 2)) # 0000011 #? Sets each bit to 1 if one of bits are 1
print(bin(1 ^ 2)) # 0000011 #? Sets each bit to 1 if only one of two bits is 1
print(bin(~1)) # invert