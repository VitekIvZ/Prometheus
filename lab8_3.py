#-*- coding: utf-8 -*-

"""
Розробити функцію bouquets(narcissus_price, tulip_price, rose_price, summ), 
яка приймає 4 аргументи -- додатні дійсні числа (ціни за один нарцис, тюльпан та троянду, і суму грошей у кишені головного героя), 
та повертає ціле число -- кількість варіантів букетів, які можна скласти з цих видів квітів, таких щоб вартість кожного букету не перевищувала summ.

Не забути, що букети з парною (загальною) кількістю квітів живим дівчатам не дарують. Тести із некоректними даними не проводяться.

Приклад послідовності дій для тестування:
print bouquets(1,1,1,5) # 34
print bouquets(2,3,4,10) # 12
print bouquets(2,3,4,100) # 4019
print bouquets(200,300,400,10000) # 4019
print bouquets(200,300,400,100000) # 3524556

"""

def bouquets(narcissus_price, tulip_price, rose_price, summ):
	n_max=int(summ/narcissus_price)
	t_max=int(summ/tulip_price)
	r_max=int(summ/rose_price)
	count=0
	for i in range(n_max+1):
		for j in range(t_max+1):
			for k in range(r_max+1):
				if (i+j+k)%2!=0:
					if (i*narcissus_price+j*tulip_price+k*rose_price)<=summ:
						count=count+1
	return count
