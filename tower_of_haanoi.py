def tower(n,a,b,c):
    if n>0:
        tower(n-1,a,c,b)
        print("move disk",n,"from",a,"to ",b)
        tower(n-1,b,a,c)
n=int (input("enter the size number:"))
tower(n,'A','B','C')
