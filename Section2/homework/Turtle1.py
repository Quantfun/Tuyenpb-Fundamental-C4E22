# from turtle import *

# shape("classic")
# color("red")
# speed(-1)

# for i in range(2):
#     right(60)
#     right(120)

# mainloop()

from turtle import *

shape("classic")
color("red")
speed(-1)


for i in range(1):
    for i in range(2):
        left(60)
        forward(100)

    for i in range(1):
        left(120)
        forward(100)
        left(60)
        forward(100)

for i in range(3):
        right(150)
        forward(100)
        left(60)
        forward(100)
        left(120)
        forward(100)
        left(60)
        forward(100)
      
mainloop()
