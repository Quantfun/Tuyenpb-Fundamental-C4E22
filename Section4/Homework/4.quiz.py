#Question 1
numbers = [35, 36, 40, 44]
print("If x = 8, then what is value of 4(x+3) ? ")
value = 4*(8+3)
answer = numbers.index(value)
n=0
for i in numbers:
    print(n+1,i,sep=". ")
    n +=1

choice = int(input("Your choice: "))
answers1 = choice == answer+1
if answers1 == True:
    print("Bingo")
else:
    print(":(")

#Question 2
numbers2 = [55, 65, 75, 85]
numbers3 = [49, 81, 72, 66, 52]
print("Jack scored these mark in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ? ")
value = sum(numbers3)/len(numbers3)
# print(value)
# answer = numbers.index(value)
n=0
for i in numbers2:
    print(n+1,"Around ",i,sep=". ")
    n +=1

choice = int(input("Your choice: "))
answers2 = choice == 2
if answers2 == True:
    print("Bingo")
else:
    print(":(")
result = [str(answers1), str(answers2)]
r = result.count("True")
print("You correctly anwser",r,"out of 2 questions")