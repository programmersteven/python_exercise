numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)
max_number = max(numbers)
min_number = min(numbers)
sum_number = sum(numbers)
length = len(numbers)
first_number = numbers[0]
last_number = numbers[length - 1]
average_number = sum_number / length
print("The first number is {}".format(first_number))
print("The last number is {}".format(last_number))
print("The smallest number is {}".format(min_number))
print("The largest number is {}".format(max_number))
print("The average of the numbers is {}".format(average_number))


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
             'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
user_names = input("Please input your name: ")
if user_names in usernames:
    print("Access granted")
else:
    print("Access denied")




