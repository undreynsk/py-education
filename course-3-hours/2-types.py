# Создайте список, содержащий разные типы данных (строку, число, список, кортеж и т.д.)
# и определите их типы с помощью функции type(). Выведите эти типы на экран

import pprint as pprint

mixed_types = [
	'and'
	, 50
	, 4.25
	, True 
	, [ 'a', '1' ]
	, ( 1,2,3,45 ) 
	, { 'b' : 1, 'a' : 1, 2 : 3 }
	, set([ 'a', '1', 'a' ])
]

a = { 'b' : 1, 'a' : 1, 2 : 3 }

for i in mixed_types:
	print(f"'{i}' : {type(i)}")

pprint.pprint( mixed_types, sort_dicts=True)	

