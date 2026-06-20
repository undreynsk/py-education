def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

times_two = multiplier(2)
print(times_two(5))  # 10

"""
funcs = []

for i in range(3):
	def f():
		return i
	funcs.append(f)
	print(f())

print(i)

print([f() for f in funcs])	

for f in funcs:
	print(f())	
"""

# the response is [2,2,2]