total = 0
while True:
    userInput = input("Enter a number: ")
    if userInput == "stop":
        break
    else:
        if userInput.isdecimal():
            total += int(userInput)
        else:
            print("The input must be a valid number")


print(f'Sum of total: {total}')