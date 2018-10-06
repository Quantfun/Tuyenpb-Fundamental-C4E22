person ={
    "name": "Quan",
    "age": 22,
    "location": "Hanoi",
}

# for k in person.keys():
#     print(k, person[k])

# for v in person.values():
#     print(v)

for k,v in person.items():
    print(k,v,sep=": ")