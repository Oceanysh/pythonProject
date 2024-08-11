from collections import OrderedDict
from random import randint
"""练习python标准库"""
favorite_language = OrderedDict()
favorite_language['JEN'] = 'Python'
favorite_language['SARAH'] = 'Java'
print(favorite_language)

class Die():
    """随机面数的骰子"""
    def __init__(self, sides = 6):
        """默认面数是6"""
        self.sides = sides
    def roll_die(self):
        for _ in range(10):
            print(randint(1, self.sides))

die = Die(10)
die.roll_die()


