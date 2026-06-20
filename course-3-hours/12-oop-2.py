#Полиморфизм. Создайте несколько классов животных с методом speak(), 
#который возвращает разные звуки для разных животных. 
#Создайте коллекцию из экземпляров этих классов и в цикле вызовите у каждого метод speak.

class Creature:

	def __init__(self):
		pass

	def speak(self):
		pass

class Dyno(Creature):
	def speak(self):
		return "arrr"


class Ptero(Creature):
	def speak(self):
		return "vah"

classes = Creature.__subclasses__()
for c in classes:
	d = c()
	print(d.speak())

