# -*- coding: UTF-8 -*-
# Сделайте функцию, которая будет возвращать длину переданного ей как аргумент имени

# *Сделайте функцию, которая принимает ваш номер телефона в виде строки 
# (вместе с + если он есть). Превращает этот номер в отсортированный список чисел 
# и возвращает его . 
# Так же в консоль выводится максимальная цифра в номере и минимальная, 
# а также количество цифр, которые встречаются в вашем номере более одного раза.

def my_len(sample:str):
	print(len(sample))

def convert_number(s:str):

	digits = list(filter(str.isdecimal, list(s) ))
	digits.sort()
	print(digits)

	len_dict = dict()

	for item in digits:
		#try:
		#	#val = len_dict[item] + 1 
		#	len_dict[item] += 1
		#except:
		#	len_dict[item] = 1
		#if item in len_dict:
		#	len_dict[item] += 1
		#else:
		#	len_dict[item]  = 1

		# Andrey - most compact record:
		len_dict[item] = len_dict.get(item, 0) + 1

	# Andrey - unfinished solution with map() - not working
	#def count_key(x:int):
	#	len_dict[x] = len_dict.get(x, 0) + 1
	#map(count_key, digits)			

	print(len_dict)
	print(len(list(filter(lambda x: len_dict[x] > 1, len_dict.keys() ))))


	print(max(digits))
	print(min(digits))



number = '+7 0204 -3924'

my_len(number)

convert_number(number)

