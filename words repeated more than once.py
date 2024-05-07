# write a program to display the words that are repeated more than once or equl to n times in the text.


str1 =input("enter string:")
n = int(input("enter number count: "))#typcast

str1 = str1.split()
counts = dict() #emplty dict

for i in str1:
    if i in counts:
        counts[i]+=1
    else:
        counts[i]=1
print(counts)
word_list = []


for key in counts:
    if counts[key]>=n:
        word_list.append(key)
if len(word_list)>0:
    print(word_list)
else:
    print("NA")
















