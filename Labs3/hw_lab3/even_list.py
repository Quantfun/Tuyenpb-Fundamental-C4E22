def even_list(list):
    for i in list[:]:
        if i % 2 != 0:
            list.remove(i)
    print(list)
    return list

list = [0,1,3,5,9,7,10]
even_list(list)
                
