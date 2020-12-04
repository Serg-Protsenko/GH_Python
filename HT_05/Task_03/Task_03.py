'''
3. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини
   та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж
   є в файлі (наприклад, файл із двох символів і треба вивести по одному символу, то що 
   виводити на місці середнього блоку символів?)
'''

file_name_1 = "The_Zen_of_Python.txt"
file_name_2 = "Two_letters.txt"
file_name_5 = "Five_letters.txt"
file_name_6 = "Six_letters.txt"

n = int(input('Enter number of characters: '))

def number_of_file(filename, n):
    try:
        f = open(filename, 'r')
        text = f.read()

        lenght_text = len(text)
        if (n + n) >= lenght_text:
            print([text[:n], text[-n:]])
            raise Exception('Text in file is too little, show only first and last letters!')
            
        index_center = lenght_text // 2
        lst =[text[:n], text[index_center : index_center+n], text[-n:]]

        print(lst)
        print()
        print(text)

    except Exception as e:
        print(e)
        
    finally:
        f.close()

        return

print(number_of_file(file_name_2, n))