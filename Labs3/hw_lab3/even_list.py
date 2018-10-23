def even_list(numbers):
    numberx = []
    for i in numbers:
        if i % 2 == 0:
            numberx.append(i)
    print(numberx)
    return numberx

numbers = [0,1,3,5,9,7,10]
even_list(numbers)
                
