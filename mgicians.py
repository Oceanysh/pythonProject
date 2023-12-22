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

# 创建前10个整数的平方
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

    print(squares)

# 简洁写法
two_squares = []
for value in range(1, 11):
    two_squares.append(value**2)

    print(two_squares)

# 列表解析
three_squares = [value**2 for value in range(1,11)]
print(three_squares)

# 4-3 到 4-9
# “4-3 数到20：使用一个for循环打印数字1~20（含）。”
for value in range (1,21):
    print(value)
# “4-4 一百万：创建一个列表，其中包含数字1~1 000 000，
# 再使用一个for循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。”

million_squares = [value for value in range (1,1000001)]
print(million_squares)

# 4-5 算总和
print(sum(million_squares))

# 4-6 找奇数
for value in range(1,20,2):
    print(value)

# 4-7 3的倍数
for value in range(3,31,3):
    print(value)

# 4-8 立方 4-9
lifang_squares = [value**3 for value in range(1,11)]
print(lifang_squares)


