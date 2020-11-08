'''
11. Write a script to remove duplicates from Dictionary.
'''

our_dict = {'a': 123, 'b': 123, 'c': 231, 'd':231, 'e':321, 'f':321}
new_dict ={}
for key, value in our_dict.items():
    if value not in new_dict.values():
        new_dict[key] = value
print(new_dict)