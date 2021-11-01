userInput = input("enter a string: ")
half1 = userInput[:len(userInput)//2]
half2 = userInput[len(userInput)//2:]
print(half1,half2)
if userInput == '':
    print('there is no string')