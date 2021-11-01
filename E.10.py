import random
userInput = int(input("input the number: "))
sum = 0
for i in range(userInput):
    random_number = random.randint(2000,3000)
    if random_number % 2 == 0:
        sum += random_number
    print(sum)