'''
8. Write a script to replace last value of tuples in a list.
        Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
        Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
'''

our_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = [i[:-1] + (100,) for i in our_list]
print(new_list)