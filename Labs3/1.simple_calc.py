from random import randint, choice
from calc import eval

def generate_quiz():
    x = randint(0,10)
    y = randint(1,10)
    op = choice(["+","-","*","/"])
    error = randint(-1,1)
    r = eval(x,y,op) + error
    return [x,y,op,r]

x, y, op, r = generate_quiz()

output = "{0} {3} {1} = {2}".format(x,y,r,op)
print(output)
user_anwer = input("(Y/N) ? ").upper()

if r == eval(x,y,op):
    if user_anwer == "Y":
        print("Correct")
    else:
        print("Oops")
else:
    if user_anwer == "Y":
        print("Oops")
    else:
        print("Correct")
