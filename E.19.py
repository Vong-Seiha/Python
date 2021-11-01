# userInput = input("Enter a string: ")
# new_str = ""
# for i in range(len(userInput)):
#     if userInput[i].isupper():
#         new_str += userInput[i].lower()
#     elif userInput[i].islower():
#         new_str += userInput[i].upper()
#     else:
#         new_str += userInput[i]
# print(new_str)

userInput = input("Enter a string: ")
new_str = ""
for i in range(len(userInput)):
    if userInput[i].isupper():
        new_str += userInput[i].lower()
    else:
        new_str += userInput[i].upper()
print(new_str)