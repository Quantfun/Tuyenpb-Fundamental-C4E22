items = ["Com", "Pho", "My xao"]

##Add new item
# favs = ["Net", "Game", "Gym"]
# print(favs)
# new_fav = input("New thing: ")
# favs.append(new_fav)
# print(favs)


##Replace
# items[2] = "Com trang"
# print(*items, " | ")

# #Update
position = int(input("Where to change ? "))
update = input("Change to what ? ")
items[position - 1] = update
print(*items, sep=" | ")

#Delete
# i = input("What to detete ")
# if i.isdigit():
#     position = int(i)
#     items.pop(position-1)
# else:
#     items.remove(i)
# print(*items, sep=" | ")




