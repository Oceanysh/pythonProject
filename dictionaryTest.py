# 第六章 字典
# 注意是花括号 首次写时 写为方括号了
alien_0 = {'color': 'green','point': 5}
# 获取键-值对
print(alien_0['color'])
print(alien_0['point'])
new_point = alien_0['point']
print('you just get ' + str(new_point) + ' points')

# 添加键-值对
alien_0['x_pisition'] = 0
alien_0['y_pisition'] = 25
print(alien_0)

# 创建空字典
alien_1 = {}
print(alien_1)
alien_1['bmw'] = 'black'
print(alien_1)
alien_1['bmw'] = 'white'
print(alien_1)

# 跟踪外星人移动轨迹
alien_2 = {'x_position': 0 , 'y_position': 20, 'speed': 'medium'}
print('orginal x_position: ' + str(alien_2['x_position']))
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else :
    x_increment = 3
alien_2['x_position'] = alien_2['x_position'] + x_increment
print('new x_position: ' + str(alien_2['x_position']))

#  彻底删除某字典值
del alien_2['speed']
print(alien_2)

# 类似对象组成字典
favorite_languages = {
    'jen': 'python',
    'john': 'c',
    'mike': 'rust',
    'amy': 'Java'
}
print('amy favorite language is ' +
    favorite_languages['amy'])


# 课后练习
neri = {
    'first_name': 'neri',
    'last_name': 'young',
    'age': 23,
    'city': 'beijing'
}
print('his first_name is '+
      neri['first_name'].title() +
      '\nhis last_name is '+
      neri['last_name'].title() +
      '\nhis age is '+
      str(neri['age']) +
      '\nhis city is '+
      neri['city'])

