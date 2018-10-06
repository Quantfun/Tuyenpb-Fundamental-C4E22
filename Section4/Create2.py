person = {
    "name": "pikachu",
    "owner": "Ash"
}
text = input("Enter new item: ")
pair = text.split(",")
key, value = pair

person[key]= value
print(person)