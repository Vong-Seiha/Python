# userInput = int(input("please input ur age: "))
# if userInput >= 18:
#     print("You are eligible to vote")
# elif userInput <= 0:
#     print("Age must be a positive digit")
# else:
#     print("cant")


# nameInput = input("input ur name: ")
# times = int(input("times to print: "))
# if nameInput == "":
#     print("no name entered")
# else:
#     for i in range(times):
#         print(nameInput)

# userInput = input("input number: ")
# if userInput.isdecimal():
#     int_user = int(userInput)
#     if int_user / 2 == 0:
#         print("even number")
#     else:
#         print("odd number")
# else:
#     print("not a valid number")

# sum = 0
# while True:
#     userInput = input("input a number: ")
#     if userInput == "stop":
#         break
#     if userInput.isdecimal():
#         int_user = int(userInput)
#         sum += int_user
#     else:
#         print("the input must be a number")
# print(sum)

# oddSum = 0
# evenSum = 0
# userInput = input("input a number: ")
# if userInput.isdecimal():
#     # int_user = int(userInput)
#     for i in range(int(userInput)+1):
#         if i % 2 == 0:
#             evenSum += i
#         else:
#             oddSum += i
#     print(f"Sum of even numbers: {evenSum}")
#     print(f"Sum of odd numbers: {oddSum}")
# else:
#     print("invalid input")
#     print("Sum of odd numbers = 0")
#     print("Sum of even numbers = 0")

# userInput = input("input a number: ")
# evenSum = 0
# oddSum = 0
# count_odd = 0
# count_even = 0
# if userInput.isdecimal():
#     for i in range(int(userInput)+1):
#         if i % 2 == 0:
#             evenSum += i
#             count_even += 1
#         else:
#             oddSum += i
#             count_odd += 1
#             print(count_odd,count_even)
    

    
#     print(evenSum)
#     print(oddSum)
#     print(f"average of evennum: {evenSum//count_even}")
#     print(f"average of oddnum: {oddSum//count_odd}")
# else:
#     print("invalid number")

# import random
# print(random.randint(5,10))

# import random
# userInput = int(input("input number: "))
# sum = 0
# for i in range(userInput):
#     random_num = random.randint(2000,3000)
#     sum += random_num
# print(sum)

# userInput = input("enter a string: ")
# if userInput =='':
#     print("the string is empty")
# else:
#     print(len(userInput))

# userInput = input("input a string: ")
# h1 = userInput[:len(userInput)//2]
# h2 = userInput[len(userInput)//2:]
# print(h1,h2)
# if userInput == '':
#     print("nth")

# userInput = input("")
# print(userInput.lower())
# print(userInput.upper())

# userInput = input("")
# h1 = userInput[:len(userInput)//2-1:-1]
# h2 = userInput[len(userInput)//2:]
# # print(h1.upper() , h2.lower())
# print(h1+h2)

# userInput = input("")
# for i in userInput:
#     asci = ord(i)
#     print(f"{i} : {asci}")


# userInput = input("input: ")
# new_string = ""
# for i in range(len(userInput)):
#     if userInput[i].isupper():
#         new_string += userInput[i].lower()
#     else:
#         new_string += userInput[i].upper()
# print(new_string)

# while True:
#     print("press 1 to encode")
#     print("press 2 to decode")
#     press = int(input(""))
#     if press == 1 :
#         word1 = input("enter the string to encode: ")
#         deword = ""
#         for word1 in word1:
#             word1 = ord(word1)
#             if word1 >= 65 and word1 <= 77 or word1 >= 97 and word1 <= 109:
#                 word1 += 13
#                 word1 = chr(word1)
#                 deword += word1
#             elif word1 >= 78 and word1 <= 90 or word1 >= 110 and word1 <= 122:
#                 word1 -= 13
#                 word1 = chr(word1)
#                 deword += word1
#         print(f'the decode text is: {deword}')
#     else:
#         word1 = input("enter the string to decode: ")
#         deword = ""
#         for word1 in word1:
#             word1 = ord(word1)
#             if word1 >= 65 and word1 <= 77 or word1 >= 97 and word1 <= 109:
#                 word1 += 13
#                 word1 = chr(word1)
#                 deword += word1
#             elif word1 >= 78 and word1 <= 90 or word1 >= 110 and word1 <= 122:
#                 word1 -= 13
#                 word1 = chr(word1)
#                 deword += word1
#         print(f'the decode text is: {deword}')
#     print("Do you want to continue?[Y/N]")
#     next = input("")
#     if next == "N":
#         break

# while True:
#     print("press 1 to encode")
#     print("press 2 to decode")
#     press = input("")
#     if press == 1:
#         word1 = input("enter string to decode: ")
#         deword = ""
#         for word1 in word1:
#             word1 = ord(word1)
#             if word1 >= 65 and word1 <= 77 or word1 >= 97 and word1 <= 109:
#                 word1 += 13
#                 word1 = chr(word1)
#                 deword += word1
#             elif word1 >= 78 and word1 <= 90 or word1 >= 98 and word1 <= 122:
#                 word1 -= 13
#                 word1 = chr(word1)
#                 deword += word1
#         print(f'the decode text is: {deword}')
#     else:
#         word1 = input("enter string to decode: ")
#         deword = ""
#         for word1 in word1:
#             word1 = ord(word1)
#             if word1 >= 65 and word1 <= 77 or word1 >=97 and word1 <= 109:
#                 word1 += 13
#                 word1 = chr(word1)
#                 deword += word1
#             elif word1 >= 78 and word1 <= 90 or word1 >= 98 and word1 <= 122:
#                 word1 -= 13
#                 word1 = chr(word1)
#                 deword += word1
#         print(f'the decode text is: {deword}')
#     print("Do you want to continue?[Y/N]")
#     next = input("")
#     if next == "N":
#         break





# import random
# def random_tuple(num):
#     sum = 0
#     lst = []
#     for i in range(num):
#         random_num = random.randint(0,100)
#         sum += random_num
#         lst.append(random_num)
#         print(f'random number {i+1}: {random_num}')
#     print(tuple(lst))
#     return sum
# print(random_tuple(5))

# def sum_of_list(lst):
#     return sum(lst)
# print(sum_of_list([20,15,10,30]))

# def search_in_tuple(tup,ind):
#     if ind in tup:
#         return f"element found at index: {tup.index(ind)}"
#     else:
#         return "element not found at index"
# print(search_in_tuple((20,15,10,30),212))

# def mean_of_list(lst):
#     lst_sum = sum(lst)
#     avg = lst_sum/len(lst)
#     return avg
# print(mean_of_list([50,10,62,32]))

# def slice_list(lst,slc):
#     return lst[slc:-slc]
# print(slice_list([50,10,62,32,64,78,90],2))

# def make_dict(givenlst,giventuple):
#     my_dict = {}
#     for i in givenlst:
#         for j in giventuple:
#             my_dict[i] = j
#     return my_dict
# print(make_dict([50,10,62],("china","kimhour","rith")))


# def dict_value(dict):
#     count = 1
#     for key,val in dict.items():
#         print(key,":", *val)
#         if count != len(dict):
#             print("*" * 50)
#             count += 1
# (dict_value({
#             120: ("Visal", "Borey", "Sovann"),
#             130: ("Hout","Mouyleng","Pidor"),
#             140: ("Nary", "Misora", "Masaaki"),     
#             })) 