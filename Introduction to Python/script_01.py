# First lines of the code
print("Introduction to Python")
print("I wrote my fist line in code Python")
print()

x = 1         # assign variable x the value 1
y = x + 5     # assign variable y the value of x plus 5
z = y         # assign variable z the value of y

# Types variables verification
print("Types variables verification")
print(type(x))
print(type(y))
print(type(z))
print()

# Working with numbers
x1 = 1       # integer
x2 = 1.0     # decimal (floating point)

print("Working with numbers")
print(type(x1))
print(type(x2))
print()

# Working with booleans
x3 = True
print(type(x3)) 
print()

# Working with strings
x4 = 'This is a string'
print(x4)
print(type(x4)) 
y4 = "This is also a string"
x4 = 'Hello' + ' ' + 'World!'
print(x4)
print()

# User input
print('What is your name ?')
name = input('')
print(name)
print()

# Reading numbers as input
print('What is your number ?')
number = int(input(""));
print()

# Converting numbers to stringsda
print("# Converting numbers to strings")
number = str(number)
print(f"The {number} number is ", type(number))