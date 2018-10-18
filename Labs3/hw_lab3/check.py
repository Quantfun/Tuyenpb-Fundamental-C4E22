def is_inside([x1,y1],[x,y,z,t]):
    check = and(x <= x1 <= x + z,y <= y1 <= y +t)
    if check  = True:
        print("True")
    else:
        print("False")
    return check    

is_inside([100,120],[80,90,60,90])

# x = ([1,2],[2,3,3,4])
# print(type(x))