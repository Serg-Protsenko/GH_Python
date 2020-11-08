'''
5. Write a script to convert decimal to hexadecimal
        Sample decimal number: 30, 4
        Expected output: 1e, 04
'''
list_nums = [int(i) for i in input('Enter decimal numbers: ').split(',')]
list_hex = [hex(i)[2:] for i in list_nums]
print('Hexadecimal numbers: ', ', '.join(list_hex))