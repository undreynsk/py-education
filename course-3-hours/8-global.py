# -*- coding: UTF-8 -*-
# 8. Пространства имен
# Изучите локальные и глобальные переменные в функции, 
# попробуйте изменить глобальную переменную из функции. (Погуглите ключевые слова global и nonlocal)



def my_len(sample:str):
	global number

	s = 1
	print(number)
	print(len(sample))

	def inner_f():
		nonlocal s
		#nonlocal number
		print(s)

	inner_f()


number = '+7 0204 -3924'

my_len(number)



