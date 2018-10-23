def is_inside(number_range,range_test):
    x1 = number_range[0]
    y1 = number_range[1]

    x = range_test[0]
    y = range_test[1]
    z = range_test[2]
    t = range_test[3]

    check = x <= x1 and x1 <= x + z and y <= y1 and y1 <= y +t

    if check  == True:
        print("True")
    else:
        print("False")
    return check    

is_inside([100,120],[120,90,60,90])

# x = ([1,2],[2,3,3,4])
# print(type(x))