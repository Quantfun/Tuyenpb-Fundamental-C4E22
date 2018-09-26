
n = int(input("type your number: "))

f = 1

for i in range (n,0,-1):
    f = f * i

print("factorial of ",n," is: ",f)