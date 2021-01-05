'''
1. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість 
color з початковим значенням white і метод для зміни кольору фігури, а його підкласи 
«овал» (oval) і «квадрат» (square) містять методи __init__ для завдання початкових 
розмірів об'єктів при їх створенні.
'''

class Figure(object):
    color = 'white'
  
    def change_color(self, color):
        self.color = color
 
 
class Oval(Figure):
 
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
 
 
class Square(Figure):
 
    def __init__(self, length):
        super().__init__()
        self.length = length

ol = Oval(5, 10)
print(ol.color)
ol.change_color('red')
print(ol.color)


print()

sq = Square(10)
print(sq.color)
sq.change_color('green')
print(sq.color)
