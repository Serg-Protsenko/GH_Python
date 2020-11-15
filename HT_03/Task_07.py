'''
7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому.
'''
def repeat_in_list(lst):
    dict_1 ={}
    for i in lst:
        if i in dict_1:
            dict_1[i] += 1
        else:
             dict_1[i] = 1
    dict_2 ={}
    for key,value in dict_1.items():
        if value > 1:
            dict_2[key] = value
    return dict_2

lst = [1,2,3,4,5,1,3,5,6,7,2,3,4]
result = repeat_in_list(lst)
print(f'Dictionary of result is {result}')
for  key,value in result.items():
    print(f'Value {key} -- counts {value}')
