'''
8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. 
Тобто, функція приймає два аргументи: список і величину зсуву (якщо ця величина додатня - 
пересуваємо з кінця на початок, якщо від'ємна - навпаки - пересуваємо елементи з початку списку в його кінець).
   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
'''

lst = [1, 2, 3, 4, 5]

def list_shift(lst, shift):
    if shift == 0:
        return lst
    else:
        return lst[-shift:] + lst[:-shift]

shift = int(input('Enter shift: '))
print(f'The origin list: {lst}')
print(f'The modified  list: {list_shift(lst, shift)}')