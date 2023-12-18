print("Hello World")

message = "Hello World Again nice"
print(message)

print("title测试" + message.title())
print("lower test " + message.lower())
print("upper test " + message.upper())

good_message = message + "Good"
print(good_message)

# 制表符打出空白
print("\tFirstTest")

# 换行符
print("One\nTwo\nThree")

print("One\nTwo\n\tThree")


# 删除结尾空白字符
like_message = 'python '
print(like_message)
print(like_message.rstrip())

# 剔除开头空白字符
dislike_message = ' java'
print(dislike_message)
print(dislike_message.lstrip())