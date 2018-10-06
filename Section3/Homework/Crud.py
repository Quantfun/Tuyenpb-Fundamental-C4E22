items = ["T-shirt", "Sweater"]
select = input("Welcome to our shop, what do you want (C, R, U, D) ? ")

if select =="R":
    print("Our items: ",*items,sep=", ")

elif select =="C":
    info = input("Enter new item: ")
    items.append(info)
    print("Our items: ",*items,sep=", ")

elif select =="U":
    items.append("Jeans")
    info = int(input("Update position ? "))
    new = input("New item: ")
    items[info-1] = new
    print("Our items: ",*items,sep=", ")
elif select =="D":
 
    info = int(input("Delete position ? "))
    items[info-2]= "Skirt"
    print("Our items: ",*items,sep=", ")






##Replace
# items[2] = "Com trang"
# print(*items, " | ")

# #Update
# position = int(input("Where to change ? "))
# update = input("Change to what ? ")
# items[position - 1] = update
# print(*items, sep=" | ")

# #Delete
# i = input("What to detete ")
# if i.isdigit():
#     position = int(i)
#     items.pop(position-1)
# else:
#     items.remove(i)
# print(*items, sep=" | ")




