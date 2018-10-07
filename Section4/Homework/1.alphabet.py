char = ["f","d","a","g","m","a","z","d","d","m","m"]
char.sort()
print(char)
char2 = set(char)
print(list(char2))
for i in char2:
    n= char.count(i)
    print(i,n)