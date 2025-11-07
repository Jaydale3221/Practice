print("Hello, World!");

number = 10
name = "John"
print('My number is {one} and my name is {two}' .format(one=number, two=name));

print(f'My name is  {name}')

s = 'Hello'
print(s[0:2])


my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)

d = {'key1':'value' , 'key2':123}
print(d['key1']) 

print(d['key2'])

dict = {'key1': {'nested_dict':[1,2,3,4,5]}}
print(dict['key1']['nested_dict'][2])

#Nested Dictionary
d ={'outside_key': {'inside_key' :'Value inside the inside key'}} 
print(d['outside_key']['inside_key'])
