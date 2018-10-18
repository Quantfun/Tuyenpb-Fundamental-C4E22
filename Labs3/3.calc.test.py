from calc import eval,add
x = int(input("x="))
y = int(input("y="))
op = input("Op (+,-,*,/):")

r= eval(x,y,op)

print(x,op,y,"=",r)