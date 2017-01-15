#-*- coding: utf-8 -*-

"""
Розробити функцію saddle_point(matrix), 
яка приймає 1 аргумент -- прямокутну матрицю цілих чисел, задану у вигляді списка списків, 
та повертає тьюпл із координатами "сідлової точки" переданої матриці або логічну константу False, якщо такої точки не існує.

Сідловою точкою вважається такий елемент матриці, який є мінімальним (строго менше за інші) у своєму рядку та максимальним (строго більше за інші) у своєму стовпці, наприклад:
матриця:
1 2 3
0 2 1
"1" в лівому верхньому кутку (за координатами (0;0)) є сідловою точкою матриці.

Вважати, що передані дані є коректними, тобто матриця не містить інших значень крім цілих чисел, а всі вкладені списки мають однакову довжину. Результуючий тьюпл містить два числа -- порядкові номери сідлової точки в рядку (індекс його списка у зовнішньому списку) та в стовпці (індекс у внутрішньому списку).

Наприклад
1 2 3
3 2 1
Виклик функції: saddle_point([[1,2,3],[3,2,1]])
Повертає: False
8 3 0 1 2 3 4 8 1 2 3
3 2 1 2 3 9 4 7 9 2 3
7 6 0 1 3 5 2 3 4 1 1
Виклик функції: saddle_point([[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]])
Повертає: (1, 2)
21
Виклик функції: saddle_point([[21]])
Повертає: (0, 0)
"""




def saddle_point(matrix):
	if not isinstance(matrix, list) or not isinstance(matrix[0], list):
		return False
	size = len(matrix[0])
	for row in matrix:
		if not isinstance(row, list) or len(row) <> size:
			return False
	for row in matrix:
		string = ''
		for el in row:
			string = string + "%4d" % (el)
		print string
	min_el_in_raw=[]
	for i in range(len(matrix)):
		min_el_in_raw.append(min(matrix[i]))
	
	max_el_in_col=max(min_el_in_raw)
	index_el=min_el_in_raw.index(max_el_in_col)

	if matrix[index_el].count(max_el_in_col)>1:
		return False

	if min_el_in_raw.count(max_el_in_col)>1:
		return False

	index_el_matrix=matrix[index_el].index(max_el_in_col)

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][index_el_matrix]>max_el_in_col:
				return False
			

	return (index_el, index_el_matrix)
