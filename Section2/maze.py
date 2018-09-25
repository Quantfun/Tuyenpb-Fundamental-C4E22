# #1. DRAW a maze
# from turtle import *

# shape("turtle")
# speed(-1)
# color("green")

# for i in range(100):
#     foward(2*i)
#     left(90)
    
# mainloop()

# >>>>>>>>>>>>>>>>>>>>>
# # #2. DRAW a circle of turtle

# from turtle import *
# shape("turtle")
# speed(-1)
# color("green")
# # pencolor("white")
# size = 20

# for i in range(30):
#     # stamp()
#     size = size + 3
#     forward(size)
#     left(120)

# mainloop()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#3. DRAW a picture
from turtle import *
speed(-1)
color("yellow","green")
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos())<1:
        break
end_fill()
mainloop()




