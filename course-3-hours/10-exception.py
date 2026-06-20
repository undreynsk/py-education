# 10. Исключения
# Напишите функцию, которая вызывает input с просьбой ввести ваш возраст. 
# Если полученный ответ не возможно конверитровать в число, 
# то функция должна вывести ошибку и предлагать ввести возраст пока юзер не введет валидное число

import pprint

def is_valid_input(s): 
	try:
		int(s)
	except Exception as e:
		print(f"Error: {e}")
		return False
	else:
		return True

while True:
	from_cli = input("Please input number: ")
	res = is_valid_input(from_cli)
	if res == True:
		break
