'''
1) Python : 
            Python is a high-level,general purpose programming language

2) Module :
            1) built-in module  2) External module

3) Variable :
            it is container that are storing data value
4) Data types :
              1) integer 2)float 3)string 4)boolean 5)None

Numeric : integer,float,complex Number
Boolean,
Set,
Squence Type : String,List,Tuple,range
maping : dictionary
'''
'''
a=10
b=10.5
c="gopal"
d=True
e=None
print(type(a))  # integer
print(type(b))  # float
print(type(c))  # string
print(type(d))  # boolean
print(type(e))  # None
'''
# userInput 
''''
a=input("Enter The Number")
print(a)'''

#  Escap squence 
'''
\n : new line
\t : space
\' : single quote
\b : back space
'''
'''
name="gopal\n\tgohel \'     umeshbhai'"
print(name)

newName="Gopal \"Gohel\""
print(newName)
'''
''' 
#Type Casting : it is used to convert one data type to anthore data type.
# int(),str(),float()

a="10"
print(type(a))
b=int(a)
print(type(b))
'''

#  String :  String is immutable data type in python and it is squence of character
'''
name="gopal"
print(len(name))  # find the length
print(name[0:3])  # sliceing
print(name[1])
print(name[1:])
'''
# String function
'''
name= "gopal"
print(name.endswith("pal")) # ans True it is no match so it is give the false
print(name.startswith("go")) # ans True
print(name.capitalize())   # first latter capital
print(name.upper())   # whole word upperCase
print(name.lower())   # whole word lowerCase
print(name.find("op"))  # find the word  ans: 1
print(name.replace("gopal","jaynit"))  # replace the string
'''
'''
name=input("Enter The Name :")
print("Good Morinig"+" "+name)
print(f"Good Afternoon {name}")
'''


# List is changeable ,meaning that we can change,add and remove items in a list after it has been created.

'''
list=["python","java",1,2,True]
list[0]="vishal"
print(len(list)) # given the length of list
list.append(101) # add item to the list at a last
list.pop(2)      # delete a particular item in the list
list.insert(0,"JAVASCRIPT")   # insert the value to the particular index
list.remove("python")         # remove the item to the specific item
#list.clear() # clear is used to delelte a all element
list.copy() # copy the list

list.count(1)
print(list)
list =["gopal","jay"]
list[0]="jaynit"
print(list)
'''
'''
number=[1,32,23,4,5]
number.reverse()
number.sort()
print(number)
'''



# Tuples : Tuples are immutable data types,it is allow duplicates value
'''
thisTuple=("apple","banana","cherry","apple")
print(type(thisTuple))  # it is give the type of data ans. tuple
print(len(thisTuple))   # it is give the length of tuple. 
number=(1,2,3,4,5,6,7,7,333)
x=number.index(6)        # it is give the  index number of 6.
y=number.count(7)         # it is give the how many type of 7.
print("This is count ",y)
print(x)
print(thisTuple)
'''
# Dicitionary : it is a collection of key value pair. it is changable.
# it is unordered and can't contain duplicate key
'''
mark={
 "harry":101,
 "shubham":102
}
'''
#print(mark["harry"])
#print(type(mark))
#print(mark.items())
#print(mark.keys())
#print(mark.values())
#mark.update({"harry":99})
#print(mark.get("shubham"))
#print(mark)

# Set : it is colleaction of non-repetive elements
# it is unodered

# d={} empty dictionary
#set={1,2}  this is set data type
#print(type(set))
'''
e=set()
print(type(e))   # type set
set={1,2,3,45,5,5}  # repet Number is not allow {5,5,5} only one time print 5
#set.add(10)    # it is used to add the number ending point.
#set.remove(1)  # it is used to remove item in particular number
#set.clear()    # whole set are clear
print(set)
'''
'''
s1={1,45,6}
s2={7,8,1,78}
print(s1.union(s2)) # 1 display only one time 
print(s1.intersection(s2)) # intersection is used to display a comman value
'''

'''
s=set()
n=input("Enter")
s.add(int(n))
n=input("Enter")
s.add(int(n))
n=input("Enter")
s.add(int(n))
n=input("Enter")
s.add(int(n))
print(s)
'''
# enter the name and language in user input
'''
dic={}
n=input("Enter")
la=input("Enter")
dic.update({n:la})
print(dic)
'''

# conditional statement
'''
number=int(input("Enter The Number :"))

if(number>50):
    print(f"Number {number} is grater than 50")
elif(number > 40):
    print(f"Number {number} is grater than 40")
elif(number < 20):
    print(f"Number {number} is less than 20")
    
else:
    print(f"Number {number} is Not grater Than 50")
'''
# Write a Program find larges number 

'''
a1=int(input("Enter The Number 1:"))
a2=int(input("Enter The Number 1:"))
a3=int(input("Enter The Number 1:"))
a4=int(input("Enter The Number 1:"))

if(a1>a2 and a1>a3 and a1>a3):
    print(f"a1 is largest number",a1)
'''
# write a progrm to check the percentge of 40 up then pass and 40 down then fail

'''

mark1=int(input("Enter The Mark1 :"))
mark2=int(input("Enter The Mark2 :"))
mark3=int(input("Enter The Mark3 :"))


total_percantage=(mark1+mark2+mark3)*100/300
if(total_percantage>=40 and mark1>=33 and mark1):
    print("You are pass",total_percantage)
else:
    print("you are fail",total_percantage)
    '''
# There are two types of loop
# 1) for loop 2) while loop
# for loop
'''
for i in range(1,6):
    print(i)
# while loop
i=1
while(i<6):
    print(i)
    i +=1
'''
'''
list = ["java","python","javaScript"]
i=0
while(i<len(list)):
    print(list[i])
    i +=1
'''

'''
list =[1,2,3]
for i in list:
    print(i)

string="gopal"
for i in string:
    print(i)
'''
# break
''''
for i in range(1,15):
    if(i==10):
        break
    print(i)'''

# continue
'''
for i in range(0,15):
    if(i==3):
        continue
    print(i)
'''

# pass is null statement in python
'''
for i in range(100):
    pass
i=0
while(i < 4):
    print(i)
    i +=1
 '''

# write a programe using for loop multiplie any number to Table print
'''
n=int(input("Enter The Number :"))

for i in range(1,11):
    print(f"{n}X{i} = {n*i}")
'''
'''
n=int(input("Enter The Number :"))
i=1
while(i<11):
    print(n*i)
    i +=1
'''
# write a program to find the J name in the list
'''

list =["Jay","Parth","Jaynit","vishal"]

for name in list:
    if(name.startswith("J")):
        print(f"Hello {name}")
'''

# find number prime or not
'''
n= int(input("Enter The Number "))

for i in range(2,n):
    if( n % i ==0):
        print("Not a Prime Number")
        break
else:
    print("Prime Number")
'''

# write a program sum of natural number
# Enter the 5 Number = 1+2+3+4+5= 15 (ANS:15)
'''

n= int(input("Enter The Number "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i +=1
print(sum)
'''


# Write a program factorial of natural numer
# 5 = 5X4X3X2X1
'''
n = int(input("Enter The Number"))
product=1
for i in range(1,n+1):
    product =product *i
print(product)
'''
'''
n= int(input("Enter The Number :"))
for i in range(1,11):
    print(f"{n} X {11-i} ={n*(11-i)}")
'''
'''

a=5
b=10.5
print(f"Variable : A ")
print(f"Type : {type(a)}")
print(f"Address {id(a)}")
print(f"Value : {a}")
'''

# write a program to calucalte  a area of a circle
# formula  math.pi * radius * radius
'''
import math
def cal(redius):
    return math.pi * redius * redius
redius=float(input("Enter"))
area=cal(redius)
print(area)
'''

# area of room
# formula length * width
# return method
'''
def room(length,width):
    return length * width
    
length=int(input("Enter The Num 1"))
width = int(input("Enter The Num 2"))

print(room(length,width))
'''

# print the without return method
'''
def room(length,width):
    area=length * width
    print(area)
    
length=int(input("Enter The Num 1"))
width = int(input("Enter The Num 2"))

room(length,width)
'''
# q=3
# i=567
# p=49.95
# myOrder="I want{} piece of item {} for {}dollar "
# print(myOrder.format(3,567,49.95))


# function in python
# it is a group of statement performing a specific task
# There are Two types of function : 1) built in function 2) user define function
'''
def average():
    a=int(input("Enter 1 : "))
    b=int(input("Enter 2: "))
    c=int(input("Enter 3 : "))
    avg=(a+b+c)/3
    print(avg)
average()
'''
# parameter function
'''
def goodDay(name,ending):
    print("good day ,"+ name)
    print(ending)
goodDay("Harry","thank you")
goodDay("gopal","thanks")
'''

# return function

'''
def sum(a,b):
    add = a+b
    return add
a1=sum(10,20)
print(a1)
'''

# Default argument function
'''
def  goodDay(name,ending="thank you"):
    print(name)
    print(ending)
goodDay("gopal")
'''


# recursion function

# factorial formula n * factorial(n-1)

'''
factorial(0)=1
factorial(1)=1
factorial(2)=2 X 1
factorial(3)=3 X 2 X 1
factorial(4)=4 X 3 X 2 X 1
factorial(5)=5 X 4 X 3 X 2 X1

factorial(n)= n X n-1 X ... 3 X 2 X 1
factorial(n) = n X factorial(n-1)
'''
'''
def factorial(n):
    if(n==0 or n==1):
        return 1
    return n * factorial(n-1)
n = int(input("Enter The Number "))
print(factorial(n))
'''

# write a program using funcion to find the greatest of three number


'''
def gretest(a,b,c):
    if(a>b and a>c):
        print(a)
    if(b>a and b>c):
        print(b)
    if(c>a and c>b):
        print(c)
a=int(input("Enter"))
b=int(input("Enter"))
c=int(input("Enter"))
gretest(a,b,c)
'''

# celsisus to farhenait

# formula: c/5 = 5*(f-32)/9
'''
def cel(f):
    c =round((f-32)*5/9,2)
    print(c)
f= int(input("Enter The Number"))
cel(f)
'''

# sum of natural number using recurison
# formula sum(n) = sum(n-1) + n
'''
1 = 1
2 = 1 + 2
3 = 1 + 2 + 3
4 = 1 + 2 + 3 + 4
n = 1 + 2 + 3 + ... n-1 + n

'''
'''
def sum(n):
    if( n == 1):
        return 1
    return  n + sum(n-1)
print(sum(4))
'''

'''
def pattern(n):
    if( n == 0):
        return 1
    print("*" * n)
    pattern(n-1)
pattern(5)
'''

