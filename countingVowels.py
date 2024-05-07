
vowel = ['a','i','o','u','e']
word = "pythonProgramming"
count = 0

for char in word:
    if char in vowel:
        count += 1
print(count)


def countvowels(vowel):
    word = "shrutiApatil"
    count= 0
    for i in vowel:
        if i in word:
            count += 1
    print(f"{count} in shrutiApatil")
vowel = ['a','i','o','u','e']

countvowels(vowel)


def countv(V):
    word = 'codinground'
    ct =0
    for i in V:
        if i in word:
            ct +=1
    print(ct)
V=['a','i','o','u','e']
countv(V)


