
def element():
    a=int(input("enter the value to search"))
    list=[1,2,3,4,5]
    if a in list:
        print("element were present in the list")
    else:
        print("element were not present in the list")

def avg():
    a=int(input())
    b=int(input())
    c=int(input())
    sum=a+b+c
    avg=sum/3
    print("sum",sum,"average",avg)
def distance():
    a=int(input("enter the first point"))
    b=int(input("enter the second point"))
    c=a-b
    print(c)
def percentage():
    a=int(input("enter the first subject"))
    b=int(input("enter the second subject"))
    c=int(input("enter the third subject"))
    d=int(input("enter the fourth subject"))
    e=int(input("enter the fifth subject"))
    f=(a+b+c+d+e)/500
    g=f*100
    print("percentage",g)

def replace():
    a=str(input())
   
    a=a.replace("c","k")
    print(a)

def remove(string, i): 
  
    
    a = string[ : i] 
      
    
    b = string[i + 1: ]
      
    
    return a + b
def sol():
    while True:
        print("enter 1 for check element in list")
        print("enter 2 for find averae of three numbers")
        print("enter 3 for distance between two points")
        print("enter 4 for finding the percentage")
        print("enter 5 for replace the string")
        print("enter 6 for remove for string")
        print("enter other than above number to exit")
        ch=int(input())
        if ch==1:
            element()
        elif ch==2:
            avg()
        elif ch==3:
            distance()
        elif ch==4:
            percentage()
        elif ch==5:
            replace()
        elif ch==6:
            a=str(input("enter the string value"))
            i=int(input("enter the position"))
            print(remove(a,i))
        else:
            break
sol()
      

