# Напишите программу, которая просит пользователя ввести число 
# и определяет, четное ли это число или нет. Выведите результат

import pprint

from_cli = input("Please input number: ")

def is_valid_input(s): 
	try:
		int(s)
	except Exception as e:
		print(f"Error: {e}")
		return False
	else:
		return True

if is_valid_input(from_cli):
	print( "Input is a number")

	if int(from_cli) % 2 == 0: 
		print("Input is even")
	else: 
		print("Input is odd")
#	print("Input is even") if ( ( int(from_cli) % 2 ) == 0 ) else print("Input is odd")		
else:
	print( "Input is NOT a number")

