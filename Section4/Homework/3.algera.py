numbers = [35, 36, 40, 44]
print("If x = 8, then what is value of 4(x+3) ? ")
value = 4*(8+3)
answer = numbers.index(value)
n=0
for i in numbers:
    print(n+1,i,sep=". ")
    n +=1

choice = int(input("Your choice: "))
if choice == answer+1:
    print("Bingo")
else:
    print(":(")
