from turtle import *

#speed(-1)

shape("classic")
color("green")

for i in range(5):
    if i==1:
        fillcolor("red")

    elif i==2:
        fillcolor("blue")
    elif i==3:
        fillcolor("brown")
    elif i==4:
        fillcolor("yellow")    
    else:
        fillcolor("grey")            
    
    begin_fill()
    for j in range(2):
        left(90)
        forward(100)
        left(90)
        forward(50)
        
    end_fill()
    forward(50)

mainloop()