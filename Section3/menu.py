items = ["Pho", "Com", "Bun"]
# print(items[1])
print(items)
print(len(items))
items.append("Xoi xeo")
print(items)
print(type(items))
print(len(items))
print(*items, sep="\n")
position = int(input("position to read ? "))
print(items[position-1])


