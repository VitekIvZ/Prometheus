#-*- coding: utf-8 -*-

"""
Розробити функцію find_most_frequent(text), 
яка приймає 1 аргумент -- текст довільної довжини, який може містити літери латинського алфавіту, пробіли та розділові знаки (,.:;!?-); 
та повертає список слів (у нижньому регістрі), які зустрічаються в тексті найчастіше.

Слова, записані через дефіс, вважати двома словами (наприклад, "hand-made"). Слова у різних відмінках, числах та з іншими перетвореннями (наприклад, "page" та "pages") вважаються різними словами. Регістр слів -- навпаки, не має значення: слова "page" та "Page" вважаються 1 словом.

Якщо слів, які зустрічаються найчастіше, декілька -- вивести їх в алфавітному порядку.

Наприклад
Виклик функції: find_most_frequent('Hello,Hello, my dear!')
Повертає: ['hello']
Виклик функції: find_most_frequent('to understand recursion you need first to understand recursion...')
Повертає: ['recursion', 'to', 'understand']
Виклик функції: find_most_frequent('Mom! Mom! Are you sleeping?!!!')
Повертає: ['mom']
"""



def find_most_frequent(text):
	if text!="":
		t=""
		for i in text:
			if i.isalpha():
				t=t+i
			else:
				t=t+" " 
		t_list=t.lower().split(" ")	
	
		d={}
		for i in range(len(t_list)):
			if t_list[i].isalpha():
				if t_list[i] not in d:
					d[t_list[i]]=t_list.count(t_list[i])
		c=d.values()
		max_el_in_d=max(c)
		rez = list(k for k,v in d.iteritems() if max_el_in_d == v)
	
		rez.sort()
		return rez
	else:
		return list()
