'''
6. Write a script to check whether a specified value is contained in a group of values.
        Test Data :
        3 -> [1, 5, 8, 3] : True
        -1 -> (1, 5, 8, 3) : False
'''

our_list = [1, 5, 8, 3]
our_tuple = (1, 5, 8, 3)

value = 3
check = False
if value in our_list:
    check = True
else:
    check = False
print(f'{value} -> {our_list} : {check}')

value = -1
if value in our_tuple:
    check = True
else:
    check = False
print(f'{value} -> {our_tuple} : {check}')