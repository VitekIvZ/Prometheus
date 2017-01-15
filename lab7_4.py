#-*- coding: utf-8 -*-

"""

Розробити функцію create_calendar_page(month,year), 
яка приймає 2 аргументи -- цілі числа -- місяць (нумерація починається з 1) і рік, 
та повертає оператором return 1 рядок, який містить сторінку календаря на цей місяць.

Якщо місяць та рік не задані, використати сьогоднішні значення.

"Сторінка", що повертається, має наступний формат:
приклад результату
Це значення є одним рядком із переносами рядка \n, пробіли після числа 28 відсутні. Зайві пробіли в кінці під-рядків або всього рядка, як і зайві порожні рядки недопустимі.

Тести із некорестними даними не проводяться.

Приклад викликів для тестування функції:
print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)

"""

def create_calendar_page(month=None, year=None):

	lin='--------------------\nMO TU WE TH FR SA SU\n--------------------\n'
		

	if month==None:
		month=datetime.date.today().month
	else:
		month=month
	
	if year==None:
		year=datetime.date.today().year
	else:
		year=year
	

	calendars = calendar.monthcalendar(year, month)

	while calendars[len(calendars)-1][len(calendars[len(calendars)-1])-1]==0:
		del(calendars[len(calendars)-1][len(calendars[len(calendars)-1])-1])

	for a in calendars:
		for b in a:
			if b==0:
				lin=lin+"  "+" "
			elif len(str(b))==1:
				lin=lin+"0"+str(b)+" "
			else:
				lin=lin+str(b)+" "
		lin=lin+"\n"


	return lin

