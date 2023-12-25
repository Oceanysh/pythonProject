# 第五章 if语句练习

# 5.1
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
     print(car.upper())
    else:
        print(car.title())

if 'bmw' in cars:
    print('in 判断列表是否包含某元素')

if 'bench' not in cars:
    print('not in  判断列表是否不包含某元素')



fruit = 'apple'
if fruit != 'banana':
    print('水果不相等')

age = 22
if age < 25 :
    print('判断数字')

# 5。25 检查多个条件
if (age > 21) and (fruit == 'apple'):
    print('and 连接判断多个条件')

if (age > 22) or (fruit == 'apple'):
    print('or 连接判断多个条件')

