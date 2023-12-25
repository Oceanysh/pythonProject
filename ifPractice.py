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

car = 'bench'
print('is car == bench i think is ture')
print(car == 'bench')
print('\nis car == audi i think is false')
print(car == 'audi')

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

# 5.2课后练习
number_flag = 2
if number_flag == 1:
    print('判断为 true')
else:
    print('判断为 false')

zz = 'now'
if zz.title() == 'Now':
    print('title test')
if zz.lower()== 'Now':
    print('title test')
else:
    print('\nlower test not pass')

if 'honqi' not in cars:
    print('not in again')
elif 'audi' in cars:
    print('in again')

if 'audi' in cars:
    print('in again')

# 5。3课后练习
alien_color = 'green'
if alien_color == 'green':
    print('you get five point')

if alien_color == 'green':
    print('you get five point')
else:
    print('you get 10 point')


if alien_color == 'green':
    print('you get five point')
elif alien_color == 'yellow':
    print('you get 10 point')
elif alien_color == 'red':
    print('you get 15 point')

age = 25
if age < 2 :
    print('he is baby')
elif 2 <= age <= 4 :
    print('he study walk')
elif 4 < age <= 13 :
    print('he is a chlidren')
elif 13 < age <= 20 :
    print('he is a teenager')
elif 20 < age <= 65 :
    print('he is a adult')
elif 65 < age :
    print('he is a oldman')

fruits = ['apple', 'orange', 'banana']
if 'apple' in fruits:
    print('in here')
if 'peach' in fruits:
    print('\npeachein here')



# 5。4
for fruit in fruits:
    if fruit == 'apple':
        print('is tough')
    else:
        print('is soft')

favorite_fruits = []
if favorite_fruits:
    print('jj')
    for fruit in favorite_fruits:
        print('aa')
else:
    print('bb')

avaiable_fruits =  ['apple', 'orange', 'banana']
requested_fruits =  ['apple', 'orange']
for fruit in requested_fruits:
    if fruit in avaiable_fruits:
        print('you can buy it')
    else:
        print("you can't buy it")

# 5.5课后练习

names = ['admin', 'david', 'john', 'amy', 'neri']
for name in names:
    if name == 'admin':
        print('hello admin')
    else:
        print('hello ' + name + 'welcome')

names = []
if names:
  for name in names:
    if name == 'admin':
        print('hello admin')
    else:
        print('hello ' + name + 'welcome')
else:
    print('we need to find some uers')

current_names = ['kat', 'bob', 'lucy', 'bruce', 'nick']
new_users =  ['Kat', 'david', 'john', 'bruce', 'neri']

for user in new_users:
    if user.lower() in  current_names:
        print('current_name ' + user)
    else:
        print('name not use')

number_ten = ['1','2','3','4','5','6','7','8','9','10']
for num in number_ten:
    if num == 1:
        print('\n1st')
    elif num == 2:
        print('\n2nd')
    elif num == 3:
        print('\n3rd')
    else:
        print(num + 'th')
# print(num + 'th') number_ten为int类型数组时
# 输出报错TypeError: unsupported operand type(s) for +: 'int' and 'str'
