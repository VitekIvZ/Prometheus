#-*- coding: utf-8 -*-

"""
Розробити функцію find_fraction(summ), 
яка приймає 1 аргумент -- невід'ємне ціле число summ, 
та повертає тьюпл, що містить 2 цілих числа -- чисельник та знаменник найбільшого правильного нескорочуваного дробу, для якого сума чисельника та знаменника дорівнює summ. Повернути False, якщо утворити такий дріб неможливо.

Тести із некоректними даними не проводяться.

Приклад послідовності дій для тестування:
print find_fraction(2) # False
print find_fraction(3) # (1, 2)
print find_fraction(10) # (3, 7)
print find_fraction(62) # (29, 33)
print find_fraction(150000001) # (75000000, 75000001)

"""

def find_fraction(summ):
	if summ>2:
		c=int(summ/2)
		z=int(summ)-c
		while c>1:
			if c==z or (c%2==0 and z%2==0) or z%c==0:
				c=c-1
				z=int(summ)-c
			else:
				break
		return (c, z)
	else:
		return False
				
