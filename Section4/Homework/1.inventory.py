inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print(inventory)
inventory["pocket"] = ['seashell', 'strange berry', 'lint']
inventory["gold"] += 50
del inventory["backpack"][1]
print(inventory)