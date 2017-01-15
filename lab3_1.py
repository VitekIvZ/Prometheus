#-*- coding: utf-8 -*-

"""
Вхідні дані: 3 дійсних числа a, b, c. Передаються в програму як аргументи командного рядка.

Результат роботи: рядок "triangle", якщо можуть існувати відрізки з такою довжиною та з них можна скласти трикутник, або "not triangle" -- якщо ні.

Наприклад
Вхідні дані: 10 20 30
Приклад виклику: python lab3_1.py 10 20 30
Результат: not triangle
Вхідні дані: 1 1 1
Приклад виклику: python lab3_1.py 1 1 1
Результат: triangle
Вхідні дані: 5.5 5.5 -2
Приклад виклику: python lab3_1.py 5.5 5.5 -2
Результат: not triangle
"""


import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if x <= 0 or y <= 0 or z <=0:
    print "not triangle"
else:
    if (y == z and (y+z)>x) or (x == y and (x+y)>z) or (x == z and (x+z)>y):
       print "triangle"
    elif (y != z and (y+z)>x) and (x != y and (x+y)>z) and (x != z and (x+z)>y):
        print "triangle"
    else:
        print "not triangle"
