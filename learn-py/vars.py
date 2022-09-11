
#?  Python has no command for declaring a variable.
#?  A variable is created the moment you first assign a value to it.
variable = 10
#*#################

#? CASTING
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#*#################

#? Many Values to Multiple Variables
v1, v2, v3 = -1 ,True,False

#? One Value to Multiple Variables
v1 = v2 = v3 = False

#? Unpack a Collection
col = [1,2,3]
a , b, c = col



#+ log for testing
print(a,b)