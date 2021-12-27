def waterjug():
    print("water jug problem")
    xc=int(input("enter the x gallon capacity"))
    yc=int(input("enter the y gallon capacity"))
    x=int(input("enter the x value"))
    y=int(input("enter the y value"))
    while True:
        rno=int(input("enter the rule no"))
        if rno==1:
            if x<xc:
                x=xc
            else:
                print("out of capacity")
        elif rno==2:
            if y<yc:
                y=yc
            else:
                print("out of capacity")
        elif rno==3:
            if x>0:
                print("enter capacity")
                d=int(input())
                x=x-d 
            else:
                print("not happening")
        elif rno==4:
            if y>0:
                print("enter capacity")
                d=int(input())
                y=y-d 
            else:
                print("not happening")
        elif rno==5:
            if x>0:
                x=0
            else:
                print("not happening")
        elif rno==6:
            if y>0:
                y=0
            else:
                print("not happening")
        elif rno==7:
            if x+y>=xc and y>0:
                x,y=xc,y-(xc-x)
            else:
                print("not happening")
        elif rno==8:
            if x+y>=yc and x>0:
                x,y=x-(yc-y),yc
            else:
                print("not happening")
        elif rno==9:
            if x+y<=xc and y>0:
                x,y=x+y,0
            else:
                print("not happening")
        elif rno==10:
            if x+y<=yc and x>0:
                x,y=0,x+y
            else:
                print("not happening")
        
        else:
            break;
    print("x:",x,"y:",y)
waterjug()
            

            
            
        
