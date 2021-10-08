import random
number = int(input("How many quick picks? "))
count = 0
for i in range(number):
    numbers = []
    for j in range(6):
        j = random.randint(1, 45)
        while j in numbers:
            j = random.randint(1, 45)
        numbers.append(j)
    numbers.sort()
    for j in numbers:
        print(j,end=" ")
    print()





