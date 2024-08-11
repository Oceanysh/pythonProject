from car import Car
from electric_car import ElectricCar
"""导入多个模块"""
bmw = Car('bmw', 'x5', '2018')
print(bmw.get_descriptive_name())

tesla = ElectricCar('TESLA', 'MODELY', '2017')
print(tesla.get_descriptive_name())