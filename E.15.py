userInput = input("input string: ")
half1 = userInput[:len(userInput)//2]
half2 = userInput[len(userInput)//2:]
h1upper = half1.upper()
h2lower = half2.lower()
print(h1upper , h2lower)