#-*- coding: utf-8 -*-

"""
Вхідні дані: рядок, що складається з відкриваючих та закриваючих круглих дужок - аргумент командного рядка. Для передачі в якості рядка послідовність береться в подвійні лапки.

Результат роботи: рядок "YES", якщо вхідний рядок містить правильну дужкову послідовність; або рядок "NO", якщо послідовність є неправильною. Дужкова послідовність вважається правильною, якщо всі дужки можна розбити попарно "відкриваюча"-"закриваюча", при чому в кожній парі закриваюча дужка слідує після відкриваючої.

Пояснення для математиків:
"" (порожній рядок) - правильна дужкова послідовність (ПДП)
"(ПДП)" - також ПДП
"ПДППДП" (дві ПДП записані поряд) - також ПДП

Наприклад
Вхідні дані: ")("
Приклад виклику: python lab4_3.py ")("
Результат: NO
Вхідні дані: "(()(()"
Приклад виклику: python lab4_3.py "(()(()"
Результат: NO
Вхідні дані: "(()(()()))"
Приклад виклику: python lab4_3.py "(()(()()))"
Результат: YES
Вхідні дані: "())()(()())(()"
Приклад виклику: python lab4_3.py "())()(()())(()"
Результат: NO
"""


import sys

a=sys.argv[1]
a_long=len(a)

if a=="":
	print "YES"

elif a_long%2!=0:
	print "NO"

else:
	
	if a[0]==")":
		print "NO"
	else:
		
		if a.count("(")>a_long/2:
			print "NO"
		elif a.count(")")>a_long/2:
			print "NO"
		elif a[1]==")" and a[2]==")":
			print "NO"
		else:		
			print "YES"
