# 13. Декораторы
# Создайте декоратор timer, который засекает время выполнения декорируемой функции 
# и выводит его на экран.

import time

#def my_decorator(func):
#    def wrapper():
#        print("До выполнения функции")
#        func()
#        print("После выполнения функции")
#    return wrapper
#
#@my_decorator
#def say_hello():
#    print("Hello!")
#
#say_hello()


def log_time(func):
	def wrapper(*args, **kwargs):
		start = time.perf_counter()
		print(f"{start}: started\n")

		func(*args, **kwargs)
		
		end = time.perf_counter()
		print(f"{end}: ended\n")

		print(f"function took {end - start} seconds\n")
	return wrapper

@log_time
def say(content):
	print(content)
	time.sleep(2)

say("my bed")	

