# with open('pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     for line in file_object:
#       print(line.rstrip())

# with open('pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     lines = file_object.readlines()
# for line in lines:
#       print(line.rstrip())
#
# with open('pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     lines = file_object.readline()
# for line in lines:
#       print(line.rstrip())


# with open('pi_digits.txt') as file_object:
#     # contents = file_object.read()
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#      pi_string += line.strip()
# print(pi_string)
# print(len(pi_string))
# print(pi_string[:3])
#
# birthday = input('enter your birthday')
# if birthday in pi_string:
#     print('include')
# else:
#     print('not include')

with open('learning_python.txt') as learn:
      concent =  learn.read()
      print(concent)
print('------------------------------------------------------')
with open('learning_python.txt') as learn:
    concent = learn.readlines()
pu_string = ''
for line in concent:
    print(line)
