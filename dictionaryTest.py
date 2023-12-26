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
print("==============================================")


# 6.4嵌套 列表里嵌套字典 字典里嵌套列表
aliens = [alien_0, alien_1, alien_2]
print(aliens)

# 创建一个存储外星人的空列表
now_aliens = []
# 创建30个外星人
for alien_number in range(30):
    new_alien = {'color': 'green','point': 5,'speed':'slow'}
    now_aliens.append(new_alien)
print(now_aliens)
# 显示前3个外星人
for three_alien in now_aliens[ :3]:
    print(three_alien)
# 显示创建多少个外星人
print(str(len(now_aliens)))

for alien in now_aliens[0:5]:
    if alien['color'] == 'green':
        print('test')
        alien['color'] = 'red'
        alien['speed'] = 'fast'
for alien in now_aliens[0:7]:
    print(alien)

# 字典中存储列表 一个键关联多个值时用到
anmianls ={
    'type' : 'cat-type',
    'name' : ['tiger', 'lion']
}
print(anmianls['name'])

print("==============================================")
# 字典中存储字典

# 6-7
# 创建一个空列表
people = []
# 随机生成3个人的字典
for person in range(3):
    new_person = {'color': 'green','point': 5}
    people.append(new_person)
print(people)

# 6-8
# 创建空列表
pets = []
# 创建字典
cat = {
    'type': 'land',
    'home_name': 'neri'
}
dog = {
    'type': 'land',
    'home_name': 'bruce'
}
pets = [cat, dog]
print(pets)
for pet in pets:
    print('宠物生活环境 ' +
          pet['type'] +
          ' 宠物家的名字 ' +
          pet['home_name'])

print("==============================================")

# 6-9
favorite_places = {
    'neri': ['beijing', 'shanghai'],
    'lucy': 'guangzhou',
    'nick': ['haerbin', 'wuhan', 'lanzhou']
}

# 报错写法 TypeError: list indices must be integers or slices, not str
# for person_name, place in favorite_places.items():
#     print(place['name'] +
#           ", he like " +
#           place['place'])

# 修改后
favorite_places = {
    'neri': ['beijing', 'shanghai'],
    # 'lucy': 'guangzhou', 单值最后也用列表，不然后续 \t 制表符会导致格式不统一
    'lucy': ['guangzhou'],
    'nick': ['haerbin', 'wuhan', 'lanzhou']
}

# 正确写法 可能用列表存储的值，单独用for循环处理
for person_name, places in favorite_places.items():
    print("\n" + person_name.title() +
          ' favorite_places is : ')
    for place in places:
        print("\t" + place.title())

print("==============================================")

# 6-10

person_numbers = {
    'jen': ['1', '2', '4'],
    'john': ['1', '2', '4', '5'],
    'mike': ['1', '2'],
    'amy':  ['1'],
    'luck': []
}
for person_name,person_number in person_numbers.items():
    print(" he/she 's name is " + person_name.title() )
    for number in person_number:
        print(" and he/she 's like " + number)



print("==============================================")
# 6-11
cities = {
    'beijing':{
        'country': 'china',
        'people': '1M',
        'journey': 'The Great Wall'
    },
    'shanghai':{
        'country': 'china',
        'people': '0.5M',
        'journey': 'wai tan'
    },
    'fuzhou': {
        'country': 'china',
        'people': '0.1M',
        'journey': 'dd'
    }
}

for city, city_info in cities.items():
    print('this city is '
          + city +
          ' belongs to ' +
          city_info['country'] +
          'there are ' +
          city_info['people'] +
          ' population ' +
          'recommend place is ' +
          city_info['journey'])

print("==============================================")