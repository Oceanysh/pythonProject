# “2-3 个性化消息：
#  将用户的姓名存到一个变量中，并向该用户显示一条消息。显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”。
#
name = "Neri"
print("Hello Neri, would you like to learn some Python today?")
# 2-4 调整名字的大小写：
#  将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
#
print(name.lower())
print(name.upper())
print(name.title())
# 2-5 名言：
#  找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
# Albert Einstein once said, “A person who never made a mistake never tried anything new.”
#
print("Albert Einstein once said, “A person who never made a mistake never tried anything new.”")
# 2-6 名言2：
#  重复练习2-5，但将名人的姓名存储在变量famous_person
#  中，再创建要显示的消息，并将其存储在变量message
#  中，然后打印这条消息。
#
name = "Albert Einstein"
message = "“A person who never made a mistake never tried anything new.”"
print(name + " once said, " + message)
# 2-7 剔除人名中的空白：
#  存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t"
#  和"\n"
#  各一次。”
#
name = "\tAlbert Einstein\t\n"
print(name)
# 摘录来自
# Python编程：从入门到实践
# [美] Eric Matthes
# 此材料可能受版权保护。