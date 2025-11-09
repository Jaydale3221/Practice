from pickle import TRUE


print("Hello, World!");

number = 10
name = "John"
print('My number is {one} and my name is {two}' .format(one=number, two=name));

print(f'My name is  {name}')

s = 'Hello'
print(s[0:2])


my_list = [1, 2, 3, 4, 5]
my_list.append(6)
my_list.pop(3)
print(my_list)

d = {'key1':'value' , 'key2':123}
print(d['key1']) 

print(d['key2'])

dict = {'key1': {'nested_dict':[1,2,3,4,5]}}
print(dict['key1']['nested_dict'][2])

#Nested Dictionary
d ={'outside_key': {'inside_key' :'Value inside the inside key'}} 
print(d['outside_key']['inside_key'])


a = True
print(a)


t = (1,2,3)

new_list = [0,1,2]
print(new_list)

new_list[0] = 'new'
print(new_list)



#set - is defined by unique elements
my_set = set([1,1,1,1,1,1,1,2,2,2,2,2,2,2,2])
print(my_set)


if 1 < 2:
    print('yes')
    

if 1 == 3:
    print('first')
elif 3 == 1:
    print('middle')
else:
    print('last')


# Dictonaires Boolean Sets 
d = {'key1' : 'value1', 'key2': 'value2'}

print(d['key2'])

# nested dictonaries
d = {'key1' : {'key2' : 'nestedValue'}}
print(d['key1']['key2'])