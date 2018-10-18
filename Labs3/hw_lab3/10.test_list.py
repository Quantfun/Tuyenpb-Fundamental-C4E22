from even_list import *

even_list = even_list([1, 2, 5, 9, -10, 6])
# print(even_list)

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")