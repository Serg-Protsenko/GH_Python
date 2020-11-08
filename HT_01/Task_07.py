'''
7. Write a script to concatenate all elements in a list into a string and print it.
'''

our_list = [1, 2, 3, 4, 5, 'a', 'b', 'c', (6, 7, 8)]
our_string_list = list(map(str, our_list))
our_string = ''.join(our_string_list)
print(our_string)