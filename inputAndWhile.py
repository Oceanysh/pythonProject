# 第七章

# message = input("please tell me something： ");
# print(message)

# prompt = " please tell me ";\
# prompt += "\nyour name:";
# newprompt = input(prompt);
# print(newprompt)


# string转int
# prompt = " please tell me ";\
# prompt += "\nyour height: ";
# newprompt = input(prompt);
# newprompt = int(newprompt)
# if newprompt > 20:
#     print("\n you are good")
# else:
#     print("\n you are bad")

# 求模运算

# number = input("oushu or jishu");
# number = int(number)
# if number % 2 == 0:
#     print("\n oushu")
# else:
#     print("\n jishu")

# 7.1 practice
# car = input("Let me see if I can find you a ");
# print(car)

# eatperson = input("how many person eat ")
# eatperson = int(eatperson)
# if eatperson > 8 :
#     print("no table")
# else:
#     print("have table")

# number = input("write number ")
# number = int(number)
# if number % 10 == 0:
#     print("\n10 de zhengshu")
# else:
#     print("\nnot 10 de zhengshu ")

# -------------------------------------

# 7.2
# current_number = 1;
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# message = "please say something";
# message = "\nif say quit while exit "
# middle_message = ""
# while middle_message != 'quit':
#     middle_message = input(message)
#     if middle_message != 'quit':
#         print(middle_message)

# 标志 true false
# message ="";
# active = True
# while active:
#     middle_message = input(message)
#     if middle_message == 'quit':
#         active = False
#     if middle_message != 'quit':
#         print(middle_message)

# break
# message ="";
# active = True
# while active:
#     middle_message = input(message)
#     if middle_message == 'quit':
#        break
#     if middle_message != 'quit':
#         print(middle_message)

# continue
# current_number = 0;
# while current_number <= 10:
#     current_number += 1
#     # 忘记写if
#     if current_number % 2 == 0:
#      continue
#     print(current_number)

# x = 1
# while x < 5:
#     print(x)
#     x += 1

# 7.2 practice
# pizza_message = "please say something you want in pizza: "
# message = ""
# active = True
# while active:
#     message = input(pizza_message)
#     if message == 'quit':
#         active = False
#         break
#     if message != 'quit':
#         print(message)
pizza_toppings = []
print("欢迎使用披萨配料选择器!")
print("请输入你想要的披萨配料,每次一种。输入'quit'结束。")

while True:
    message = input("请输入一种披萨配料: ").lower()
    if message == 'quit':
        break
    pizza_toppings.append(message)
    print(f"已添加 {message} 到你的披萨中。")

print("\n你的披萨配料包括:")
for topping in pizza_toppings:
    print(f"- {topping}")
print("谢谢使用,祝你的披萨美味!")

# movie_message = "your cost for movie depends on your age: "
# while movie_message != '':
#     movie_message = input(movie_message)
#     movie_message = int(movie_message)
#     if movie_message < 3:
#         print("under 3 is free")
#     if 3 < movie_message < 12:
#         print("you need 10")
#     if 12 < movie_message:
#         print("you need 15")

# x =1
# while x < 5:
#     print(x)

# ----------------------------------------------

# 7.3
# unconfirmed_users = ['bob', 'alice', 'john']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("now confirm is " + current_user.title())
#     confirmed_users.append(current_user)
# 没有用for处理
# for confirmed_user in confirmed_users:
#     print('\n now ' + confirmed_user)


# pets = ['dog', 'cat', 'mouse', 'dog', 'dog']
# print(pets)
# while 'dog' in pets:
#     pets.remove('dog')
# print(pets)

# reponses = {}
# active = True
# while active:
#     name = input("\nwhat's your name? ")
#     reponse = input("\nwhat food you like? ")
#     reponses[name] = reponse
#     repeat = input("anyone want to say? yes/no")
#     if repeat == 'no':
#         active = False
# print('\n=================')
# for name, reponse in reponses.items():
#     print(name + " wants " +  reponse)

# 课后练习
# sandwich_orders = ['aa', 'bb', 'cc']
# finished_sandwiches = []
# while sandwich_orders:
#     finished_sandwiche = sandwich_orders.pop()
#     print( ' I made your '+ finished_sandwiche + ' sandwich')
#     finished_sandwiches.append(finished_sandwiche)
# print(finished_sandwiches)

# sandwich_orders = ['aa', 'bb', 'cc', 'pastrami', 'pastrami', 'pastrami']
# print('\n pastrami is sell out')
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

# places = {}
# actice = True
# while actice:
#     name = input("\nwhat's your name? ")
#     place = input("\nIf you could visit one place in the world, where would you go? ")
#     places[name] = place
#     repeat = input("anyone want say yes/no")
#     if repeat == 'no':
#         actice = False
# print("\n======================")
# for name, place in places.items():
#     print(name + ' want to go ' + place)
