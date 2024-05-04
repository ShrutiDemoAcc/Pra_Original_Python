
#1 reverse a string
s = "shruti patil"
def reverse_string(s):
    print(s[::-1])
reverse_string(s)


s1 = 'vish'
def rev_str(s1):
    print(s1[::-1])
rev_str(s1)


#1 odd or even number

num = int(input("Enter your number: "))
if (num % 2) == 0:
    print(f"{num} is a even number")
else:
    print(f"{num} is odd number")

#3 given number is positive or negative
def positive_negative():
    number = float(input("Enter your number: "))
    if number > 0:
        print("Positive")
    elif number == 0:
        print("neither + nor -")
    else:
        print("negative number")
positive_negative()

# 3 sum of two number
def sum(x,y):
    print(x+y)
sum(3,7)


#4 prime number
def prime_number():
    number1 = int(input("Enter Your Number: "))
    flag = False
    if number1 >1:
        for i in range(2 , number1):
            if (number1 % i) == 0:
                flag = True
                break
    if flag:
        print("prime number")
    else:
        print("non prime number")
prime_number()

#5 palindrome or not
def is_palindrome(s):
    return s == s[::-1]
string = "radar"
print(is_palindrome(string))      # Output: True

def Palindrome(s):
    return s==s[::-1]
name = 'madam'
print(Palindrome(name))

def P(S):
    return S == S[::-1]
S = 'KANAK'
print(P(S))

def Palindrome_number(Number):
    return str(Number) == str(Number)[::-1]
Number = 121
print(Palindrome_number(Number))


Num_Palindrome = lambda num1:str(num)==str(num)[::-1]
num1 = 12121
print(Num_Palindrome(num1))
print("___")

#6 armstrong number or not

#given strings are anagram
def Anagram(S1 , S2):
    if sorted(S1)==sorted(S2):
        print("yes, its an anagram")
    else:
        print("Not an anagram")

S1 = "vivid"
S2 = "diviv"
Anagram(S1, S2)
print("____")

def Max(a,b):
    if a>b:
        print("Max")
    else:
        print("Not Max")

Max(7,4)
print("_____")

def Minimun_Number(c,d):
    if c<d:
        print("less")
    else:
        print("not less")
Minimun_Number(1,4)

def Max_Three_num(q,w,e):    #same for min number
    if q>w and q>e:
        print(f"{q} is greater")
    elif w>q and w>e:
        print(f"{w} is greater")
    else:
        print(f"{e} is greater")
Max_Three_num(1,2,3)

#factorial number

def Factorial_Num():
    num = int(input("Enter a number: "))
    fact =1
    if num < 0:
        print("Not a factorial number")
    elif num ==0:
        print("factorial of 0 is 1")
    else:
        for i in range(1 , num+1):
            fact = fact*i
        print("The Factorial of ",num ,"is" , fact)
Factorial_Num()

#Fibonacci
terms = int(input("enter a number: "))
n1, n2 = 0,1
count = 0
while count<terms:
    print(n1)
    nth = n1+n2
    n1=n2
    n2=nth
    count+=1

#Pattern
def star_Pattern(n):
    for i in range(0,n):
        for j in range (0 , i+1):
            print('*', end=" ")
        print("\r")
n = 5
star_Pattern(n)
# *
# * *
# * * *
# * * * *
# * * * * *

def star_Pattern2(n):
    k=n-1
    for i in range(0,n):
        for j in range (0,k):
            print(end=" ")
        k=k-1
        for j in range (0,i+1):
            print("4", end=" ")
        print("\r")

star_Pattern2(10)


def num_pattern(n):
    num=1
    for i in range ( 0,n):
        num = 1
        for j in range (0 , i+1):
            print(num , end = " ")
            num = num+1
        print("\r")
num_pattern(10)

def num_pattern1(n):
    num1 = 1
    for i in range (0,n):
        for j in range(0,i+1):
            print(num1 , end = " ")
            num1=num1+1
        print("\r")
num_pattern(4)


#palindrom string
def is_P(Str):
    rever = Str[::-1]
    return Str == rever
Str="MADAM"

print(is_P(Str))


#factorial  Factorial of n = n! = n × (n – 1) × (n – 2)

def large(a,b):
    if a>b:
        print("large")
    else:
        print("small")
large(1,2)

def large_list(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

