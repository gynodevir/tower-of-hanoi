def add():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a+b
    print("sum:",c)

def sub():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a-b
    print("sub:",c)

def mul():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a*b
    print("mul:",c)
def div():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a/b
    print("div:",c)

def flrdiv():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a//b
    print("flrdiv:",c)
def mod():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a%b
    print("mod:",c)
def exp():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    c=a**b
    print("exp:",c)

def condition():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    if a>b:
        print(a)
    else:
        print(b)
def equal():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    if a!=b:
        print("not")
    else:
        print("yes")
def And():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    if a>2 and b>2:
        print("true")
    else:
        print("false")
def Or():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    if a>0 or b>0:
        print("true")
    else:
        print("false")
def Not():
    a=eval(input("enter the first:"))
    b=eval(input("enter the second:"))
    if not(a>0 and b>0):
        print("true")
    else:
        print("false")
def identity():
    x=["apple","banana"]
    y=["apple","banana"]
    z=x 
    print(z is not y)





while True:
    
    ch=int(input())
    if ch==1:
        add()
    elif ch==2:
        sub()
    elif ch==3:
        mul()
    elif ch==4:
        div()
    elif ch==5:
        mod()
    elif ch==6:
        flrdiv()
    elif ch==7:
        exp()
    elif ch==8:
        condition()
    elif ch==9:
        equal()
    elif ch==10:
        And()
    elif ch==11:
        Or()
    elif ch==12:
        Not()
    elif ch==13:
        identity()
    
        
    else:
        break


