#-*- coding: utf-8 -*-

"""
Вхідні дані: довільна, відмінна від нуля, кількість значень - аргументів командного рядка. Значеннями-аргументами можуть бути числа або рядки, які складаються з цифр та літер латинського алфавіту без пробілів.

Результат роботи: рядок, що складається з отриманих значень в зворотньому порядку, записаних через пробіл. Пробіл в кінці рядка відсутній.

Наприклад
Вхідні дані: 1
Приклад виклику: python lab4_3.py 1
Результат: 1
Вхідні дані: qwe asd zxc 123
Приклад виклику: python lab4_3.py qwe asd zxc 123
Результат: 123 zxc asd qwe
Вхідні дані: padawan young my HAVE MUST YOU PATIENCE
Приклад виклику: python lab4_3.py padawan young my HAVE MUST YOU PATIENCE
Результат: PATIENCE YOU MUST HAVE my young padawan
"""


import sys

if len(sys.argv)==2:
    s = sys.argv[1]
else: 
    s=sys.argv[1:]


if type(s) == str:
    s_list = s.split(' ')
    a = s_list[::-1]
    print " ".join(a)
elif type(s) == list:
    a = s[::-1]
    print " ".join(a)

