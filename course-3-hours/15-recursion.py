# 15. Рекурсия
# Напишите рекурсивную функцию для вычисления факториала числа

import sys

def factorial(num: int) -> int:
	fact = 0

	if num < 1:
		return 1

	if num < 2:
		return num

	fact = factorial( num - 1 )

	return fact * num


start = int(sys.argv[1])
print(f"{start}! = {factorial(start)}")