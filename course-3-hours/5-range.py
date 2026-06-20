# Создайте с помощью рэнжа кортеж чисел от 20 до 50 включительно 
# и сделайте срез этого кортежа, 
# который будет содержать только четные числа этого кортежа в обратном порядке. 
# Выведите получившийся результат на экран

import pprint

li = tuple(i for i in range(20, 52))

print(list(filter( lambda x: x % 2 == 0, reversed(li))))

print(list(x for x in reversed(li) if x % 2 == 0))

# Wrong solution from course author:
#my_tuple = tuple(range(20, 52))
#my_slice = my_tuple[::-2]
#print(my_slice)

