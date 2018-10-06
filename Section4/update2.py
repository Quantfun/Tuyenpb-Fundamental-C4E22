person = {
    "name": "Ivy",
    "age": 5,
}
print(person)

update = input("Do you want to update or delete ? D/U ")

if update == "D":
    key = input("what key do you want to delete? name/age ")
    del person[key]
elif update == "U":
    key = input("what key do you want to update? name/age ")
    value = input("Enter your new key: ")
    person[key]= value

print(person)
