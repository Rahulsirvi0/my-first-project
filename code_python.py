
#1 PRINT HELLO WORLD
print("Hello worldoo")

#2 GREATES BW TWO NUMBERS
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

if  a>b:

  print(a,"is greater than",b)

else :
  print(a,"is greater than",b)

#3 GREATES BW TWO NUMBERS  USING A FUNCTION
a=int(input("Enter value of a "))
b=int(input("Enter value of b "))

def greatest(a,b):
  if  a>b:
    print(a,"is greater than",b)
  else :
    print(a,"is greater than",b)

greatest(a,b)

#4 GREATES BW THREE NUMBERS

a=int(input("Enter value of a "))
b=int(input("Enter value of b "))
c=int(input("Enter value of c "))

if  a>b and a>c:

  print(a,"is greateest number")

elif b>c and b>a:
  print(b,"is greatest number")
else :
  print(c,"is greatest number")

#5 GREATES BW THREE NUMBERS USING FUNCTION

a=int(input("Enter value of a "))
b=int(input("Enter value of b "))
c=int(input("Enter value of c "))

def greatest(a,b,c):
  if  a>b and a>c:
    print(a,"is greateest number")
  elif b>c and b>a:
      print(b,"is greatest number")
  else :
       print(c,"is greatest number")


greatest(a,b,c)

#6 TO CHEK THE GIVEN NUMBER IS PRIME OR NOT
n=int(input("Enter value of n to check prime "))
count=0
for i in range (1,n+1):
  if n%i==0 :
    count=count+1

if count==2:
  print(n,"is prime")

else :
  print(n,"is not prime")

#7 TO CHEK THE GIVEN NUMBER IS PRIME OR NOT USING A FUNCTION
n=int(input("Enter value of n to check prime "))
def primecheck(n):
  count=0
  for i in range (1,n+1):
    if n%i==0 :
      count=count+1
  return count

count=primecheck(n)
if count==2:
  print(n,"is prime")

else :
  print(n,"is not prime")

#8 TO PRINT PRIME NUMBERS IN GIVEN RANGE
n=int(input("Enter the range for prime "))
for i in range (2,n+1):
  count=0
  for j in range (1,i+1):
   if i%j==0 :
     count=count+1

  if count==2:
   print(i)

#9 TO PRINT PRIME NUMBERS IN GIVEN RANGE USING FUNCTION
n=int(input("Enter the range for prime "))

def primeprint(n):
  for i in range (2,n+1):
    count=0
    for j in range (1,i+1):
     if i%j==0 :
       count=count+1
    if count==2:
      print(i)

primeprint(n)

#10 TO PRINT EVEN NUMBERS IN GIVEN RANGE
n=int(input("Enter n"))
for i in range (1,n+1):
  if i%2==0 :
    print(i)

#11 TO FIND THE FACTORIAL OF GIVEN NUMBER
fact=1
n=int(input("Enter factber for factorial"))
for i in range(1,n+1):
  fact=fact*i
print(fact)

#12 TO FIND THE SUM OF DIGITS OF GIVEN NUMBER
sum=0
n=n=int(input("Enter number for its digits sum "))
while n!=0:
  digit=n%10
  sum=sum+digit
  n=n//10
print(sum)

#13 TO CHEK THE GIVEN NUMBER IS ARMSTRONG OR NOT

n=int(input("Enter number to check armstrong "))
sum=0
temp=n
while n!=0:
  digit=n%10
  sum=sum+(digit*digit*digit)
  n=n//10
if sum==temp:
  print(temp,"is armstrong")
else :
  print(temp,"is not armstrong")

#14 TO PRINT THE GIVEN ARMSTRONG NUMBERS FROM 1 TO 1000

n=int(input("Enter the range you want armstrongs "))
for i in range (1,n+1):
  sum=0
  temp=i
  while temp!=0:
    digit=temp%10
    sum=sum+(digit*digit*digit)
    temp=temp//10
  if sum==i:
    print(i)

#15 TO CHEK THE GIVEN NUMBER IS PALLINDROM OR NOT
n=int(input("Enter number to check pallindrom "))
rev=0
temp=n
while n!=0:
  digit=n%10
  rev=(rev*10)+digit
  n=n//10
if rev==temp:
  print(temp,"is a pallindrome")
else :
  print(temp,"is not a palindrome")

"""16
PRINT USING CONTINUE
1
2
4
5
"""
i=1
while i<=5:
  if i==3:
    i=i+1
    continue
  print(i)
  i=i+1

"""17
PRINT USING CONTINUE , OR
1
2
5
"""
i=1
while i<=5:
  if i==3 or i==4:
    i=i+1
    continue
  print(i)
  i=i+1

"""18
PRINT USING CONTINUE , OR
1
2
3
5
6
7
9
"""
i=1
while i<=10:
  if i==4 or i==8:
    i=i+1
    continue
  print(i)
  i=i+1

"""19
PRINT USING BREAK
1
2
"""
i=1
while i<=5:
  if i==3 :
    break
  print(i)
  i=i+1

"""20
PRINT
*
**
***
****
*****
"""
n=int(input("Enter the number of rows of star "))
for i in range (1,n+1):
  for j in range (1,i+1):
    print("*",end="")
  print("")

"""21
PRINT
*
**
***
****
*****
"""
n=int(input("Enter the number of rows of star "))
for i in range (n,1):
  for j in range (1,n-1):
    print("*",end="")
  print("")
  i=i-1

#22 FOR LOOP
for i in range (1,5):
  print(i)
  i=i+1

#23 LIST IN PYTHON
studentlist=["rahul","priyanka","nishchay",87,56]
print(studentlist)
print(type(studentlist))

#24 TAKE LIST FROM USER
list1=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  list1.append(a)
print(list1)

#25 TO COUNT THE NUMBER OF EVEN , ODD , ELEMENTS  IN A LIST WITHOUT USING AN INBUILT FUNCTION
list1=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  list1.append(a)
print(list1)
evenlist=[]
oddlist=[]
count=0
even=0
odd=0
for i in list1:
  count=count+1
  if i%2==0:
   evenlist.append(i)
   even=even+1
  else:
    oddlist.append(i)
    odd=odd+1
print("The number of elements in the list =",count)
print(evenlist)
print("The number of even elements in the list =",even)
print(oddlist)
print("The number of odd elements in the list =",odd)

#26 REPLACING 1ST AND 2ND ELEMENT OF THE LIST
namelist=["rahul","amisha","nandu","kritika"]

namelist[1:3]=["choudhary","sumita"]
print(namelist)
print(namelist[-1:])
print(namelist[-3:])
print(namelist[:-3])
print(namelist[:-1])

#27 FUNCTION OF METHOD INSERT,POP,APPEND

namelist=["rahul","amisha","nandu","kritika"]
namelist.insert(1,"viraj")
print(namelist)
namelist.pop()
print(namelist)
namelist.append("viraj")
print(namelist)

# METHOD TO CONNECT OR ADD TWO LIST
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list1.extend(list2)
print(list1)

# METHOD TO CONNECT OR ADD TWO LIST
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
list3=[]
list3=list1+list2
print(list3)

#28 FUNCTION OF CLEAR LIST OPERATION
numlist=[4,6,5,3,7,8,2]
numlist.clear()
print(numlist)

#29 FINDING LARGEST NUMBER FROM THE USER GIVEN LIST
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)
print(userlist)
largest=userlist[0]
for i in userlist:
   if i>largest:
     largest=i
print(largest)

#30 FINDING LARGEST NUMBER FROM THE USER GIVEN LIST USING FUNCTION
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)
print(userlist)
def max(templist):
  largest=templist[0]
  for i in templist:
     if i>largest:
       largest=i
  print(largest)

max(userlist)

#31 REVERSE OF A LIST WITHOUT AN INBUILT FUNCTION
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)
  i=i-1
print(userlist)

def revlist():
  j=0
  for i in range (n-1,n//2,-1):
   temp=userlist[i]
   userlist[i]=userlist[j]
   userlist[j]=temp
   j=j+1
  print(userlist)

revlist()

#32 ADDING ELEMENTS TO TUPLE BY CONVERTING TO LIST AND AGAIN TO TUPLE
tuple1=()
list1=list(tuple1)
n = int(input("Enter the number of elements: "))
for i in range(n):
    a = int(input("Enter number: "))
    list1.append(a)
print(list1)
tuple1=tuple(list1)
print(tuple1)

#33 SOERTING OF A LIST AN INBUILT FUNCTION
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)

print(userlist)
userlist.sort()
print(userlist)

#34 SOERTING OF A LIST WITHOUT AN INBUILT FUNCTION
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)
print(userlist)

def sort(userlist):
  for i in range (0,n):
    for j in range (i+1,n):
      if userlist[i]>userlist[j]:
        temp=userlist[i]
        userlist[i]=userlist[j]
        userlist[j]=temp
  print(userlist)

sort(userlist)

#35 SOERTING IN DECENDING OF A LIST AN INBUILT FUNCTION
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)
print(userlist)
userlist.sort(reverse=True)
print(userlist)

#36 SOERTING  IN DECENDING OF A LIST WITHOUT AN INBUILT FUNCTION
userlist=[]
n=int(input("Enter the number of elements "))
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)

print(userlist)

def sort(userlist):
  for i in range (0,n):
    for j in range (i+1,n):
      if userlist[i]<userlist[j]:
        temp=userlist[i]
        userlist[i]=userlist[j]
        userlist[j]=temp
  print(userlist)

sort(userlist)

#37 OPERATION PERFORMED ON DICTIONARY

mydictionary={
    "NAME":"RAHUL",
    "SURNAME":"CHOUDHARY",
    "AGE":21,
    "GENDER":"MALE",
}
print(mydictionary)
print(mydictionary["NAME"])
print(mydictionary.get("NAME"))
print(mydictionary.keys())
print(mydictionary.values())
print(mydictionary.items())

for i in mydictionary.items():
  print(i)

mydictionary["AGE"]=18
print(mydictionary)

mydictionary.update({"AGE":20})
print(mydictionary)

mydictionary.pop("AGE")
print(mydictionary)

mydictionary["FATHERNAME"]="RAJESH"
print(mydictionary)

for i in mydictionary:
  print(i,end=" ")       #IT FETCHES THE KEYS
  print(mydictionary[i]) #IT FETCHES THE VALE

#38 TO COUNT THE NUMBER OF ELEMENTS IN THE LIST
n=int(input("Enter the number of elements "))
userlist=[]
count=0
for i in range (0,n):
  a=int(input("Enter number "))
  userlist.append(a)
print(userlist)

for i in userlist:
    count=count+1
print("The number of elements in the list is =",count)

#39 OOP CONCEPTS CLASS USING PYTHON
class rahul:
  def __init__(obj,name,age):
    obj.name=name
    obj.age=age

  def show(obj):
    print(obj.name,obj.age)

s1=rahul("Rahul",20)
print(s1.name,s1.age)
s1.show()

#40 CLASS TAKING INPUT FROM USER
class rahul:
  def __init__(obj,name,age):
    obj.name=name
    obj.age=age

  def show(obj):
    print(obj.name,obj.age)

n=input("Enter the name of the student ")
a=int(input("Enter the age of the student "))
s1=rahul(n,a)
print(s1.name,s1.age)
s1.show()

#41 CLEAR OUTPUT AFTER TAKING
from IPython.display import clear_output
n=[]
rollno=[]
for i in range (4):
  n.append(input())
  rollno.append(input())

clear_output()

for i in range (4):
  print(n[i],end=" ")
  print(rollno[i])

#42 SIMPLE TWO CLASSES WITH TWO OBJECTS
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def show (self):
        print(self.name,"age=",self.age)

class student :
    def __init__(self,n,a,m):
        self.name=n
        self.age=a
        self.marks=m
    def show (self):
        print(self.name,"age=",self.age,"got marks =",self.marks)

p1=person("Priyanka",17)
p1.show()
p2=student("Rahul",18,90)
p2.show()

#43 INHERITANCE OF TWO CLASSES
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

class student(person) :
    def __init__(self,n,a,m):
        super().__init__(n,a)
        self.marks=m
    def show (self):
        print(self.name,"age=",self.age,"got marks =",self.marks)

p1=student("Priyanka",17,100)
p1.show()

#44 INHERITANCE OF THREE SINGLE INHERITANCE CLASSES
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

class student(person) :
    def __init__(self,n,a,m):
        super().__init__(n,a)
        self.marks=m
    def show (self):
        print(self.name,"age=",self.age,"got marks =",self.marks)

class CSEstudent(person) :
    def __init__(self,n,a,m):
        super().__init__(n,a)
        self.branch=m
    def display (self):
        print(self.name,"age=",self.age,"is in branch of",self.branch)

p1=student("Priyanka",17,100)
p1.show()
p2=CSEstudent("Rahul",18,"Cyber")
p2.display()

#45 INHERITANCE OF MULTIPLE INHERITANCE CLASSES
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

class student :
    def __init__(self,m):
        self.marks=m

class CSEstudent(person,student) :
    def __init__(self,n,a,m,mood):
        person.__init__(self,n,a)
        student.__init__(self,m)
        self.mood=mood
    def display (self):
        print(self.name,"age=",self.age,"got marks=",self.marks,"so he is in mood of",self.mood)

p2=CSEstudent("Rahul",18,90,"happy")
p2.display()

#46 INHERITANCE OF THREE CLASSES BY MULTILEVEL INHERITANCE
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a

class student(person) :
    def __init__(self,n,a,m):
        super().__init__(n,a)
        self.marks=m
    def show (self):
        print(self.name,"age=",self.age,"got marks =",self.marks)

class CSEstudent(student) :
    def __init__(self,n,a,m,b):
        super().__init__(n,a,m)
        self.branch=b
    def display (self):
        print(self.name,"age=",self.age,"is in branch of",self.branch,"got marks=",self.marks)

p1=student("Priyanka",17,100)
p1.show()
p2=CSEstudent("Rahul",18,90,"Cyber")
p2.display()

#47 INHERITANCE OF THREE CLASSES BY MULTILEVEL INHERITANCE
class person:
    def __init__(self,n,a):
        self.name=n
        self.age=a
    def details (self):
        print(self.name,"age=",self.age)

class student(person) :
    def __init__(self,n,a,m):
        super().__init__(n,a)
        self.marks=m
    def gotmark (self):
        print("got marks =",self.marks)

class CSEstudent(student) :
    def __init__(self,n,a,m,b):
        super().__init__(n,a,m)
        self.branch=b
    def course (self):
        print("is in branch of",self.branch)

p1=CSEstudent("Rahul",18,90,"Cyber")
p1.details()
p1.gotmark()
p1.course()
