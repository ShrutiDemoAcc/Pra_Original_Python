# #1) Variables and strings
# #variables- is like a container where you can store value in it.
# #String- string is a series of characters . string is surrounded by " or ' quotes.
# #concatanate - is nothing but combining strings, tuple. we can use + sign
variable_Example = 10
variable_Example1 = 20
print("string", variable_Example)
print(type(variable_Example))
concatenation = variable_Example + variable_Example1
print(concatenation)
#
# #2 lists
# #List is mutable data type in python which use [] brackets to use.
# #generally it takes large memory and kind of slower as compared to tuple.
# #we can store many types of data in list.we can access elements using index or loop.

list1 = [1,2,3,4,'d','e','e','t']
print(list1)
print(list1[2])   #index number
print(list1[-1])     #print index number
for list2 in list1:   # for loop
    print(list2)
list1.append('shruti')    # add element
list1.append('vish')
print(list1)

#numerical list
list_Num = []
for x in range(1,5):
    print(x*5)
#
# #list comprehension
# #list_Comre = [expression for an item iterable if conditional]
# #example= [x ** x for x in range (1,11)]
list_Comre = [x / x for x in range (1,4)]
print(list_Comre)
#
# #slicing a list
# # syntax = obj_str[ start : end : step ]
# # example = [ 1 : 4 : -1 ]
syntax = ['s', 'd', 2,4 , 's', 'd', 2, 4]
syntax1 = syntax[4:-1]
print(syntax1)
#
# #3 Tuple- tuple is iimutable is nature denoted by () brackets.it is faster it consumes less memory.
year = (1997,1998,1999,2200)
print(year)
#
# #4 if statements
# # is statements is used to to test for particular conditions.
# # Conditional tests
# # equals x == 42
# # not equal x != 42
# # greater than x > 42
# #  or equal to x >= 42
# # less than x < 42
# #  or equal to x <= 42
age = int(input("Enter Your Age: "))
#1
if age >= 18:
    print("you can vote")
else:
    print("You can not vote")
#2 if-elif-else

if age < 18:
    print('You are a teen ager')
elif age > 18 and age < 25:
    print("You are an adult")
elif age > 25 and age <50:
    print (" You are senior")
else:
    print("You are not elegible due to higher age above 50")

#5 Dict = Dict strore connection between peices of information. each item in a dict is key value pair.
example_dict = {'a' : 0, 'b' : 1, 'c' : 2}
print(example_dict['a'])   #print value
example_dict['d'] = 3   #add
print(example_dict)
#looping whole
for alpha, num in example_dict.items():
    print(alpha, str(num))
    print(type(str(num)))
#looping keys
for k in example_dict.keys():
    print(k)
#looping values
for v in example_dict.values():
    print(v)


# #6 user input - progrm can prompt user input, in string format

name = input("Enter your name: ")
# #number = int(input("Enter your age "))

# #7 while loop
# #a while loop repeats a block of code as long as certain condition is true

while_loop = 1
while while_loop < 5:
    print(while_loop)
    while_loop +=1

# #Letting the user choose when to quit
msg = ''
while msg != 'quit':
 msg = input("What's your message? ")
 print(msg)

# # 8 functions
# #functions are name block of code . designed to do one specific job,
# #informatipn passed to function is an argument
# #informatipn received by function is an parameter
# #simple ex 1-
def shruti():
    print("my name is shruti")
shruti()

# #simple ex 2
def shruti1(username):
    print("hello, good morning" + " " +username)
shruti1('shruti')

# #exapme 3
def pizza(topping = 'bacon'):
    print("hello " + "your pizza topping is " + topping)
pizza('paneer')
pizza()

# # ex 4- returning a value
def add(x,y):
    return x+y
sum = add(5,5)
print(sum)

# #class
# #class is a blueprint for creating a object.it defines the behaviour of an object.
# #information of class is stored in attributes
# #functions of class are called as methods
#
class dog():
    def color(self):
        print("white")
    def breed(self, username):
        print("husky" ,username )
    def Tail(self , one = 'short', two = 'mid'):
        print("long")
# DOG = dog()
# print(DOG.color() + DOG.breed('simba') + DOG.Tail()+DOG.Tail('c')+DOG.Tail('d'))
# DOG.dog.Tail()


#inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.

class AA():
    def A(self):
        print("y")

class BB(AA):
    def B(self):
        print("x")
obj = AA()
obj.A()
obj1=BB()
obj1.B()


#working with files
# file = f'C:\Users\shrut\OneDrive\Desktop\LMP.untitled.txt'
# with open (file) as file1:
#     lines = file1.readlines()
# for line in lines:
#     print(line)

# exceptions
# Exception helps us to respond appropriately to the errors that are
#likely to occur.
#try - place the code might cause an error
#exception- code that should run inresponse to error
#else-run only if the try block was successful  goes i else block

Promt= "how many tickts you need?"
num_Tckt= int(input(Promt))
try:
    num_Tckt = int(num_Tckt)
except ValueError:
    print("please try again.")
else:
    print("You are ready to go..")

#list-
user = [1,2,3,5,1,8,5,6,9,7,2,0,1,4,5,8,5,2]
user1 = user[0]
print(user1)
user[0] = 'a'
print(user)
user.append('shruti')
print(user)
user.insert(5 , 'patil')
print(user)
del user [1]    #remove by index number
print(user)
user.remove('patil')   #remove by value
print(user)
user.pop()            #last elemet
print(user)
user.pop(0)                # by index
print(user)
user2 = len(user)      #length
print(user2)
min1 = min(user)
print(min1)
max1 = max(user)
print(max1)

user3 = user[-3:]      # slicing
print(user3)
user_copy = user[:]    # copy list
print(user_copy)
print('h')


#he sort() method changes the order of a list permanently.
# The sorted() function returns a copy of the list, leaving the
# original list unchanged. You can sort the items in a list in
# alphabetical order, or reverse alphabetical order. You can
# also reverse the original order of the list. Keep in mind that
# lowercase and uppercase letters may affect the sort order
print(sorted(user))
print(sorted(user , reverse = False))
print(user.reverse())

#looping through list
for u in user:
    print(u)


#Range-it is a function to work with a set of numbers efficietly
#starts by 0 and stopts 1 number below the number pass to it.
#we can use list to genarete large list of numbers
for i in range(0,100):
    print(i)

# List COmpre
list1 = [ x+x for x in range(1,11)]
print(list1)

names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = []
for name in names:
    upper_names.append(name.upper())
print(upper_names)

names = ['kai', 'abe', 'ada', 'gus', 'zoe']
upper_names = [name.upper() for name in names]
print(upper_names)

#tuple-A tuple is like a list, except you can't change the values in a
# tuple once it's defined. Tuples are good for storing
# information that shouldn't be changed throughout the life of
# a program. Tuples are designated by parentheses instead
# of square brackets. (You can overwrite an entire tuple, but
# you can't change the individual elements in a tuple.)

T = (2,4,6,8,10,12,14,16,18,20)
for T1 in T:   #looping on tuple
    print(T1)

T = (3,6,9,12,15,18,21,24,27,30)
for T2 in T:
    print(T2)


#Dict-COnnect pieces of related info.
# Each piece of information in a
# dictionary is stored as a key-value pair. When you
# provide a key, Python returns the value associated
# with that key. You can loop through all the key-value
# pairs, all the keys, or all the values.

Dic = {'userA': 'Shruti', 'userB':'patil', 'userC':'vishwesh'}
#u can also use the get() method, which returns None
#instead of an error if the key doesn't exist.
print(Dic['userA'])   #get value by key
Dic1 = Dic.get('userB')    # get value by get() method
print(Dic1)
Dic['userD'] = 'Python'           #Adding a key-value pair
Dic['userE'] = 'C#'
print(Dic)
Dic['userD'] ='JAVA'    #Modifying values in a dictionar
print(Dic)
del Dic['userE']      #Deleting a key-value pair
print(Dic)

#ou can loop through a dictionary in three ways: you can
# loop through all the key-value pairs, all the keys, or all the
# values.
# A dictionary only tracks the connections between keys
# and values; it doesn't track the order of items in the
# dictionary. If you want to process the information in order,
# you can sort the keys in your loop.
for user, name in Dic.items():   #loop all
    print(user + ":" +name)

for user in Dic.keys():     # loop keys
    print(user)

for name in Dic.values():    #loop values
    print(name)

for name in sorted(Dic.values()):  # keys n values in order
    print(name)

length_Dic = len(Dic)     #Length
print(length_Dic)

#Nesting - A list of dict
#t's sometimes useful to store a set of dictionaries in a list;
#this is called nesting.
# Start with an empty list.
users = []
# Make a new user, and add them to the list.
new_user = {
 'last': 'fermi',
 'first': 'enrico',
 'username': 'efermi',
 }
users.append(new_user)
# Make another new user, and add them as well.
new_user = {
 'last': 'curie',
 'first': 'marie',
 'username': 'mcurie',
 }
users.append(new_user)
# Show all information about each user.
for user_dict in users:
 for k, v in user_dict.items():
    print(k + ": " + v)
 print("\n")


#Testing if a value is not in a list
Banned_user = ['ana', 'bela', 'martin', 'justin']
user = ' shruti'

if user not in Banned_user:
    print("You all are in")


def shruti():
    print("Say....hello")
shruti()

def shruti1(message):   #Passing a single argumen
    print(message)
shruti1('hello, everyone')

def cat(color, breed):    #Using positional /keyword arguments
    print('Cat colour is ' + color)
    print('Cat breed is ' + breed)

cat('white', 'husky')

def cat(color, breed):
    print('Cat colour is ' + color)
    print('Cat breed is ' + breed)
cat(color = 'white', breed='husky')


#Using a default value
def describe_pet(name, animal='dog'):
 """Display information about a pet."""
 print("\nI have a " + animal + ".")
 print("Its name is " + name + ".")
describe_pet('harry', 'hamster')
describe_pet('willie')

def num(first, last):   #Returning a single value
    full_name = first + ' ' + last
    return full_name.title()
M = num('shruti' , 'patil')
print(M)

def M(first, last):   #Returning a dictionary
    person= {'s':1, 'd':2}
    return person
M1=M('selena', 'gomez')
print(M1)

def build_person(first, last, age=None):  #Returning a dictionary with optional values
 """Return a dictionary of information
 about a person.
 """
 person = {'first': first, 'last': last}
 if age:
    person['age'] = age
 return person
musician = build_person('jimi', 'hendrix', 27)
print(musician)
musician = build_person('janis', 'joplin')
print(musician)


def greet_users(names):
 """Print a simple greeting to everyone."""
 for name in names:
    msg = "Hello, " + name + "!"
 print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)



def make_pizza(size, *toppings):
    """make a pizza"""
    print("\nmaking a " + size + " pizza")
    print("toppings:")
    for topping in toppings:
        print("-" + topping)

make_pizza('small','peperoni')
make_pizza('mid','panner', 'pasta', 'mushrooms')
make_pizza('large', 'originaos', 'cheeze')



#Modules-you can store your functions in a separate file called a
# module, and then import the functions you need into the file
# containing your main program. This allows for cleaner
# program files. (Make sure your module is stored in the
# same directory as your main program.)







