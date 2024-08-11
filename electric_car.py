from car import Car
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