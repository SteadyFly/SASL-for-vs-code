#start reading file with datarefs
file = open("datarefex.txt")
line = file.read().replace("\n", "\n")
print(len(line))
#end reading file with datarefs

#convert into proper amount of parts
separated_string = line.splitlines()
print(len(separated_string))
#end

string2 = '"'
string ='": { "prefix": "'
string4 = '", "body": [ "'

string3 = '" ], "description": "WIP" },'
my_new_list = [string2 + x + string + x + string4 + x + string3 for x in separated_string]
print(my_new_list)
my_lst = my_new_list
my_lst_str = ''.join(map(str, my_lst))
print(my_lst_str)

with open('afterconv.txt', 'w') as f:
    f.write(my_lst_str)