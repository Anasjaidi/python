# 'hello' is the same as "hello".

#? to add " inside a string wrap it inside ' or the oposite
s = 'anas "mqwd" asat'
s1 = "anas jaidi"

#? slice from string
#+ slice from begin  to the index 4 snd exclude it
print(s[:4]) # anas 
#+ slice from the 1 to the index 3 snd exclude it
print(s[1:3]) # na
#+ slice from the 4 to the end
print(s[5:]) #  "mqwd" asat

#? case strings
print(s1.upper()) # ANAS JAIDI
print(s1.capitalize()) # Anas jaidi
print(s1.lower()) # anas jaidi

#? Remove Whitespace from 0:-1
s1 = '    ' + s1 + '   ' 
print(s1.strip().upper()) # 'ANAS JAIDI'

#? Replace String
s1 = s1.strip().lower()
print(s1.replace('anas', 'robin').replace('jaidi', 'hood')) # robin hood

#? Split String
print(s1.split()) # ['anas', 'jaidi']
print(s1.split(' ')) # ['anas', 'jaidi']


#? format string 
fs = "{} ok"
print(fs) # {} ok
print(fs.format(s1))  # anas jaidi ok
fs = "first {1}, last {0}"
print(fs.format('jaidi', 'anas'))  # first anas, last jaidi

#? length of string
print(len(s1)) # 10

#? center a string
print(s1.center(12)) # ' anas jaidi '

#? number of times a specified value appears in the string. 
#+ string.count(value, start, end)
print(s1.count('anas')) # 1

#? find index of string in other string
print(s1.find('jaidi')) # 5
print(s1.find('mqwed')) # -1 not found