import turtle
def draw_square(size,linecolor):
   color(linecolor)
   for i in range (4):
      forward(size)
      left(90)

from turtle import *

linecolor = input("Your color: ")
size = int(input("your size: "))


draw_square(size,linecolor)
mainloop()

