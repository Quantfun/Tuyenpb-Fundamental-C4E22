def add(x,y):
    print(x+y)
    return r

def eval(x,y,op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    
    return x/y 

# print(eval(9,10,"*"))
