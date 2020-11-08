'''
13. Write a script to get the maximum and minimum value in a dictionary.
'''

our_dict =  {'a': 1, 'b': 2, 'c': 3, 'd':4, 'e':5}
our_dict_values = our_dict.values()
max_value_dict = max(our_dict_values)
min_value_dict = min(our_dict_values)
print(f'Maximum value in a dictionary is {max_value_dict}.')
print(f'Minimum value in a dictionary is {min_value_dict}.')