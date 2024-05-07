#consonents means except vowel

def count_consonents(Con):
    word = "count the number of consonents in a string"
    count = 0
    for i in word:
        if i not in Con:
            count +=1
    print(count)
Con = ['a','i','o','u','e', 'A','E','I','O','U']
count_consonents(Con)





vowels =['a','i','o','u','e', 'A','E','I','O','U']
word = 'pythoN'
count = 0

for i in word:
    if i not in vowels:
        count += 1
print(count)









