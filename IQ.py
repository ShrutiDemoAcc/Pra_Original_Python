import re
#swap two number
num1 = 1
num2 = 2

temp = num1
num1 = num2
num2 = temp

print(num1 ,"&",num2)

#check for url in a string
#https://www.youtube.com/watch?v=Nk-CJcDZkAc&list=PLUDwpEzHYYLv0iZsTx4dm-v-icoVXRqrz&index=25
str = 'i am a blogger and my profile is https://www.youtube.com/'
url=re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str)
print(url)

#:Find Sub string Presence in a String
string = 'python is easy to learn language, is not it?'
sub_string = 'it'
print(string.find(sub_string))

if (string.find(sub_string)==-1):
    print("not found")
else:
    print("found")


# reverse a sentence/ reverse a string in sentence
str = 'python is easy to learn language'
words = str.split(' ')
words = words[-1::-1]
print(words)
Output_str = ' '.join(words)
print(Output_str)


# palindrome
def is_palindrome(a):
    word = a[::-1]
    if word == a:
        print("yes, palindrome")
    else:
        print("not palindrome")
a='madam'
print(is_palindrome(a))


#print second largest and first largest
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2,8,5,5,8,99]
ls.sort()
print(ls)
print('First largest ',ls[-1])
print('second largest ',ls[-2])

#Find Smallest & Largest Numbers in a List
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2,8,5,5,8,99]
ls.sort()
print(ls[1])
print(ls[-1])

# Multiply All Numbers in the List
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2]
ls1 = 1
for i in ls:
    ls1 = ls1 * i
print(ls1)

# Find Sum of Elements in the List
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2]
ls1 = 0
for i in ls:
    ls1 = ls1 + i
print(ls1)

total = sum(ls)
print(total)

#Count Occurrences of an element in a list
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2]
x=5
count = 0
for i in ls:
    if (i==5):
        count = count+1
print(count)

#How To Clone or Copy a List
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2]
ls1 = ls
print(ls1)
ls2=ls.copy()
print(ls2)
ls3 = ls[:]
print(ls3)

#How To Clear a List
ls=[1,5,8,7,8,9,6,5,8,5,4,1,2,1,2]
ls.clear()
print(ls)

#print number in o=even and odd order
ls = [2,8,7,4,9,5,6,3,2,1]
def odd_even(ls):
    even = []
    odd = []
    for i in ls:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even + odd
print(odd_even(ls))

#  print number in o=even and odd order by list cmprehension



