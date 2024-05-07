#hvdfg5bfbfbfvd5bvf9b965fbf6b5f
#print alphabet and numbers separete

str1 = "bnh658drf5vdf8b4vdf52d5bfd4v f54v545cxv 5c4"   #take a string

alphabets =[]   # take empty list
number =[]

for char in str1:
    if char.isalpha():     #check if alpha or number and append
        alphabets.append(char)
    else:
        number.append(char)

final_list = (sorted(alphabets)+(sorted(number)))    #used sorted builtin function
output=' '.join(final_list)                         # added
print(output)
