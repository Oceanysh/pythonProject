# 第八章
# def greet_user():
#     """注释 描述函数是做什么的 三引号"""
#     print("hello")
# greet_user()

# def greet_user(username):
#     """注释 描述函数是做什么的 三引号"""
#     print("hello, " + username.title())
# greet_user("john")

# def display_message(username):
#     """注释 描述函数是做什么的 三引号"""
#     print("I learn , " + username.title())
# display_message("hanshu ")


# 位置实参
# def describe_pet(animal_type, animal_name):
#     """注释 描述函数是做什么的 三引号"""
#     print("my pet is  " + animal_type.title() + "his name is " + animal_name.title())
# describe_pet(" dog " , "feifei")
# describe_pet(" cat " , "zhishangfeifei")

# 关键字实参
# def describe_pet(animal_type, animal_name):
#     """注释 描述函数是做什么的 三引号"""
#     print("my pet is  " + animal_type.title() + "his name is " + animal_name.title())
# describe_pet(animal_name = "feifei", animal_type = " dog " )
# describe_pet(" cat " , "zhishangfeifei")

# 关键字
# 由于给animal_type指定了默认值， 无需通过实参来指定动物类型，因此在函数调用中只包含一个实参——宠物的名字。然而，
# Python 依然将这个实参视为位置实参，因此如果函数调用中只包含宠物的名字，这个实参将关联到函数 定义中的第一个形参。
# 这就是需要将pet_name放在形参列表开头的原因所在。
# def describe_pet( animal_name, animal_type = 'dog'):
#     """注释 描述函数是做什么的 三引号"""
#     print("my pet is  " + animal_type.title() + "his name is " + animal_name.title())
# describe_pet(animal_name = "feifei"  )
# describe_pet('弟弟')

# ----------------------------------------------------------------
# 8.3
# def get_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()
# # musician = get_name('fei','ff')
# # print(musician)
# while True:
#     f_name = input('\n enter your first_name')
#     if f_name == 'q':
#         break
#     l_name = input('\n enter your last_name')
#     if l_name == 'q':
#         break
#     print(f_name + ' ' + l_name)


# def get_name(first_name, last_name, age = ''):
#     person = {'first':first_name, "last":last_name, 'age':age}
#     if age:
#         person['age'] = age
#     return person
# musician = get_name('fei','ff')
# jj = get_name('jj', 'aa', 27)
# print(musician)
# print(jj)

# 练习
# def city_country(city, country):
#     print(city + ', ' + country)
# city_country('shanghai', 'china')

# def make_album(singer, album_name, songs_count = ''):
#     album = {'singer':singer, 'album_name':album_name, 'songs_count':songs_count}
#     return  album
# while True:
#         in_singer = input('\nsinger')
#         if in_singer == 'q':
#             break
#         in_album_name = input('\nalbum_name')
#         if in_album_name == 'q':
#             break
#         in_songs_count = input('\nsongs_count')
#         if in_songs_count == 'q':
#             break
#         print('\n enter q can quit')
#         final_album = make_album(in_singer, in_album_name, in_songs_count)
#         print(final_album)


# a_album = make_album('jj', '七里香')
# b_album = make_album('jj', '夜曲', 10)
# print(a_album)
# print(b_album)

# ------------------------------

# 8.4

# 本人
# def show_magicians(names):
#     for name in names:
#         print('nams is ' + name)
# def make_great(names):
#     while names:
#       willgreat_name = names.pop()
#       print('\n this is now add great name' + willgreat_name)
#       names.append('the Great ' + willgreat_name)
#
#
# names = ['aa', 'bb', 'cc']
# make_great( names)
# show_magicians(names)


# claude 提供
# def show_magicians(magicians):
#     """打印魔术师列表中每个魔术师的名字"""
#     for magician in magicians:
#         print(magician)
#
# def make_great(magicians, change_magicians):
#     """修改魔术师列表,在每个魔术师的名字前加上'the Great'"""
#     for i in range(len(magicians)):
#         magicians[i] = "the Great " + magicians[i]
#         change_magicians.append(magicians[i])
#
# # 创建一个包含魔术师名字的列表
# magicians = ["David Copperfield", "Penn Jillette", "Teller", "Dynamo"]
# change_magicians = []
# print("原始魔术师列表:")
# show_magicians(magicians)
# print("原始change_magicians列表:")
# show_magicians(change_magicians)
#
# # 修改魔术师列表
# make_great(magicians[:], change_magicians)
#
# print("\n修改后的魔术师列表:")
# show_magicians(magicians)
# print("\n修改后的change_magicians列表:")
# show_magicians(change_magicians)

# 8-11 不变的魔术师 本人根据claude提供的8-9 8-10基础上修改

# ----------------------------------------------------

# 8.5

# def sandwiches(*topping):
#     print('\n this is your want sandwich')
#     for top in topping:
#         print('- ' + top)
# sandwiches('bread', 'meat', 'tomato')
#
#
# def build_profile(first, last, **user_info):
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile['first_name'] = first
#     profile['last_name'] = last
#     for key, value in user_info.items():
#         profile[key] = value
#     return profile
#
# user_profile = build_profile('albert', 'einstein', location='princeton',field='physics',age= '18')
# print(user_profile)


def make_car(zhizaoshang, size, **topping):
    car = {}
    car['zhizaoshang'] = zhizaoshang
    car['size'] = size
    for key, value in topping.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
