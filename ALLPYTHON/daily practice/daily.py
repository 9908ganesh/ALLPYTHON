'''#break
for i in range(100):
    print(i)
    if i == 23:
        break

for i in range(1):
    for j in range(1):
        for k in range(2):
            print(f"i={i},j={j},k={k}")
             
print("======================================================================")
# even or odd number
number=int(input("enter your number"))
if number%2==0:
    print("{0} is an even number:".format(number))
else:
    print("{0}is an odd number".format(number))

print("======================================================================")
# possitive numbers
number = int(input("enter your number"))
if number >=0:
    print("{0} it is possetive number".format(number))
else:
    print("{0} it is  negetive number".format(number))

# skip some specific values from start to end

for i in range(11):
    if i >=5 and i <= 8:
        continue
    print(i)


for k in range(1,100):
    if k > 20 and k <50:
        continue
    if k > 50 and k <80:
        continue
    print(k)

# swap

g=10
h=30
k=g
g=h
h=k
print(g)

# count digits
num =str(input("enter no:"))
c=len (str(num))
print(c)

#multiplication
t=int(input("enter no:"))
for k in range(1,11):
    print(f"{t} x {k} = {k*t}")
    
# average
    
a=int(input("enter no:"))
b=int(input("enter no:"))
c=int(input("enter no:"))
d=int(input("enter no:"))
e=int(input("enter no:"))
f=int(input("enter no:"))
av=(a+b+c+d+e+f)/5
print(av)

# odd numbers
for o in range(1,100,2):
    print(o)

# even numbers
for e in range (0,101,2):
    print(e)


for k in range(5):
    k= "*"
    for i in range(1):
        i="*"
        for j in range(1):
            j="*"
            print(f"{k} {i} {j}")

for i in range (100,3):
    print(i)

from string import Template
n=input("enter your name : ")
pn=int(input("enter ur phone number :+91"))
ad=input("enter ur address")
tep=Template("my name is $name my phone number is $phonenumb my address is $myaddress ")
strcan=tep.substitute(name=n,phonenumb=pn,myaddress=ad)
print(strcan)
from string import Template
a=str(input("enter ur nm:"))
b=str(input("enter ur last nm:"))
c=int(input("enter ur adher no:"))
d=int(input("enter ur phnm:"))
e=str(input("enter ur vnm:"))
f=str(input("enter ur mnm:"))
g=int(input("enter pincode"))
h=str(input("enter ur nationlity nm"))
oo=Template("my name is $nm and my last name is $lnm my adher number is $ano and my phone number is $pno my villege name is $vnm it is located in $mnm mandal its pin code is $pnc and i am an $con")
inf=oo.substitute(nm=a,lnm=b,ano=c,pno=d,vnm=e,mnm=f,pnc=g,con=h)
print(inf)

import datetime
print(datetime.datetime.now())# showing present time
print("-----------------------------------------------------------------------------")
print(datetime.datetime.weekday(datetime.datetime.now()))# emo emo naake theliyadhu
print("-----------------------------------------------------------------------------")

print(datetime.date.today())#showing only today date
print("-----------------------------------------------------------------------------")
print(datetime.datetime.strptime('2/11/2024', '%d/%m/%Y'))#striptime meance it showing yy-mm-dd
print("-----------------------------------------------------------------------------")

date_string = "25/December/2022"  # it is showing date in string 
print("date_string =", date_string)
print("-----------------------------------------------------------------------------")

date_object = datetime.datetime.strptime(date_string, "%d/%B/%Y")
print("date_object =", date_object)

print("-----------------------------------------------------------------------------")
now = datetime.datetime.now()

t = now.strftime("%H:%M:%S")
print("Time:", t)
print("-----------------------------------------------------------------------------")

a=datetime.datetime.now()
b=a.strftime("%H-%M-%S")
print (b)

class simplecalculator:
    def addition():
        return(a+b)

class shanmukha:
    def __init__(self,f,l,age,address):
        self.first_nm=f
        self.last_nm=l
        self.student_age=age
        self.student_address=address
    def student_detailes(self):
        print(self.first_nm +""+self.last_nm,self.student_age,self.student_address)    
v=shanmukha('gurram','jaya',21,'w_colony')
b=shanmukha('vinay','kumar',25,'c_colony')
c=shanmukha('boji','barath',23,'mr_palli')
d=shanmukha('ram','charan',24,'w_colony')
e=shanmukha('bhanu','swapna',26,'mr_palli')
v.student_detailes()
b.student_detailes()
c.student_detailes()
d.student_detailes()
e.student_detailes()

a=int(input('enter a value :'))
b=int(input('enter b value :'))
if b!=0:
    c=a/b
    print(c)
else:
    try:
        c=a/b
    except:
        print('invalid input')
    finally:
        print('done')

print("testing error handling ")


try:
    a=int(input("enter a value :"))
    b=int(input("enter a denaminator :"))
    c=a/b
    print(c)
except:
    print('dinominator is zero(0)')
finally:
    print("done done")


print("testing the error handling")

try:
    a=int(input("enter a value"))
    b=int(input("enter a denaminator"))
    c=a/b
    print(c)
except:
    print('dinominator is 0')
finally:
    print('done')







print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


list = [-1,-9,-8,-4,-5,-2,2]
for i in list:
    if i<=0:
        print("this is negetive numbers",i)
    else:
        ("it positive numbers")




list = ["apple","banana","orenge"]
print("apple" in list)


#palindrome
v=input("enter a string")
r=v[::-1]
if r==v:
    print("it is palidrome")
else:
    print("it is not a palindrome")'''

list=[4,"ganesh","shaju",6,7,"jay",9]
str_l1=[]
int_l2=[]
for items in list:
    if isinstance (items, str):
        str_l1.append(items)
    if isinstance (items, int):
        int_l2.append(items)
print(str_l1)
print(int_l2)

di=dict(zip(str_l1,int_l2))
print(di)
a=[]
b=[]

for keys in di:
        a.append(keys)
for values in di:
    b.append(values)
c=a+b
print(c)
