# ------------------------------------------------
# 1️⃣ PRINTING AND VARIABLES
# ------------------------------------------------

# Basic print statement
print("Hello, World!")

# Variable assignment
number = 10             # Integer variable
name = "John"           # String variable

# Using format() for string formatting
print('My number is {one} and my name is {two}'.format(one=number, two=name))
# ⚠️ Below line prints the placeholders literally — incorrect format
print('My number is {number} and my name is {name}')

# Using f-string (✅ modern and preferred)
print(f'My number is {number} and my name is {name}')
print(f'My name is {name}')


# ------------------------------------------------
# 2️⃣ STRINGS
# ------------------------------------------------

s = 'Hello'
print(s[0:2])    # String slicing → Output: 'He'

# Common string methods
text = 'hello world'
print(text.title())    # Capitalizes first letter of each word
print(text.upper())    # Converts to uppercase
print(text.split())    # Splits into a list by spaces

tweet = 'Go splits! # Sports'
print(tweet.split('#'))     # Split string by '#'
print(tweet.split('#')[1])  # Access the part after '#'


# ------------------------------------------------
# 3️⃣ LISTS
# ------------------------------------------------
# Lists are ordered, mutable (changeable), and use [ ]

my_list = [1, 2, 3, 4, 5]
my_list.append(6)         # Add element at end
my_list.pop(3)            # Remove element at index 3
print(my_list)

# Lists are mutable
new_list = [0, 1, 2]
new_list[0] = 'new'       # Modify element
print(new_list)

# List operations
f = [1, 2, 3, 4, 5]
g = [6, 7, 8, 9, 10]

f.append(6)
f.pop(1)
f.insert(4, 'changed')

print(f[::-1])            # Reverse list
print(f)

combined = f + g          # Combine two lists
print(combined)


# ------------------------------------------------
# 4️⃣ TUPLES
# ------------------------------------------------
# Tuples are ordered and immutable (cannot change)
t = (1, 2, 3)
print(t)

# Convert tuple → list → modify → back to tuple
tup = (1, 2, 3)
lst = list(tup)
lst.append(4)
t = tuple(lst)
print(t)


# ------------------------------------------------
# 5️⃣ SETS
# ------------------------------------------------
# Sets store unique values only (no duplicates)
list_vals = [1, 1, 1, 2, 2, 2, 3, 3, 3]
unique_set = set(list_vals)
print(unique_set)    # Output: {1, 2, 3}


# ------------------------------------------------
# 6️⃣ DICTIONARIES
# ------------------------------------------------
# Dictionaries store key-value pairs using { }

d = {'key1': 'value', 'key2': 123}
print(d['key1'])
print(d['key2'])

# Nested dictionaries
dict1 = {'key1': {'nested_dict': [1, 2, 3, 4, 5]}}
print(dict1['key1']['nested_dict'][2])

d = {'outside_key': {'inside_key': 'Value inside'}}
print(d['outside_key']['inside_key'])

# Add and update dictionary values
details = {'name': 'Jay', 'age': 26, 'country': 'India'}
details['email'] = 'jd@gmail.com'
details['place'] = 'KOP'
print(details)

student = {'marks': {'math': 90, 'science': 85}}
print(student['marks'])

# Dictionary methods
d = {'k1': 1, 'k2': 2}
print(d.keys())     # Get keys
print(d.values())   # Get values
print(d.items())    # Get key-value pairs


# ------------------------------------------------
# 7️⃣ BOOLEAN
# ------------------------------------------------
a = True
print(a)


# ------------------------------------------------
# 8️⃣ CONDITIONALS (if, elif, else)
# ------------------------------------------------
if 1 < 2:
    print('Yes, 1 is less than 2')

if 1 == 3:
    print('First')
elif 3 == 1:
    print('Middle')
else:
    print('Last')


# ------------------------------------------------
# 9️⃣ LOOPS (for & while)
# ------------------------------------------------

# FOR loop - iterate over list
seq = [1, 2, 3, 4, 5]
for item in seq:
    print(item)

for i in seq:
    print('Hello')

# WHILE loop
i = 1
while i < 5:
    print(f'i is: {i}')
    i += 1

i = 7
while i <= 10:
    print(f'Value of i: {i}')
    i += 1


# ------------------------------------------------
# 🔟 RANGE FUNCTION
# ------------------------------------------------
for x in range(0, 5):
    print(x)   # Prints 0,1,2,3,4


# ------------------------------------------------
# 1️⃣1️⃣ LIST COMPREHENSION
# ------------------------------------------------

nums = [1, 2, 3, 4, 5]

# Regular way
out = []
for num in nums:
    out.append(num**2)
print(out)

# Shorter way using list comprehension
out = [num**3 for num in nums]
print(out)

# Another example
k = [2, 4, 5, 6]
p = [item**2 for item in k]
print(p)


# ------------------------------------------------
# 1️⃣2️⃣ FUNCTIONS
# ------------------------------------------------

# Simple function
def my_fun(param1):
    """Print the parameter value"""
    print(param1)

my_fun('hello')


# Function with string input
def myname(name):
    """Print a greeting"""
    print('Hello ' + name)

myname('Jay')


# Function with return value
def square(num):
    """Return square of a number"""
    return num**2

print(square(3))


# Function returning sum
def add_fun(num1, num2):
    """Print sum of two numbers"""
    print(num1 + num2)

add_fun(100, 250)


# Function to check even number
def is_even(num):
    """Check if a number is even"""
    if num % 2 == 0:
        print(True)
    else:
        print(False)

is_even(3)


# Function returning list of squared numbers
def square_list(numbers):
    squared = []
    for item in numbers:
        squared.append(item**2)
    return squared

nums = [1, 2, 3]
print(square_list(nums))


# ------------------------------------------------
# 1️⃣3️⃣ MAP, FILTER, LAMBDA FUNCTIONS
# ------------------------------------------------

# Regular function
def times2(num): 
    return num ** 2

print(times2(5))

# Using map() - applies a function to each element
lst = list(map(times2, [2, 3, 4, 6]))
print(lst)

# Using lambda (anonymous function)
sequence = [1, 2, 3, 4, 5]
tripled = list(map(lambda num: num * 3, sequence))
print(tripled)

squared = list(map(lambda x: x**2, [1, 2, 3]))
print(squared)

# Adding a fixed number using lambda + map
a = 10
lst = list(map(lambda x: x + 10, [a]))
print(lst)

# filter() - filter elements based on a condition
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda num: num % 2 == 0, nums))
print(even_nums)


# ------------------------------------------------
# 1️⃣4️⃣ OPERATORS & UNPACKING
# ------------------------------------------------

# 'in' operator
x = 'x' in [1, 2, 3]
print(x)  # False

# Tuple inside list
pairs = [(1, 2), (3, 4)]
print(pairs[1][1])   # Access 4
print(pairs[1])      # (3,4)

# Tuple unpacking
for (a, b) in pairs:
    print(a)


# ------------------------------------------------
# ✅ PRACTICE OUTPUT CHECKS
# ------------------------------------------------
a, b = 5, 10
print(f'Sum of {a} and {b} is {a+b}')

word = 'Python'
print(word[1:3])     # 'yt'
print(word[3::-1])   # Reverse from index 3
print(word[-2:])     # Last 2 letters
print(word[4::-1])   # Reverse from index 4
print(word[0::2])    # Skip every 2nd char

# Range examples
for i in range(0, 11):
    print(i)

for _ in range(0, 5):
    print('Hello')

# Reverse countdown
for i in range(10, 0, -1):
    print(i)

# Print even numbers from list
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in lst:
    if i % 2 == 0:
        print(i)

print("✅ End of Python Basics Practice File")


# 🧠 Python Crash Course Exercises

# What is 7 to the power of 4?
x = 7 **4
print(x)
# Split this string: "s = 'Hi there Sam!'"
s = 'Hi there Sam!'
print(s.split())
# Turn it into a list.
lst  = list(s.split())
print(lst)
# Given the variables, use .format() to print a formatted string.
planet = 'Earth'
diameter = 12742
print(f'The diameter of planet {planet} is {diameter}')

# Given this nested list, use indexing to grab the word "hello".
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])  # Output: hello

# Given this nested dictionary, grab the word "hello".
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

# What is the main difference between a tuple and a list?

# Create a function that grabs the email website domain from a string like "user@domain.com".
# **So for example, passing "user@domain.com" would return: domain.com**
def email(emailid):
        username, domain = emailid.split('@')
        print(domain + ' domain and this is username '+ username)
        
email('jaydale@gmail.com')

# Example: "user@domain.com" → returns "domain.com".

# Create a basic function that returns True if the word "dog" is contained in the input string (ignore case and punctuation).
def findDog(sentence):
    sentence = sentence.lower().split()
    for word in sentence:
        if 'dog' in word:
            return True   
    return False

def findDog(sentence):
    return 'dog' in sentence.lower().split()

findDog('Is there a dog here?')

# Create a function that counts how many times the word "dog" occurs in a string.
def countDog(sentence):
    x = 0 
    sentence = sentence.lower().split()
    for word in sentence:
        if 'dog' in word:
            x = x + 1
    return x   

countDog('This dog runs faster than the other dog dude!')

# Use lambda expressions and the filter() function to filter out words from a list that don’t start with the letter ‘s’.

seq = ['soup','dog','salad','cat','great']
s = []
for word in seq:
   if word[0] == 's':
    s.append(word)
print(s)

lambda word : word[0] == 's', seq

# result = list(filter(lambda word: word[0] == 's', seq))

lst = list(filter (lambda word : word[0] == 's', seq))
print(lst)
lst = list(filter (lambda word :word[0] ==  's',seq) )
print(lst)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = []
# for num in nums:
#     if num % 2 == 0:
#         n.append(num)

# print(n)

lst = list(filter(lambda num : num % 2 == 0, nums) )
print(lst)  
# You are driving a little too fast, and a police officer stops you — write a function (the prompt continues in the notebook).