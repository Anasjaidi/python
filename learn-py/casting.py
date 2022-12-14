"""
  Casting in python is therefore done using constructor functions:
    int() - constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (providing the string represents a whole number)
    float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer)
    str() - constructs a string from a wide variety of data types, including strings, integer literals and float literals
"""
x = 1.5
s = "3.5"

xs = float(s)
sx = str(x)

print(type(xs), type(sx)) # float, str