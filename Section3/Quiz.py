print("Today C4E class is held and there are many female student. Who is the most handsome ? ")
person= ["Kent", "Ivy", "Both", "No body"]
print(*person,sep="\n")
choice  = int(input("What is your answer? "))
while True:
    if choice ==2 :
        print("Correct")
    else:
        print("It is wrong. Plz try it")
    break
