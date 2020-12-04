'''
2. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, 
   а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна 
   кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
'''
 
from time import sleep
 
while True:
    for i in range(4):
        print('Red        Green')
        sleep(1)
 
    for i in range(2):
        print('Yellow     Green')
        sleep(1)
 
    for i in range(4):
        print('Green      Red')
        sleep(1)
 
    for i in range(2):
        print('Yellow     Red')
        sleep(1)