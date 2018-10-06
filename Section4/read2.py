pokemon = {
    "name": "Pokemon",
    "owner": "Ash",

}
key = input("what ? ")
if key in pokemon:
    value = pokemon[key]
    print(value)
else:
    print("Not found")
