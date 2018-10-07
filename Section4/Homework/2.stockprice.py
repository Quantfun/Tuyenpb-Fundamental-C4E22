prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,

}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}

##Print prices & stock of each item
# select = input("Select your item: ")
# print(select,"price: ", prices[select], "stock: ",stock[select])

total = 0
for x in prices:
    value = int(prices[x]*stock[x])
    print(x,value)
    total += value
print("Total: ",total)