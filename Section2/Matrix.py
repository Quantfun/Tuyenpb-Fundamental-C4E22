#MATRIX with side from 1 to n
# n = int(input("your maxtrix sides: "))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i*j," ",end="")
#     print()
       

#MATRIX with side from 1 & 0
n = int(input("your matrix side: "))
if n % 2 == 0:
    for i in range(n//2):
        for j in range(n//2):
            print(1," ",end="")
            print(0," ",end="")
        print()
        for j in range(n//2):
            print(0," ",end="")
            print(1," ",end="")
        print()

else:
    for i in range(n//2):
        for j in range(n//2):
            print(1," ",end="")
            print(0," ",end="")
        print(1)
        for j in range(n//2):
            print(0," ",end="")
            print(1," ",end="")
        print(0)