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