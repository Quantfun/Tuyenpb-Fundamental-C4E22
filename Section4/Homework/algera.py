numbers = [35, 36, 40, 45]
print("If x = 8, then what is value of 4(x+3) ? ")

n=0
for i in numbers:
    print(n+1,i,sep=". ")
    n +=1

choice = int(input("Your choice: "))
if choice ==3:
    print(":(")
else:
    print("Bingo")
