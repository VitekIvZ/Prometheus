#-*- coding: utf-8 -*-

"""
Завдання передбачає пошук "щасливих" квитків. "Щасливим" називається такий тролейбусний квиток, в якому сума перших трьох цифр дорівнює сумі останніх трьох. Наприклад 030111 (0+3+0 = 1+1+1), 902326 (9+0+2 = 3+2+6), 001100 (0+0+1 = 1+0+0).

Вхідні дані: два цілих невід'ємних числа (0<=a1<=a2<=999999) - аргументи командного рядка.

Результат роботи: кількість "щасливих квитків", чиї номери лежать на проміжку від a1 до a2 включно. Якщо число на проміжку має менше 6 розрядів, вважати, що на його початку дописуються нулі у необхідній кількості, як це і відбувається при нумерації квитків. Виводити номери квитків не треба.

Наприклад
Вхідні дані: 0 1000
Приклад виклику: python lab4_4.py 0 1000
Результат: 1
Пояснення: номер 000000
Вхідні дані: 1001 1122
Приклад виклику: python lab4_4.py 1001 1122
Результат: 3
Пояснення: номери 001001, 001010, 001100
Вхідні дані: 222222 222333
Приклад виклику: python lab4_4.py 222222 222333
Результат: 7
Пояснення: номери 222222, 222231, 222240, 222303, 222312, 222321, 222330
"""


import sys
a=int(sys.argv[1])
b=int(sys.argv[2])
count=0


for i in range(a, b+1):
	tmp=""
	tmp=str(i).zfill(6)
	
	l_sum=0
	for l in range(3):
		l_sum = l_sum + int(tmp[l])
	r_sum = 0	
	for r in range(3,6):
		r_sum = r_sum + int(tmp[r])
	
	if l_sum == r_sum:
		count = count + 1

print count
