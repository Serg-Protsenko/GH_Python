'''
4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець 
діапазона, і вертатиме список простих чисел всередині цього діапазона.
'''

def prime_list(start, stop):
    lst = [i for i in range(start, stop + 1)]
    prime_lst = []
    
    for i in lst:
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_lst.append(i)
    return prime_lst

start = int(input())
stop = int(input())
prime_list(start, stop)
print(f'For the list of numbers: {[i for i in range(start, stop + 1)]} \nPrime numbers are {prime_list(start, stop)}.')