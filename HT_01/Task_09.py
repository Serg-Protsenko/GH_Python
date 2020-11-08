'''
9. Write a script to remove an empty tuple(s) from a list of tuples.
        Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
        Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
'''

our_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
new_list = [i for i in our_list if i]
print(new_list)