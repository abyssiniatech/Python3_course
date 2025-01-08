# part one Introduction to python
# print('*' * 5);


# part two Variables
# name='surafel'
# age=32
# sex='M'
# Department='computer science'
# def Info():
#     print(name)
#     print(age)
#     print(sex)
#     print(Department)
# Info()


# datatypes in python
# Python has five standard data types − integers, floating point numbers, strings, lists, and dictionaries. In addition, Python also provides some special data types such as files, frozen sets, and a few more.

# integer=10 
# float=12.4
# string="hello"
# istrue=True
# print(type(istrue))

# is_new=True
# name="surafel mengist"
# age=23
# print(age)


# name=input("enter you name")
# age=input('enter your age')
# print("my name is" + name + "and" + age + "years old" )

# Project one age calculator



# def AgeCalculator():
#     birthYear=int(input('Birth Year:'))
#     age=2024-birthYear
#     print(age)
# AgeCalculator()


# Project two your weight pound kg

# weight=int(input('weight in pound'))
# weightCal=weight * 0.453592
# print(weightCal  )

# string manuplation
# name="Hello world"
# print(name[0:])
# print("are you ready,s")
# print(name[:4])
# print(name[9])

# name='Jenifer'
# print(name[1:-1])

# if statment in python
# number1=12
# number2=12
# if number1 >number2:
#     print("num1")
# elif number1< number2:
#     print(" num2")
# else:
#     print("two numbers are equal")



# numbers
# numbers=[1,3,10,34,45]
# print(numbers[3])




# def Surafel():
#     print("hello")
# Surafel()


# def AreYouready():
#     print("are you ready to learn javascript") 
# AreYouready()

# weight=int(input("enter your weight"))
# height=float(input('enter your height'))
# Bmi=weight/(height * height)
# print(Bmi)


# Is_login=True
# Is_input=True
# if(Is_login and Is_input ):
#     print('congratulation You can Access ')
# else:
#     print("you can not access these website")


# if -else project

# temeparature=int(input('enter temprature'))
# if temeparature < 10:
#     print("it's a cold day")
# if temeparature >30:
#     print("it's a hot day")
# else:
#     print("it's nither hot nor cold")


# nume='surafel'
# if len(nume)<5:
#     print("your name is less than three char")
# elif len(nume)<7:
#     print('your name is b.n 5 and 7')
# else:
#     print('shor or long name'



# Numbers is python
# num1=12
# num2=34
# def Number():
#     if num1>num2:
#         print("num1 is the larger num")
#     else:
#         print("num2 is the largest")
# Number()


# math maniuplation in python

# temprature=int(input('enter the temprature'))
# if temprature < 10:
#     print("cold day")
# elif temprature < 30:
#     print("avargee temprature")
# else:
#     print("Hot")
    
    
#    Logical  or Operator in python

    
# high_income=True
# Good_credit=False
# if(high_income and Good_credit):
#     print("Eligible for loan")
# else:
#     print("you are not Eligable for loan")

    # logical and operator true if and only if both condition is true
    
    # logical or is the type of condition both Logic is at least one condition is  true
    
# Age=18
# Has_Health_Condition=False
# Has_completed_Grade_8=True
# if Age or Has_Health_Condition and Has_completed_Grade_8:
#     print("Eligable to Start Driving License")
# else:
#     print("You Can not Eligable to Start Driving licsence ")

# ******these is the project to evalute the number of character in the string
# name="sur"
# if(len(name))<5:
#     print("your name is less than 3")
# else:
#     print("your name is grater than 5")
    
    
# name="surafel"
# age=32
# Change to uppercase and to lower case to the string
# print(name.upper())
# print(name.lower())
# print(f' my name is {name} and i am {age} years old');
# secreteNum=3
# inc=1
# while inc<5:
#     if(inc==secreteNum):
#         print('you are win the game')
#         inc + 1
# 10/04/2017
# Good Day
# Change lower case to upper case
# name='surafel'
# print(name.upper())


#Secret Number game Project one
# guess_count=0
# guess_limit=3
# secret_num=9
# while guess_count <guess_limit:
#     guess=int(input('Guess:'))
#     guess_count+1
#     if guess ==secret_num:
#         print('you won!')
#         break


# Secret_num=8
# Guess_count=0
# Guess_limit=3
# while Guess_count <Guess_limit:
#     guess=int(input('Guess:'))
#     Guess_count +=1
#     if(guess ==Secret_num):
#         print("you won the game!")
        
        # car game
# start=True
# stop=True
# Quit=True
# if start ==True:
#     print("the car is Start")
# elif stop==True:
#     print("the car is stop")
        
# elif Quit==True:
#      print("quit")
# else:
#      print("idont understand")
    
# car=input('enter::')
# if car =='start':
#     print("the Car is Start driving")
# elif  car =='stop':
#     print("stop the car")
# elif car =='quit':
#     print("stop excute")
# else:
#     print("I don't understand")
  
  
  
  
  
  
    # for loop in Python
# for item in ['surafel','Abel','Nahome']:
#     print(item.upper())  


# run the numbers from one to 10  
# for num in range(10):
#     print(num)



# Print even numbers
# for Odd in range (10):
#     if Odd %2==0:
#         print(Odd) 

# odd numbers in python
# for Num in range(20):
#     if Num %2 != 0:
#         print(Num)


# five star project in python
# number=[5,2,5,2,2]   
# for num in number:
#     print('X' * num)
# list=[1,2,4,7,12,45,678]
# print(max(list))
# print(min(list))

# find the max number of the list
# numbers=[12,34,56,78,98,765];
# max=numbers[0]
# for num in numbers:
#     if num > max:
#         max=num
# print(max)


# 2D list
# Matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(Matrix[1][2])


# list manuplation in python
# Listof_numbers=[1,2,34,56]
# print(Listof_numbers.append(8));
# print(Listof_numbers.remove(8))
# print(Listof_numbers)
# Numbers=[1,23,45,67,2,3,14]
# num2=Numbers
# print(num2.copy())




# remove the duplicate items
# num=[2,2,4,5,4,6,4,6,1] 
# unique=[]
# for number in num:
#     if number not in unique:
#         unique.append(number)
# print(unique)



# name=[12,23,12,23,1,1,23,4,56,4]
# unique_name=[]
# for names in name:
#     if names not in unique_name:
#         unique_name.append(name) 
# print(unique_name)
# num=1
# if num<2:
#         print("the Num is Les than 2")
# elif num<4:
#         print("the given num is between 2 and 4")
# else:
#         print("the num is greater than 4")
# Name=("Abel","Teshome","Abel","Yared")
# Randomnumber=[1002,2,34,56,78]
# print(max(Randomnumber))
    
    # find the largest numbers in python
# Matrix=[
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12,13]
# ]
# print(Matrix[1][1])
# list in python 

# numbers=[1,2,3,4,5]
# numbers.sort()
# numbers.reverse()
# print(numbers)

# list in python




# removes duplicate umber in python
# numbers=[1,2,3,4,5,1,3,4,6,4,2]
# unique=[]
# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)    


# Tupple inpython  #####***
#   A tuple is a collection which is ordered and unchangeable.
# numbers=(1,2,1,3,4,5,6)
# print(numbers)



# dictionary in prython 
# A dictionary in Python is a collection of key-value pairs. The dictionary keys must be unique. The dictionary value may be of any type.
# example
# school={
    
#     "name":"surafel",
#     "email":"sura@gmail.com",
#     "age":30,
# }
# print(school["age"]

# RandomNum=input(':>')
# numbers={
#     "one":"1",
#     "two":"2",
#     "two":"3",
#     "Three":"4",
#     "five":"6",
#     "seven":"7",
#     "eight":"8",
#     "nine":"9",
#     "ten":"10"
# }

# function in python 
# def Hello(a,b):  
#    product= a*b
#    print(product)
# Hello(12,12)
# parameter in functions
# def Introducing(First_name,Last_Name="Abel"):
#     print(f"my name is {First_name}")
#     print(f"my last name is {Last_Name}")
# Introducing("surafel")
# def sum(a,b):
#     print(a+b)
# sum(12,23)
# positional and keyword arguments found inpython
# calculate the square of the number
# def square():
#     inp=int(input("enter the number"))
#     print(inp * inp)
# square()
# def sqaure(num):
#     return num * num
# print(sqaure(5))
# by default in  python the return value is none
# def  hello():
#     print('hello')
# hello()
# hello()
# hello()
# hello()
# these is 
# sum={
#     "name":"surafel",
#     "name":"Nahom",
#     "name":"abel",
# }
# print(sum['name'])
#********* handle errors in python
# try:
#      age=int(input('enter your age > '))
#      income=2000
#      risk=income/age
#      print(f"i'm {risk} years old")
# except ZeroDivisionError:
#     print("age can not be zero")
# except ValueError:
#     print("invalid input try again")
# **** comments in python
# thre are two types of comment those are singlre line comment and multiline comment




# class in python
# class Point:
#     def name():
#         print("my name is surafel") 
#     def age():
#         print('i am 30 years old')
# Name1=Point.name()
# age1=Point.age()




# class in python
# class Hello:
#     def One():
#         print("one")
#     def two():
#         print("two")
# func1=Hello.One()
# func2=Hello.two()

# class Mamal:
#     def move(self):
#         print('Move')
        
#     class Dog(Mamal):
#         def bark(self):
#            print("the dog bark")
     
# dog1=Mamal.Dog()
# dog1.bark




# modules in on python
# print("there are the best")

# import convertor
# convertor.Bmi



# packages in python
# package in python like directory or folders


# Generate random numbers in python
# import random
# for i in range(1):
#     print((random.randint(1,20)))

# def one(one):
#     return one
# print(one("surafel"))



# thre are two file path in python 
# 1 absolute path means go on based on the folder
# 2 relative path




# easy datatype in python
# first_name='surafel'
# Last_name="mengist"
# print(first_name.upper() + Last_name.upper() )
# print(len(first_name))




# try:
#     def Hello():
#         print("Hi")

# except:
#     print("err has Happend")

# Hello()
# def Hello():
#   num =int(input("enter the given numbrer)>"));
#   if  num<3:
#       print("the given number is less than three");
#   elif num<10:
#       print("the given number is between 3 and 10");
      
#   else:
#      print("the given num is big");
# Hello()



# chick the given number from key board and check if the number is  either even or odd number



# def ChickNumber():
#     GivenNum=int(input("enter the given number"));
#     if(GivenNum % 2==0):
#         print("the given number is even :: " , GivenNum)
#     else:
#         print("the given number is odd :: " , GivenNum )
# ChickNumber()




# there different datatypes in python code
# forloop in python and also nice to render list



# driving License Logic
# age=26
# Is_Health=True
# Education=7

# if age>18 and Is_Health and Education>10:
#     print("you can start Driving License")
# else:
#     print(" you Can not Start driving License ")
    
# Age=int(input("enter your age : "));
# if(Age<3):
#     print("you are baby")
# elif Age <17:
#     print("You are teenager")
# elif Age >17 and Age <29:
#     print("you are young ")
# else:
#     print("You are old")
    

# datastructure is the structure of data on the computer and how to store it
    
# the lopps inside loops is called nested list

# render string in for loops
# for list in ('abel','nahome','aster','yared'):
#     print(list)

# these is an example of nested loops
# for name in("abel",'Yared',"Nahome"):
#     for number in range(1):
#      print(name,number)

# user={
#     "name":'surafel',
#     "age":"23",
#     "Addresse":"Addis Ababa "
# }
# run dictionary items in python
# for item in user.values():
#     print(item)
    
    
    # run dictionary keys in python
# for items in user.keys():
#     print(items)
# print(user)
    
# my_list=[1,2,3,4,5,6,7,8,9,10]
# counter=0
# for list in my_list:
#     counter=counter + list
# print(counter)



# find the sum of the following list python
# list_num=[12,34,56,78,34,120,100]
# counter=0
# for list in list_num:
#     counter=counter + list
    
# if counter<100:
#     print("the sum of the number is less than 100")
# elif counter>200 and counter <300:
#     print("the sum of the number is between 200 and 300")
# elif counter>300 and counter < 400:
#     print("the sumof the number is between 300 and 400")
# else:
#     print("the sum the number is greater than 400")

# number=[1,2,3,4,56,57]
# counter =0
# for list in number:
#     counter=counter+list
# print(counter)


# loop and run the number from 0 to 100
# for number in range(0,100):
#     print(number)
# while loops in python
# i=0
# while i <10:
#     if i%2!=0:
#      print(i)
#     i=i+1
    

# numbers=[1,2,3]
# for item in  numbers:
#     print(item)
    
    
    # in while loop
# i=0
# while  i<len(numbers):
#     print(numbers[i])
#     i=i+1
    
    
# based on the condion we can use either for loop and while loops but for loops is best as compare with the two
#    generate greeting in python

# while True: 
#  greet=input(": ")
#  if greet==greet:
#     print("Hello " + greet)
#     if greet=='by':
#       break
         

# andre amazing tutorials start at chapter for pa

# name=input("enter your naame")
# age=int(input('enter your age') )
# sex=input("enter your sex")
# grade=input('enter your grade lavel')

# def Student():
#     print(f"my name is {name} {age} {sex} {grade}")
    
# Student()




# looping statment inpython
# for number in range(10):
#     if number ==4:
#         break
#     print(number)


# i=0
# while i<5:
#     print(i)
#     i=i+1


# switch statment in python
# day=input("inter day")
# if day=='monday':
#     print("the day is Monday")
# elif day=="teusday":
#     print("The day is teusday")
# elif day=='wednesday':
#     print('the day is wedensday')
# elif day=="thirsday":
#     print("The day is thirsday")
# elif day=="friday":
#     print(" the day is friday")
# else:
#     print("the weekend day ")
    
        
# dictionary in python

# School={
#     "Name":"surafel",
#     "age":"23",
#     "Addrese":"Addis ababa",
#     "email":"sura2015@gmail.com"
# }
# print(School.values())
    
# print('GUI in python')
# Picture=[
#     [0,0,0,0,0],
#     [0,0,1,0,0],
#     [0,0,0,1,0],
#     [0,0,0,1,0]
# ]
# for image in Picture:
#     for pixel in image:
#         if(pixel==1):
#             print("*",end='')
#         else:
#           print("",end='')
#     print("")



# python is the best programming langudge
# def Hello():
#     print("surafel")
# Hello()

# return keyword in python is the best keyword return diffrent variable values and alson it is the best
# example
# def Sum(num1,num2):
#     return num1+num2
# print(Sum(12,34))


# the next example of return keyword

# def sum(num1,num2):
#     return num1+num2
# total=sum(23,22)
# print(total+10)

# def function1(num1,num2):
#     def function2(num1,num2):
#         return num1+num2
#     sum2=function2(23,45)
#     print(sum2)
# sum=function1(12,12)
# print(sum)

# finally return keyword in python nice to return nested functions just like the above the examples



# duplicate letters in pthon
# letters=['a','b','c','d','e','f','a','d','g','a']
# Duplicat_letters=[]
# for values in letters:
#     if letters.count(values)>1:
#         Duplicat_letters.append(values)
# print(Duplicat_letters)

# $$$$$$$$$Project 1
# run and excute the duplicate list in the following list and also excutes nest

# list1=[1,2,3,4,5,6,1,3,4,2,4]
# duplicate=[]
# for value in list1:
#     if list1.count(value)>1:
#         duplicate.append(value)
# print(duplicate)

# %%%%%%%% Project 2
# the second Challenges are find the non duplicate list and excute it
# list1=[1,2,3,4,5,6,1,3,4,2,4]
# duplicate=[]
# for val in list1:
#     if list1.count(val)<=1:
#         duplicate.append(val)
# print(duplicate)

# happy=''
# sad=''
# if happy:
#     print('iam happy 😁')
# else:
#     print('i am 😢')


# imogi=input('enter emoji')
# if imogi:
#     print("Happy")
# else:
#     print("i am sad")
# def hello(name,age,sex,emoji='😂'):
#     return name,age,sex,emoji
# print(hello("surafel",23,'M'))


# name='surafel'
# print(name.capitalize())



# ***priject 3
# find and run the given number is either even or odd to check it the folloeing logics
# num=int(input('enter num ::'))
# def is_odd_or_even():
#     if num %2==0:
#         print("the number is even")
#     else:
#         print("the num is odd")
# is_odd_or_even()


# print("Thank you very much about react js")


# print("Hello ,World")


# function scope meas what variables run the given functions access it 
# global scope
# function scope
# age=12
# def one(num):
#     return num
# print(one(12 + age))

# name=input("enter your name :")
# def surafel():
#     if name=="surafel":
#         print("you are surafel")
#     else:
#         print("you are not surafel")
# surafel()    



# print("After six month i am thew best programmer around the world")

# print("i am the software engineer")


# def Hello(e):
#     return e
# output=Hello("Hello")
# print(output)




# getring input from the users
# name=input("enter your name")
# age=int(input("enter your age"))
# def Info():
#     if name=="surafel" and age<30:
# #         print("you are good")
#     else:
#         print('you are not correct')
# Info()





# word replacement exercise

# list in python
# list1=[1,2,3,4,5,6]
# name=['abel','yared' ,"surafel"];
# print(name[2][0]) these code is used to run the second index array and also the first character of that array




# run the countries based of the 
countries=["Ethiopia","Kenya","Uganda","Nigeria"]
for countries in range:
    print(countries)















