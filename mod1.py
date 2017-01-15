#-*- coding: utf-8 -*-

"""
Розробити функцію convert_n_to_m(x, n, m), 
яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36), 
та повертає рядок -- представлення числа х у системі числення m.

У випадку, якщо аргумент х не є числом або рядком, або не може бути представленням цілого невід'ємного числа в системі числення з основою n, повернути логічну константу False.

В системах числення з основою більше десяти для позначення розрядів із значенням більше 9 використовувати літери латинського алфавіту у верхньому регістрі від A до Z. У вхідному x можуть використовуватися обидва регістри.

Вважати, що в одиничній системі числення число записується відповідною кількістю нулів.

Наприклад
Виклик функції: convert_n_to_m([123], 4, 3)
Повертає: False
Виклик функції: convert_n_to_m("0123", 5, 6)
Повертає: 102
Виклик функції: convert_n_to_m("123", 3, 5)
Повертає: False
Виклик функції: convert_n_to_m(123, 4, 1)
Повертає: 000000000000000000000000000
Виклик функції: convert_n_to_m(-123.0, 11, 16)
Повертає: False
Виклик функції: convert_n_to_m("A1Z", 36, 16)
Повертає: 32E7
"""




key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

import sys
a=sys.argv[1].replace(" ","")
b=""
c=[]
d=""

for i in range(len(a)):
	if ord(a[i])>=97 and ord(a[i])<=122:
		b=b+'a'
	elif ord(a[i])>=65 and ord(a[i])<=90:
		b=b+'b'

for i in range(0, len(b)-1, 5):
	if len(b[i:i+5])==5:
		c.append(b[i:i+5])

for el in c:
	d=d+alphabet[key.index(el)]

print d
