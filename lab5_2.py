#-*- coding: utf-8 -*-

"""
Розробити функцію counter(a, b), 
яка приймає 2 аргументи -- цілі невід'ємні числа a та b, 
та повертає число -- кількість різних цифр числа b, які містяться у числі а.

Наприклад
Виклик функції: counter(12345, 567)
Повертає: 1
Виклик функції: counter(1233211, 12128)
Повертає: 2
Виклик функції: counter(123, 45)
Повертає: 0
"""



def counter(a, b):
	a=str(a)
	b=str(b)
	c=""
	count_b=0
	for i in b: 
		if i not in c:
			c=c+i
	for j in c: 
		if j in a:
			count_b=count_b+1
	
	return count_b


