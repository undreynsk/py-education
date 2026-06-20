# 17. ФП
# Создайте последовательность чисел от -10 до 10 включительно. 
# С помощью функции map и вспомогательного callable сделайте 
# эту последовательность чисел другой последовательностью, 
# каждое число которой на 10 меньше предыдущего (если оно было отрицательное) 
# и на 10 больше предыдущего (если он положительное).
# В результате вы должны получить [-20, -19, ... - 11, 0 , 11, 12 ... 19, 20]

import sys

seq = list(range(-10,11))

class PlusDelta:
	def __init__(self, delta):
		self.delta = delta

	def __call__(self, num):
		if ( num == 0 ):
			return 0
		elif ( num < 0 ):
			return num - self.delta
		else:
			return num + self.delta

print(seq)

s = PlusDelta(10)
#print(s(5))

new_seq = list(map(s, seq))

print(new_seq)

#start = int(sys.argv[1])
#print(f"volume({start}) = {volume(start)}")