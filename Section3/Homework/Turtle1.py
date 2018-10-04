from turtle import *

shape("classic")
speed(-1)

for i in range(3,8,1):
    if i==3:
        color("red")
    
    elif i==4:
        color("blue")
    elif i==5:
        color("brown")
    elif i==6:
        color("yellow")
    else:
        color("grey")

    for j in range(i):    
        forward(100)
        left(360/i)

mainloop()