userInput = input("input the number: ")
evenSum = 0
oddSum = 0
count_even = 0
count_odd = 0
if userInput.isdecimal():
    for i in range(int(userInput)+1):
        if i % 2 == 0:
            evenSum += i
            count_even += 1
        else:
            oddSum += i
            count_odd += 1
    print(f'average even:{evenSum/count_even}')
    print(f'average odd: {oddSum/count_odd}')
else:
    print("not a valid number")
