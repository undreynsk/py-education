# 11. Генераторы, итераторы
# Создайте генератор, в котором будет иплементирован словарь, в котором ключ 
# - это название месяца, а значение - кол-во дней в этом месяце. 
# Этот генератор должен возвращать сообщение 
# по типу "В месяце Январь 31 день" или в "В месяце Апрель 30 дней". 
# Выведите с помошью цикла for все доступные значения из генератора.


m={'j':31, 'f':28}

def days(month:str):
	yield f"In '{month}': {m.get(month, month + ' does not exists')}"
	#yield "a"
	#yield f"In '{month}'"


for d in ['f', 'j', 'f', 'n']:
	#print(f"getting value for key '{d}'\n")
	print(next(days(d)))

#month = 'd'
#print(f"In '{month}': {m.get(month, default=month + ' does not exists')}")
#print(f"In '{month}': {m.get(month, month + ' does not exists')}")
#print(next(days('d')))
#print(days('f'))
