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
    'amy': 'Java',
    'luck': 'c'
}
print('amy favorite language is ' +
    favorite_languages['amy'])

# 遍历该语言
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite_language is " +
          language.title())

print("====================")
print("====================")

# 遍历key
for name in favorite_languages.keys():
    print(name.title())
print("====================")
print("====================")
# 可以不写显示的.keys()
for name in favorite_languages:
    print(name.title())
# 用keys()检查
if 'leslie' not in favorite_languages.keys():
    print("please commit leslie!")
print("====================")
print("====================")
# 顺序遍历key
for name in sorted(favorite_languages.keys()):
    print(name.title())
print("====================")
print("遍历所有值")
for language in favorite_languages.values():
    print(language.title())
print("====================")
print("遍历所有值并用 set 剔除重复项")
for language in set(favorite_languages.values()):
    print(language.title())


print("====================")
print("创建应该会接受调查的名单，遍历此名单，感谢已经参加的，邀请未参加的")
friends = ['jen', 'john', 'kanye']
for friend in friends:
    if friend in favorite_languages.keys():
        print(friend + " thank you come")
    else:
        print(friend + " welcome come")
print("====================")
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(name + " thank you come")
    else:
        print(name + " welcome come")




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

# 6.3 遍历字典
for key, value in neri.items():
    print("\nkey: " + key)
    print("value: " + str(value))

# 6.3 课后练习

rivers = {
    'nile': 'egypt',
    'china': 'huanghe',
    'china': 'changjiang',
    'american': 'mxxbh'
}

for country, name in rivers.items():
    print('The ' + name.title() + ' run through ' + country.title())
# 打印河流名字 两个china的key，打印了最后一个value
for river_name in rivers.values():
    print("河流名字是 " + river_name)
# 打印国家 两个china 同样只打印了一个
for river_country in rivers:
    print("河流所在国家是：" + river_country)
