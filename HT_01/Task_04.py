'''
4. Write a script to concatenate N strings.
'''

lst_string = []
while True:
    our_string = input('Enter some string or nothing for exit: ')
    if our_string:
        lst_string.append(our_string)
    else:
        break
print(' '.join(lst_string))