#12. ООП
#Создайте класс Car с атрибутами конкретной машины: марка, цвет и скорость. 
# Добавьте методы для увеличения и уменьшения скорости
#
#Наследование. Создайте класс ElectricCar, который наследует класс Car и
# добавляет атрибут заряда батареи.
#
#Инкапсуляция. Сделайте скорость приватным атрибутом и модифицируйте методы газ и стоп. 
#Изменяться скорость должна только при помощи этих методов. 
#Скорость не должна превышать 100 км/час. 
#Добавьте метод get_speed, который возвращает значение скорости в км/ч

class Vehicle:

	max_speed = 100

	# decorator definition
	def limit_speed(func):
		def wrapper(self, *args, **kwargs):
			func(self, *args, **kwargs)

			if self.__velocity > Vehicle.max_speed:
				print(f"Limiting speed '{self.__velocity}' -> {Vehicle.max_speed}" )
				self.__velocity = Vehicle.max_speed
			if self.__velocity < 0:
				print(f"Correcting speed '{self.__velocity}' -> 0" )
				self.__velocity = 0

		return wrapper				

	@limit_speed
	def __init__(self, model, color='white', velocity=0):
		#breakpoint()
		#print(f"{self=}, {type(self)=}")
		self.model    = model
		self.color    = color
		self.__velocity = velocity
		#self.limit_speed()

	@limit_speed
	def v_up(self,step=10):
		self.__velocity += step
		#self.limit_speed()

	@limit_speed
	def v_down(self,step=10):
		self.__velocity -= step
		#self.limit_speed()

	@limit_speed
	def gas(self): 
		self.v_up()		
		#self.limit_speed()

	@limit_speed
	def stop(self):
		self.__velocity=0
		#self.limit_speed()

	def get_speed(self):
		return self.__velocity

	# remove decorator
	del limit_speed


class Electo(Vehicle):

	def __init__(self,model, color='white', velocity=0, battery_level=0):
		super().__init__(model, color, velocity)
		self.battery_level=battery_level

		

red_car = Vehicle('bmw', 'red', 280)

red_car.v_up()
red_car.v_up()
print(red_car.get_speed())

red_car.stop()
red_car.v_down()
print(red_car.get_speed())

electo_car=Electo('li', 'black', 380, 100)
print(electo_car.__dict__)