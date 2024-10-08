# 第九章

class Dog():
    """小狗类"""

    def __init__(self, name, age):
        """include nam age"""
        self.name = name
        self.age = age

    def sit(self):
        """会蹲下"""
        print(self.name.title() + ' is now sitting')

    def dagun(self):
        """会打滚"""
        print(self.name.title() + 'dagun')

# -----------------------------

# 创建实例
my_dog = Dog('JOHN', 10)
print('my dog name is ' + my_dog.name.title())
print('my dog age is ' + str(my_dog.age))
my_dog.sit()
my_dog.dagun()

# ---------------

# practice

class Restaurant():
    """饭店"""
    def __init__(self, restaurant_name, cuisine_type):
        self.cuisine_type = cuisine_type
        self.restaurant_name = restaurant_name

    def describe_restaurant(self):
        """饭店描述"""
        print("cuisine_type is " + self.cuisine_type.title())
        print('restaurant_name is ' + self.restaurant_name)

    def open_restaurant(self):
        """营业状态"""
        print('this restaurant is open')

nmsr = Restaurant("nanmenshuanrou", "huoguo")
print(nmsr.restaurant_name)
print(nmsr.cuisine_type)
nmsr.describe_restaurant()
nmsr.open_restaurant()

# --------------------------------------

class User():
    def __init__(self, first_name, last_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    def describe_user(self):
        print('user firstname is ' + self.first_name)
    def greet_user(self):
        print('hello!')
feifei = User('fei', 'fei', 12)
print(feifei.first_name)
print(feifei.last_name)
print(feifei.age)

# -------------------------

# 9.2
# 练习
class Restaurant():
    """饭店"""
    def __init__(self, restaurant_name, cuisine_type):
        self.cuisine_type = cuisine_type
        self.restaurant_name = restaurant_name
        self.number_served = 10

    def describe_restaurant(self):
        """饭店描述"""
        print("cuisine_type is " + self.cuisine_type.title())
        print('restaurant_name is ' + self.restaurant_name)

    def open_restaurant(self):
        """营业状态"""
        print('this restaurant is open')

    def set_number_served(self, numeber):
        self.number_served = numeber

    def increment_number_served(self, incre_number):
        self.number_served += incre_number
nmsr = Restaurant("nanmenshuanrou", "huoguo")
nmsr.number_served = 10
nmsr.set_number_served(20)
nmsr.increment_number_served(50)
print(nmsr.restaurant_name)
print(nmsr.cuisine_type)
print('有' + str(nmsr.number_served) + '人在这里就餐')
nmsr.describe_restaurant()
nmsr.open_restaurant()

# ---------------------------------------------------

class User():
    def __init__(self, first_name, last_name, age, login_attempts):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.login_attempts = login_attempts
    def describe_user(self):
        print('user firstname is ' + self.first_name)
    def greet_user(self):
        print('hello!')
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(self.login_attempts)
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(self.login_attempts)

feifei = User('fei', 'fei', 12, 2)
print(feifei.first_name)
print(feifei.last_name)
print(feifei.age)
feifei.increment_login_attempts()
feifei.reset_login_attempts()

# ---------------------------------------------
# 9.3

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        """初始化父类属性"""
        super().__init__(restaurant_name, cuisine_type)
        """添加一个名为 flavors 的属性，用于 存储一个由各种口味的冰淇淋组成的列表。"""
        self.flavors = []
    def show_flavors(self):
        """编写一个显示这些冰淇淋的方法。"""
        if self.flavors:
            print("冰淇淋有：" + ", ".join(self.flavors))
        else:
            print("目前没有冰淇淋")
    def add_flavors(self, flavors):
        self.flavors.append(flavors)

ice = IceCreamStand('hagendasi', 'icecream')
ice.add_flavors('aa')
ice.add_flavors('bb')
ice.show_flavors()

# ------------------------------------------------


class Privileges():
    def __init__(self,privileges = []):
        self.privileges = privileges
    def show_privileges(self):
        if self.privileges:
            print('权限有： ' + '，'.join(self.privileges))
        else:
            print('没权限')
    def add_privileges(self, privileges):
        self.privileges.append(privileges)


class Admin(User):
    def __init__(self, first_name, last_name, age, login_attempts ):
        super().__init__( first_name, last_name, age, login_attempts )
        self.privileges = Privileges()



admin = Admin('fei', 'fei', '12', 'aa')
admin.privileges.add_privileges('can add post')
admin.privileges.add_privileges('can delete post')
admin.privileges.add_privileges('can ban user')
admin.privileges.show_privileges()

# ------------------------------------------------


class Car():
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            return long_name.title()

    def read_odometer(self):
            print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
            self.odometer_reading += miles

class Battery():
    """sssss"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """检查电瓶容量，如果它不是 85，就将它设置为 85"""
        if self.battery_size != 85:
            self.battery_size = 85
        print('now battery_size is ' + str(self.battery_size))


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_LiXiang = ElectricCar('LiXiang', 'L9', '2022')
my_LiXiang.battery.get_range()
print(my_LiXiang.odometer_reading)
print(my_LiXiang.get_descriptive_name())
my_LiXiang.battery.upgrade_battery()
my_LiXiang.battery.describe_battery()
my_LiXiang.battery.get_range()

# -----------------------------------------------------------------------------

# 9.4

