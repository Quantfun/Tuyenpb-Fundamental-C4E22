from random import *

def generat_quiz():
    x = randint(0,10)
    return [x,0,"@@",12]

def check_answer(x,y,op,result, user_choice):
    print(user_choice)