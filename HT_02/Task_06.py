'''
6. Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" -> просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
'''

# our_string =  "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345"
our_string = input()

def some_operation_with_row(sequence):
    if 30 <= len(sequence) <= 50:
        return print(f'Length of our sequence is {len(sequence)}')
    elif len(sequence) < 30:
        chars = []
        nums = []
        for i in sequence:
            if i.isdigit():
                nums.append(i)
            else:
                chars.append(i)
        suma_num = sum([int(i) for i in nums])
        only_chars = ''.join(chars)
        return print(f'Sum of numbers is {suma_num}. \nYour sequence without numbers: {only_chars}.')

    elif len(sequence) > 50:
        only_nums = int(''.join(i for i in sequence if i.isdigit()))
        only_chars = ''.join(i for i in sequence if i.isalpha())
        vowels = 0
        consonants = 0
        y = 0
        for char in only_chars:
            if char.lower() in ('a', 'e', 'i', 'o', 'u'):
                vowels += 1
            elif char.lower() == 'y':
                y += 1
            else:
                consonants += 1
        return print(f'Only numbers without letters - {only_nums}. \nIn your seguence - {only_chars} are {vowels} vowels, {consonants} consonants and {y} letters "y".')

some_operation_with_row(our_string)