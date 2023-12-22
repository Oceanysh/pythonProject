# 第四章内容 操作列表
# for 遍历列表
magicians = ['david', 'neri', 'bob']
for magician in magicians : print(magician)
for magician in magicians :
    print(magician.title() + ", this good ")
    print("I can't wait " + magician.title() + '\n')

# 注意格式，下面错误写法（没有缩进）导致输出一次
for magician in magicians :print(magician.title() + ", this good ")
print("I can't wait " + magician.title() + '\n')


# 4-1 4-2
animals = ['cat', 'dog', 'rat', 'elephant']
for animal in animals:
    print("打印每种动物" + animal)
    print(animal + "，is cute!")
print('I really like animal')

# 4.3 创建数值列表
for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

# 打印1～10偶数
even_numbers = list(range(2,11,2))
print(even_numbers)