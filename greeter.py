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
def describe_pet( animal_name, animal_type = 'dog'):
    """注释 描述函数是做什么的 三引号"""
    print("my pet is  " + animal_type.title() + "his name is " + animal_name.title())
describe_pet(animal_name = "feifei"  )
describe_pet('弟弟')