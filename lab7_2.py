#-*- coding: utf-8 -*-

"""
Розробити класс Student для представлення відомостей про успішність слухача курсу Prometheus. Об'єкт класу має містити поля для збереження імені студента та балів, отриманих ним за виконання практичних завдань і фінального екзамена.

Забезпечити наступні методи класу:

конструктор, який приймає рядок -- ім'я студента -- та словник, що містить налаштування курсу у наступному форматі:
conf = {
'exam_max': 30, # кількість балів, доступна за здачу екзамена
'lab_max': 7, # кількість балів, доступна за виконання 1 практичної роботи
'lab_num': 10, # кількість практичних робіт в курсі
'k': 0.61, # частка балів від максимума, яку необхідно набрати для отримання сертифікату
}.
метод make_lab(m,n), який приймає 2 аргументи та повертає посилання на поточний об'єкт. Тут m -- кількість балів набрана за виконання завдання (ціле або дійсне число), а n -- ціле невід'ємне число, порядковий номер завдання (лаби нумеруються від 0 до lab_num-1). При повторній здачі завдання зараховується остання оцінка. Якщо n не задане, мається на увазі здача першого невиконаного практичного завдання. Врахувати, що під час тестування система іноді дає збої, тому за виконання завдання може бути нараховано більше балів ніж це можливо за правилами курсу, що не повинно впливати на рейтинг студента. Крім того в системі можуть міститися додаткові завдання, чиї номери виходять за межі 0..lab_num -- звичайно, бали за них не повинні зараховуватися для отримання сертифікату.
метод make_exam(m), який приймає 1 аргумент -- ціле або дійсне число, оцінку за фінальний екзамен, та повертає посилання на поточний об'єкт. Як і у випадку з практичними завданнями, оцінка за екзамен в результаті помилки іноді може перевищувати максимально допустиму.
метод is_certified(), який повертає тьюпл, що містить дійсне число (суму балів студента за проходження курсу), та логічне значення True або False в залежності від того, чи достатньо цих балів для отримання сертифікату.
Так як курс є доступним онлайн і не має дедлайнів на здачу робіт, студент може виконувати роботи в довільному порядку. Вважати, що кількість спроб на виконання кожного з завдань необмежена.

Приклад послідовності дій для тестування класу:
conf = {
'exam_max': 30,
'lab_max': 7,
'lab_num': 10,
'k': 0.61,
}
oleg = Student('Oleg', conf)
oleg.make_lab(1) \ # labs: 1 0 0 0 0 0 0 0 0 0, exam: 0
.make_lab(8,0) \ # labs: 7 0 0 0 0 0 0 0 0 0, exam: 0
.make_lab(1) \ # labs: 7 1 0 0 0 0 0 0 0 0, exam: 0
.make_lab(10,7) \ # labs: 7 1 0 0 0 0 0 7 0 0, exam: 0
.make_lab(4,1) \ # labs: 7 4 0 0 0 0 0 7 0 0, exam: 0
.make_lab(5) \ # labs: 7 4 5 0 0 0 0 7 0 0, exam: 0
.make_lab(6.5) \ # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 0
.make_exam(32) # labs: 7 4 5 6.5 0 0 0 7 0 0, exam: 30
print oleg.is_certified() # (59.5, False)
oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print oleg.is_certified() # (62.5, True)

"""

class Student():
	exam_max=None
	lab_max=None
	lab_num=None
	k=None
	students=[]
	labs=None
	exam=None
	
	def __init__(self, name=None, conf=None):
		keys = conf.keys()
		self.name=name
		self.students.append({"name":self.name, "labs":[], "exam":0})
		if 'exam_max' in keys:
			self.exam_max = conf['exam_max']
		if 'lab_max' in keys:
			self.lab_max = conf['lab_max']
		if 'lab_num' in keys:
			self.lab_num = conf['lab_num']
		if 'k' in keys:
			self.k = conf['k']
       
	def make_lab(self, m=None, n=None):
		self.m = m
		self.n = n
		for i in self.students:
			for k,v in i.iteritems():
				if v == self.name:
					if len(i.get("labs"))<self.lab_num:
						while len(i.get("labs"))<self.lab_num:
							i.get("labs").append(0)
		if self.n==None:
			for i in self.students:
				for k,v in i.iteritems():
					if v == self.name:
						for b in range(len(i.get("labs"))):
							if i.get("labs")[b]==0:
								if self.m>=self.lab_max:
									i.get("labs")[b]=self.lab_max
									break
								else:
									i.get("labs")[b]=self.m
									break
		elif self.n>=0 and self.n<=self.lab_num-1:
			for i in self.students:
				for k,v in i.iteritems():
					if v == self.name:
						for b in range(len(i.get("labs"))):
							if b==self.n:
								if self.m>=self.lab_max:
									i.get("labs")[b]=self.lab_max
								else:
									i.get("labs")[b]=self.m
		for i in self.students:
			for k,v in i.iteritems():
				if v == self.name:
					labs=i.get("labs")
					exam=i.get("exam")	
		return "labs: {}, exam: {}".format(" ".join(str(v) for v in labs), str(exam))					
									
	def make_exam(self, m=0):
		self.m_e=m

		for i in self.students:
			for k,v in i.iteritems():
				if v == self.name:
					if self.m_e>=self.exam_max:
						i["exam"]=self.exam_max
					else:
						i["exam"]=self.m_e

		for i in self.students:
			for k,v in i.iteritems():
				if v == self.name:
					labs=i.get("labs")
					exam=i.get("exam")	
		return "labs: {}, exam: {}".format(" ".join(str(v) for v in labs), str(exam))

	def is_certified(self):
		for i in self.students:
			for k,v in i.iteritems():
				if v == self.name:
					rez=sum(i.get("labs"))+i.get("exam")

			return (rez, (rez/100)>=self.k,)

		return None
