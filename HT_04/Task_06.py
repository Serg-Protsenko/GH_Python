'''
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
'''
def my_range(start, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0
    while (step > 0 and start < stop) or (step < 0 and start > stop):
        yield start
        start += step
 
print(f'With my range function: {list(my_range(5))}')
print(f'With build-in funcion: {list(range(5))}\n')
print(f'With my range function: {list(my_range(3,8))}')
print(f'With build-in funcion: {list(range(3,8))}\n')
print(f'With my range function: {list(my_range(3,8,2))}')
print(f'With build-in funcion: {list(range(3,8,2))}\n')
print(f'With my range function: {list(my_range(4,-1,-1))}')
print(f'With build-in funcion: {list(range(4,-1,-1))}\n')
print(f'With my range function: {list(my_range(0,-5))}')
print(f'With build-in funcion: {list(range(0,-5))}\n')