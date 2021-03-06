#-*- coding: utf-8 -*-

"""
Розробити функцію encode_morze(text), 
яка приймає 1 аргумент -- рядок, 
та повертає рядок, який містить діаграму сигналу, що відповідає переданому тексту, закодованому міжнародним кодом Морзе для англійського алфавіту. Розділові та інші знаки, що не входять до латинського алфавіту, ігнорувати. Регістром літер нехтувати.

Morze code

Для передачі повідомлення за одиницю часу приймається тривалість однієї крапки. Тривалість тире дорівнює трьом крапкам. Пауза між елементами одного знака -- одна крапка, між знаками в слові -- 3 крапки, між словами -- 7 крапок. Словом вважати послідовність символів, обмежена пробілами. Результуюча "діаграма" демонструє наявність сигналу в кожний проміжок часу: на і-й позиції знаходиться "^", якщо в цей момент передається сигнал, і "_", якщо сигналу немає. Зайві паузи в кінці повідомлення на "діаграмі" відсутні.

Пояснення

Наприклад
Виклик функції: encode_morze('Morze code')
Повертає: ^^^_^^^___^^^_^^^_^^^___^_^^^_^___^^^_^^^_^_^___^_______^^^_^_^^^_^___^^^_^^^_^^^___^^^_^_^___^
Виклик функції: encode_morze('Prometheus')
Повертає: ^_^^^_^^^_^___^_^^^_^___^^^_^^^_^^^___^^^_^^^___^___^^^___^_^_^_^___^___^_^_^^^___^_^_^
Виклик функції: encode_morze('SOS')
Повертає: ^_^_^___^^^_^^^_^^^___^_^_^
Виклик функції: encode_morze('1')
Повертає: 
"""



morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
}

def encode_morze(text):
	rez=""
	for x in text:
		if x.isalpha():
			for y in morse_code.get(x.upper()):
				for i in range(len(y)):
					if y == ".":
						rez=rez+"^"
					elif y == "-":
						rez=rez+"^^^"
				rez=rez+"_"
			rez=rez+"__"
		elif x==" ":
			rez=rez+"____"
	if len(rez):
		while rez[-1]=="_":
			rez=rez[:-1]
		
	return rez


