# ================================================
# 🐍 PYTHON BASICS - Quick Reference / Study Notes
# ================================================

# ------------------------------------------------
# 1️⃣ PRINTING AND VARIABLES
# ------------------------------------------------
print("Hello, World!")   # Print statement

number = 10              # Integer variable
name = "John"            # String variable

# Using format() for string formatting
print('My number is {one} and my name is {two}'.format(one=number, two=name))
print('My number is {number} and my name is {name}') # this is wrong - it prints {number} and {name}
print(f'My number is {number} and my name is {name}')

# Using f-string (modern and preferred way)
print(f'My name is {name}')


# ------------------------------------------------
# 2️⃣ STRINGS
# ------------------------------------------------
s = 'Hello'
print(s[0:2])            # String slicing → prints 'He'


# ------------------------------------------------
# 3️⃣ LISTS
# ------------------------------------------------
# Lists are ordered, mutable collections (use [ ])
my_list = [1, 2, 3, 4, 5]
my_list.append(6)        # Add an element
my_list.pop(3)           # Remove element at index 3
print(my_list)

# Lists are mutable
new_list = [0, 1, 2]
print(new_list)
new_list[0] = 'new'      # Changing value at index 0
print(new_list)


# ------------------------------------------------
# 4️⃣ TUPLES
# ------------------------------------------------
# Tuples are ordered and immutable (use ( ))
t = (1, 2, 3)
print(t)


# ------------------------------------------------
# 5️⃣ SETS
# ------------------------------------------------
# Sets contain only unique elements (use { })
my_set = set([1,1,1,2,2,2])
print(my_set)            # Output: {1, 2}


# ------------------------------------------------
# 6️⃣ DICTIONARIES
# ------------------------------------------------
# Dictionaries store key-value pairs (use { })
d = {'key1':'value', 'key2':123}
print(d['key1'])
print(d['key2'])

# Nested dictionary
dict1 = {'key1': {'nested_dict': [1,2,3,4,5]}}
print(dict1['key1']['nested_dict'][2])

# Another nested dictionary example
d = {'outside_key': {'inside_key': 'Value inside the inside key'}}
print(d['outside_key']['inside_key'])

# Dictionary examples continued
d = {'key1': 'value1', 'key2': 'value2'}
print(d['key2'])

d = {'key1': {'key2': 'nestedValue'}}
print(d['key1']['key2'])


# ------------------------------------------------
# 7️⃣ BOOLEAN
# ------------------------------------------------
a = True
print(a)

# ------------------------------------------------
# 8️⃣ CONDITIONALS (if, elif, else)
# ------------------------------------------------
if 1 < 2:
    print('yes')

if 1 == 3:
    print('first')
elif 3 == 1:
    print('middle')
else:
    print('last')


# ------------------------------------------------
# 9️⃣ LOOPS
# ------------------------------------------------
# FOR LOOP - iterate over sequence
seq = [1, 2, 3, 4, 5]
for item in seq:
    print(item)

for i in seq:
    print('hello')

# WHILE LOOP
i = 1
while i < 5:
    print(f'i is : {i}')
    i = i + 1

i = 7
while i <= 10:
    print(f'Value of i : {i}')
    i = i + 1


# ------------------------------------------------
# 🔟 RANGE FUNCTION
# ------------------------------------------------
# Used to generate a sequence of numbers
for x in range(0, 5):
    print(x)


# ------------------------------------------------
# 1️⃣1️⃣ LIST COMPREHENSION
# ------------------------------------------------
nums = [1, 2, 3, 4, 5]

# Normal way
out = []
for num in nums:
    out.append(num**2)
print(out)

# List comprehension (shorter way)
out = [num**3 for num in nums]
print(out)

# Another example
k = [2, 4, 5, 6]
p = [item**2 for item in k]
print(p)


# ------------------------------------------------
# 1️⃣2️⃣ FUNCTIONS
# ------------------------------------------------
# Defining a function
def my_fun(param1):
    """Simple function that prints its parameter"""
    print(param1)

my_fun('hello')

# Function with string input
def myname(str):
    """Prints a greeting"""
    print('Hello ' + str)

myname('a')

# Function with return value
def square(num):
    """Returns the square of a number"""
    return num**2

output = square(3)
print(output)

# ------------------------------------------------
# ✅ END OF PYTHON BASICS
# ------------------------------------------------
# practice
a = 5 
b = 10
print(f'Sum of {a} and {b} is {a+b}')

word = 'Python'
print(word[1:3])
print(word[3::-1])
print(word[-2:])
print(word[4::-1])
print(word[0::2])

text = 'hello world'
print(text.title())

f = [1,2,3,4,5]
g = [6,7,8,9,10]

f.append(6)
f.pop(1)
f.insert(4, 'changed')
print(f[::-1])
print(f)
combined = f + g
print(combined)

tup = (1,2,3)
lst = list(tup)
lst.append(4)
t = tuple(lst)
print(t)


list = [1,1,1,2,2,2,2,3,3,3]
s = set(list)
print(s)


detail = {'name': 'Jay','age':26, 'country': 'India'}
detail['email'] = 'jd@gmail.com'
detail['place'] = 'KOP'
print(detail)

student = {'marks': {'math': 90, 'science': 85}}
print(student['marks'])

for i in range(0,11):
    print(i)

for word in range(0,5):
    print('Hello')

i = 5
while i<=10:
    print(i)
    i = i + 1

squr = [1,2,3,4,5]
for item in squr:
    print(item**2)

for i in range(10,0,-1):
    print(i)

lst= [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i % 2 == 0:
        print(i)

def myfun(para):
    print('Hello ' + para)

myfun('jay')


def add_fun(num1, num2):
    return print(num1 + num2)
add_fun(100,250)

def is_even(num):
    if num % 2 ==0:
        print(True)
    else:
        print(False)
        
is_even(3)

def sqaure_list(numbers):
    squared = []
    for item in numbers:
        squared.append(item**2)
    return squared

nums = [1,2,3]
print(sqaure_list(nums))


def squaredlist(num):
    squared = []
    for item in num:
        squared.append(item**2)
    return squared

num = [2,3,4,6]
print(squaredlist(num))