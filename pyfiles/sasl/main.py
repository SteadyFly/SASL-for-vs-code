import re


file = open("api.txt")
line = file.read().replace("\n", "\n")

i = 300
v = 0
if i < 301:
    v = v+1

print(line)




separated_string = line.splitlines()
print(separated_string)

print(len(separated_string))
string2 = '"'
string ='": { "prefix": "'
string4 = '", "body": [ "'

string3 = '" ], "description": "WIP" },'
my_new_list = [string2 + x + string + x + string4 + x + string3 for x in separated_string]

print(my_new_list)
my_lst = my_new_list
my_lst_str = ''.join(map(str, my_lst))
print(my_lst_str)

with open('saslexport.txt', 'w') as f:
    f.write(my_lst_str)



