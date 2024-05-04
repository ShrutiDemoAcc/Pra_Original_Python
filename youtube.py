#print coomon letter

def common_letter():
   Str = str(input("enter string s1: "))
   Str1 = str(input("enter string s2: "))
   S = set(Str)
   S1 = set(Str1)
   ls = S & S1
   print(ls)
   print(S)
   print(S1)
common_letter()

#count the frequesncy of words in a string
#python is a good language. python is a nice lang.nice to learn.
def freq_words():
    str= input("Enter your string ")  #user input
    ls = str.split()    #split into words and puts into list
    d ={}  #empty dict
    for i in ls:    #i = python
        if i not in d.keys():
            d[i]=0
        d[i]=d[i]+1
    print(d)
freq_words()


#convert 2 list into dict
def list_to_Dict():
    keys=[1,2,3]
    values = ['a','s','f']
    result = dict(zip(keys, values))
    print(result)
list_to_Dict()

#convert dict to tuple
def dict_To_Tuple():
    example_dict = {'a': 0, 'b': 1, 'c': 2}
    for i in example_dict.items():
        print(i)
dict_To_Tuple()

#missing number in array
#summation method
#sum of n natural number
#n*(n+1)/2
def summation():
    a = [1,2,3,5,6,7]
    n =a[-1]
    sum1=0
    total = n*(n+1)//2
    sum1 = sum(a)
    print(total-sum1)
summation()
#XOR method
# A B
# 0 0 0
# 0 b b
# a 0 a
# a a 0
# b b 0

def get_missing_XOR(a):

    n=len(a)
    xor = a[0]
    for i in range(1,n):
        xor = xor^a[i]
    x2=0
    for i in range(1 , n+2):
        x2=x2^i
    print(xor^x2)
a=a = [1,2,3,5,6,7]
get_missing_XOR(a)


#pairs with given sum value of am array
def twosum(arr, target_value):
    arr.sort()
    left = 0
    right = len(arr)-1
    while (left <= right):
        if( arr[left]+arr[right]>target_value):
            right= right-1
        elif(arr[left]+arr[right]<target_value):
            left = left +1
        elif(arr[left]+arr[right]==target_value):
            print("the value is",arr[left] ,"&", arr[right])
            right= right-1
            left = left+1

arr = [5,7,4,3,9,8,19,21]
target_value = 17
twosum(arr,target_value)


#find min diff between two array
#hints=1)sort the elements of array

def min_diff_Array(arr):
    arr.sort()
    size = len(arr)
    min_diff = 999*999
    #comparte
    for i in range(size-1):
        if (arr[i+1]-arr[i]<min_diff):
            min_diff = arr[i+1]-arr[i]
    return min_diff
arr=[5,32,45,4,12,18,25]
print(min_diff_Array(arr))

def max_diff_array(arr1):
    arr1 = sorted(arr1)
    size=len(arr1)
    max_diff =-88*888
    for i in range(size-1):
        if(arr1[i+1]-arr1[i]>max_diff):
            max_diff = arr1[i+1]-arr1[i]
    return max_diff
arr1=[5,32,45,4,12,18,25,99]
print(max_diff_array(arr1))


#length of last word
def last_word(A):
    arr =A.split(' ')
    print(arr)
    last_word1 = arr[-1]
    print(last_word1)
A ="hello shruti"
last_word(A)


# remove duplicate from array
def remove_duplicates_Array(arr):
    n=len(arr)
    if ( n==0 or n==1):
        return arr
    duplicate_Array = 0
    for last_occurance in range(0,n-1):
        if (arr[last_occurance] != arr[last_occurance-1]):
            arr[duplicate_Array]=arr[last_occurance]
            duplicate_Array=duplicate_Array+1
    arr[duplicate_Array]=arr[n-1]
    return arr[0:duplicate_Array+1]

arr=[1,1,2,2,2,3,3,3,4,5,5,6,6,6,7]
print(remove_duplicates_Array(arr))


#index of Anagrams=1)sort

def index_Anagrams(A):
    if (A==None):
        return
    else:
        dict={}
        for i in range(len(A)):
            word=''.join(sorted(A[i]))
            if (word not in dict):
                dict[word]=[i+1]
            else:
                dict[word].append(i+1)
        return dict
A = ["cat","dog", "god" , "act"]
print(index_Anagrams(A))


#remove duplicates in python

arr = [1,8,5,6,8,5,2,3,7,8,5,2,1,4,5,6,6,7,5,5,2,5,5,8]
arr2= set(arr)
print(arr2)

arr3=list(set(arr))
print(arr3)

arr4=[]
for i in arr:
    if ( i not in arr4):
     arr4.append(i)
print(arr4)

rem_dup = lambda arr:set(arr)
print(rem_dup(arr))

#symettric differeance

S1={1,2,3,8}
S2={2,1,3,7}
re_dup= S1.symmetric_difference(S2)
print(re_dup)


#find largest number in an array

arr =[66,88,77,44,11,22,33,99]
def max(arr):
    max=arr[0]
    size =len(arr)
    for i in range(size):
        if (arr[i]>max):
            max=arr[i]
    return max

print(max(arr))

def min(arr1):
    min = arr[0]
    size = len(arr1)
    for i in range(size):
        if (arr1[i]<min):
            min = arr[i]
    return min
arr1 =[66,88,77,44,11,22,33,99]
print(min(arr1))


#amazing substring starts with vowel, it should be substring

def amaze_substring(str1):
    vowel="aeiouAEIOU"
    count = 0
    for i, char in enumerate(str1):
        if char in vowel:
            count+=len(str1)-1
    return count
print(amaze_substring('abrab'))


#extract number in the string and return as a list

sentence = "my name is 123, and your name is 2.34"
num=[]
for word in sentence.split():
    if word.isdigit():
        num.append(word)
print(num)







