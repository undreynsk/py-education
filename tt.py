def f(data):
	result=[]

	for key, values in data.items():
		evens = [num for num in values if num % 2 == 0]
		if evens:
			result.append(evens)
	
	return result

data = {
	"a":[1,2,3],
	"b":[4,5,6],
	"c":[7,8,9]
}

print(f(data))