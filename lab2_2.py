#-*- coding: utf-8 -*-

""""
Вхідні дані: 3 числа x, y та z. x, y -- невід'ємні цілі числа, z дорівнює 0 або 1. x не дорівнює 0. Передаються як аргументи командного рядка.

Вихідні дані: рядок "Everybody sing a song: <текст пісеньки>.", де <текст пісеньки> формується з у куплетів, розділених пробілами. Всі куплети однакові і складаються з x 'la' через дефіс. Якщо z дорівнює одиниці, в кінці ставиться окличний знак, інакше крапка. За відсутності куплетів пробіл перед крапкою/окличним знаком не ставиться.

Підказка: для цього можна застосувати множення рядків.

Приклад
Вхідні дані: 2 3 1
Приклад виклику: python lab2_2.py 2 3 1
Результат: Everybody sing a song: la-la la-la la-la!
Вхідні дані: 1 0 0
Приклад виклику: python lab2_2.py 1 0 0
Результат: Everybody sing a song:.
""""



import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])
song = []
for i in range(0, x):
    song.append('la')

if z == 1:
    print "Everybody sing a song:" + (" " + '-'.join(song))*y + "!"

elif z == 0:
    print "Everybody sing a song:" + (" " + '-'.join(song))*y + "."
