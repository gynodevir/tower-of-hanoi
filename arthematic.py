def add():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a+b
    print("sum:",c)

def sub():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a-b
    print("sub:",c)

def mul():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a*b
    print("mul:",c)
def div():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a/b
    print("div:",c)

def flrdiv():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a//b
    print("flrdiv:",c)
def mod():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a%b
    print("mod:",c)
def exp():
    a=int(input("enter the first"))
    b=int(input("enter the second"))
    c=a**b
    print("exp:",c)

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
    else:
        break


