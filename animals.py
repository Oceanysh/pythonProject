# 第三章列表练习
animals = ['cat', 'dog', 'rat', 'elephant']
print(animals)
print(animals[0])
print(animals[1].title())

# 特殊索引 -1 返回最后一个元素 ；-n,返回倒数第n个元素
print(animals[-1])

print(animals[-3])

print(animals[1].title() + " is my favorite animal")

# 修改列表元素
animals[0] = 'lion'
print(animals)
# 添加列表元素
animals.append('cat')
print(animals)
# 创建空列表
animals_empty = []
print(animals_empty)
# insert方式增加元素
animals_empty.insert(0, 'dog')
animals_empty.insert(2, 'snake')
print(animals_empty)
# 为何直接添加2索引没有报错，输出时报错了?
print(animals_empty[1])
# del 删除元素
del animals[3]
print(animals)
# pop 删除元素
popped_animals = animals.pop()
print(popped_animals)
print(animals)
# 弹出任意位置的元素
first_animal = animals.pop(0)
print(first_animal)

# remove根据值删除元素
remove_animal = 'dog'
animals.remove(remove_animal)
# 不可以直接animals.remove('dog') 这样输出的是None
print(remove_animal)
print(animals)

# 3.2练习题
# 3-4
persons = ['john','mike','kobe','james','amy']
print(persons)
# 3-5
print(persons[0].title() + "\tcan't come")
cant_come_person = 'john'
persons.remove(cant_come_person)
print(persons)
persons.insert(0,'nash')
print(persons)
# 3-6
persons.insert(0,'booker')
persons.insert(3,'harden')
persons.append('george')
print(persons)
# 3-7
persons.pop(0)
persons.pop(0)
persons.pop(0)
persons.pop(0)
persons.pop(0)
persons.pop(0)
print(persons)
del persons[0]
del persons[0]
print(persons)