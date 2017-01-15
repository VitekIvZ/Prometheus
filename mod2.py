#-*- coding: utf-8 -*-

"""
Розробити функцію convert_n_to_m(x, n, m), яка приймає 3 аргументи -- ціле число (в системі числення з основою n) або рядок x, що представляє таке число, та цілі числа n та m (1 <= n, m <= 36), та повертає рядок -- представлення числа х у системі числення m.

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

def convert_n_to_m(x, n, m):
	try:
		if type(x)==float or type(x)==dict or type(x)==list or n < 1 or m > 36:
			return False
		else:
			if type(x)==str:
				x_upper=x.upper()
			else:
				x_upper=str(x)
				if x_upper[0]=="-":
					return False

			d={"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "A":10, "B":11, "C":12, "D":13, "E":14, "F":15, "G":16, "H":17, "I":18, "J":19, "K":20, "L":21, "M":22, "N":23, "O":24, "P":25, "Q":26, "R":27, "S":28, "T":29, "U":30, "V":31, "W":32, "X":33, "Y":34, "Z":35}
			x_10=0
			k=len(x_upper)-1
			a=0
			x_m=""

			n=int(n)
			m=int(m)

			for i in x_upper:
				a=int(d.get(i,0))
				if a >= n:
					return False
				else:
					x_10 = x_10+a*(n**k)
					k = k-1

			if m > 1:
				while x_10 > m:
					for key, value in d.iteritems():
                        			if x_10%m == value:
                            				x_m = x_m+key
					x_10 = x_10//m
				
				if x_10 == m:
					x_m = x_m+"01"
				elif x_10 > 9:
					for key, value in d.iteritems():
                        			if x_10 == value:
                            				x_m = x_m+key
				else:
					x_m = x_m+str(x_10)
				rez = x_m[::-1]

			else:
				rez = "0"*x_10
			
			return rez
	except (TypeError, ValueError):
		return False
