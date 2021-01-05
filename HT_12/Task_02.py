'''
2. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» 
та приймав кольор фігури при створенні екземпляру, а методи __init__ підкласів 
доповнювали його та додавали початкові розміри.
'''

class Figure(object):
 
    def __init__(self, color='white'):
        self.color = color
 
    def change_color(self, color):
        self.color = color
 
 
class Oval(Figure):
 
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        super().__init__(color)
 
 
class Square(Figure):
 
    def __init__(self, length, color):
        Figure.__init__(self, color)
        self.length = length


ol = Oval(5, 10, 'grey')
print(ol.color)
ol.change_color('red')
print(ol.color)

print()

sq = Square(10, 'grey')
print(sq.color)
sq.change_color('green')
print(sq.color)