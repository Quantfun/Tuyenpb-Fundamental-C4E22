while True:
    pwd = input("Enter your passwords ")
    if len(pwd) < 8:
        print("Not long enough")

    elif pwd.isdigit():
        print("Must not contain only numbers")
    elif pwd.isupper():
        print("Must contain lowercase letters")
    elif pwd.islower():
        print("Must contain uppercase letters")
    else:
        print("OK")
        break


