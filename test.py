# # name = input("please input your name")
# # age = input("please input your age")
# # print(f'My name is {name} and i am {age}')

# list = [1,2,3,4,5,6,7,8,9]
# x=7
# if x in list:
#     print('false')
# x = 3
# y = 3
# if x==y:
#     print("false")
# elif x>y:
#     print('true')

# list = ["1","2","3"]
# set = {"4","5","6","7"}
# tuple = ("8","9","10","11")
# dict = {"12":"hour","13":"seiha","14":"china","15":"rith"}
# inputnumber = input("please input number:")
# print(inputnumber)
# if inputnumber in list:
#     print('element in list')
# elif inputnumber in set:
#     print('element in set')
# elif inputnumber in tuple:
#     print('element in tuple')
# # else:
# #     print('element in dict')
# elif inputnumber in dict:
#     print('element in dict')

# list = [1,2,3,4,5,6,7,8,9,10]
# set1 = {1,2,3,4,5,6,7,8,9,10}
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# list.extend([11,12,13])
# news = set(list)
# olds = tuple(list)
# print(news)
# print(olds)
# print(list)

# set1 = {1,2,3,4,5,6,7,8,9,10}
# new = tuple(set1)
# print(new)

# array = [1,2,3,4,5,6,7,8,9,9]
# array.insert(7,[1,2,3])
# print(array)

# array = [1,2,3,4,5,6,7,8,9,9]
# array.append('seiha')
# print(array)

# array = [1,2,3,4,5,6,7,8,9,9]
# array.remove(1)
# print(array)

# array = [1,2,3,4,5,6,7,8,9,9]
# count_element = array.count(9)
# print(count_element)
# print(sorted(array,reverse=True))

# array = [1,2,3,4,5,6,7,8,9,9,1,2,3]
# array.sort()
# print(array)

# a = 2
# news = str(a)
# print(news)
# print(type(news))

# a = "15"
# new = int(a)
# print(new)
# print(type(new))

# name = [1,2,3,4,5]
# for i in name:
#     print(i)

# for i in range(0,10):
#     if i == 9:
#         print("true")
#     elif i == 0:
#         print("true")
#     elif i == 7:
#         print("true")
#     else:
#         print("false")

# while True:
# x = 0
# while x < 100:
#     print(x)
#     x += 1

# name = input("please input your name: ")
# age = input("How old are you? ")
# print(f'My name is {name} and I am {age} years old')
       
# list1 = [10,20,30,40,50]
# sum = 0
# for i in list1:
#     sum = sum + i
#     print(sum)

# for i in range(1,21):
#     print(i)
# for i in range(1,101,5):
#     print(i)
# sum = 0
# for i in range(1,21):
#     sum = sum +i
# print(sum)

# list = [10,20,30,40,50]
# x = 10
# for i in list:
#     if i == x:
#         print('found the number')
#         break
#     else:
#         continue
# else:
#     print('number not found')

# list = [10,20,30,40,50]
# x = 100
# for index,value in enumerate(list):
#     # print(index,value)
#     if value == x:
#         print("found the number",index)
#         break
#     else:
#         pass
# else:
#     print("number not found")

# list = [1,2,3,4,5,6,7,8,10,120]
# for i in enumerate(list):
#     print(i)

# a = 10
# b = 20
# print(a*b)

# x = 5
# if x > 2:
#     print('bigger than 2')
#     print('still bigger')
# print('done with 2')
# for i in range(5):
#     print(i)
#     if i > 2:
#         print('done with i',i)
# print('all done')

# x = 30
# if x > 2:
#     print('more than one')
#     if x < 100:
#         print("less than 100")
# print('all done')

# x = 4
# if x > 2:
#     print("bigger")
# else:
#     print("smaller")
# print('all done')

# NumList=[]       #empty list
# evenSum=0        #declare and initialised variable evenSum to sum of even numbers
# oddSum=0         #declare and initialised variable oddSum to sum of odd numbers


# name = input("please input your name: ") 
# age = int(input("Please input your age: "))
# print(f'My name is {name} and I am {age} years old')  

# age = int(input("please input ur age:   "))

# if age >= 18:
#     print("You are eligible to vote")
# elif age < 0:
#     print("age must be positive digt")
# else:
#     print("You aren't adult yet .. sorry can't vote") 

# name = input("please input your name: ")   
# num = int(input("Input number of times to print:"))

# if name == '':
#     print("there is no name")
# else:
#     for i in range(num):
#         print(name)

# num = input("please input the number: ")

# if num.isdecimal():
#     int_num = int(num)
#     if int_num % 2 == 0:
#         print("the number your have entered is even")
#     else:
#         print("the number you have entered is odd")
# else:
#     print("not a valid number")

# total = 0
# while True:
#     userInput = input("please input the number: ")
#     if userInput == "stop":
#         break
#     else:
#         if userInput.isdecimal():
#             total += int(userInput)
#         else:
#             print("not a valid number")
# print(f'sum= {total}')

# userInput = input("pleae input the number: ")
# evenSum = 0
# oddSum = 0
# if userInput.isdecimal():
#     for i in range(int(userInput)+1):
#         if i % 2 == 0:
#             evenSum += i
#         else:
#             oddSum += i
#     print(f'sum of odd number:{evenSum}')
#     print(f'sum of even number:{oddSum}')
        
# else:
#     print("invalid input")
#     print(f'sum of odd number:{evenSum}')
#     print(f'sum of even number:{oddSum}')



# age = int(input("please input your age: "))
# if age >= 18:
#     print("your are good")
# elif age < 0:
#     print("age must be positive")
# else:
#     print("you're underage")

# name = input('please input your name: ')
# times = int(input("please input the times of print: "))
# if name =='':
#     print("no name entered")
# else:
#     for i in range(times):
#         print(name)


# userInput = input("Please input the number: ")
# if userInput.isdecimal():
#     int_input = int(userInput)
#     if int_input % 2 == 0:
#         print("The number u have entered is even")
#     else:
#         print("The number u have entered is odd")
# else:
#     print("not a valid number")


# sum = 0
# while True:
#     userInput = input("please input the number: ")
#     if userInput =="stop":
#         break
#     else:
#         if userInput.isdecimal():
#             sum += int(userInput)
#         else:
#             print("the input must be a valid number ")
# print(f'sum={sum}')

# num = input("please input the number: ")
# oddSum = 0
# evenSum = 0
# if num.isdecimal():
#     for i in range(int(num)+1):
#         if i % 2 == 0:
#             evenSum += i
#         else:
#             oddSum += i
#     print(f'sum of odd number={oddSum}')
#     print(f'sum of odd number={evenSum}')
        
# else:
#     print("invalid input")
#     print("sum of odd number=0")
#     print("sum of odd number=0")

# num = input('please input the number: ')
# oddSum = 0
# evenSum = 0
# count_odd = 0
# count_even = 0
# if num.isdecimal():
#     for i in range(int(num)+1):
#         if i % 2 == 0:
#             evenSum += i
#             count_even += 1
#         else:
#             oddSum += i
#             count_odd += 1
#     print(f'Average of even numbers={evenSum/count_even}')
#     print(f'Average of Odd numbers={oddSum/count_odd}')

# else:
#     print('invalid input')


# num = input('please input the number: ')
# list_even = []
# list_odd = []
# if num.isdecimal():
#     for i in range(int(num)+1):
#         if i % 2 == 0:
#             list_even.append(i)
            
#         else:
#             list_odd.append(i)
            
#     print(f'Average of even numbers={sum(list_even)/len(list_even)}')
#     print(f'Average of Odd numbers={sum(list_odd)/len(list_odd)}')

# else:
#     print('invalid input')



# for i in range(1500,2700):
#     if i % 5 == 0 and i % 7 == 0:
#         print(i)

# num = [1,2,3,4,5,6,7,8,9,10]
# count_even = 0
# count_odd = 0
# for i in num:
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print("Number of even numbers: ",count_even)

# print("Number of odd numbers: ",count_odd)

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} fishbuzz')
#     elif i % 3 == 0:
#         print(f"{i} buzz")
#     elif i % 5 == 0:
#         print(f'{i} buzz')
#     else:
#         print(i)

# n = int(input("please input the number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     avg = sum/n
# print(avg)

# n = int(input("please input the number: "))
# factorial = 1
# for i in range(1,n+1):
#     factorial *= i
# print(factorial)




# for i in range(1499,2701):
#     if i%5 == 0 and i%7 == 0:
#         print(i)


# numbers = [1,2,3,4,5,6,7,8,9]
# count_even = 0
# count_odd = 0 
# for i in numbers:
#     if i % 2 == 0:
#         count_even += 1
#     else:
#         count_odd += 1
# print(f'number of even number:{count_even}')
# print(f'number of odd number:{count_odd}')

# for i in range(1,51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzbuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     else:
#         print(i)


# userInput = int(input("please input the number: "))
# sum = 0
# for i in range(0,userInput+1):
#     sum += i
#     avg = sum/userInput
# print(sum,avg)

# userInput = int(input("please input the number: "))
# sum = 1
# for i in range(1,userInput+1):
#     sum *= i
#     print(sum)

# age = int(input('input ur age: '))
# if age > 18:
#     print("can vote")
# elif age < 0:
#     print("positive digit plz")
# else:
#     print("cant vote")

# name = input("ur name:")
# times = int(input("time of print: "))
# if name == '':
#     print("no name entered")
# else:
#     for i in range(times):
#         print(name)

# userInput = input("please input the number: ")
# if userInput.isdecimal():
#     int_user = int(userInput)
#     if int_user % 2 == 0:
#         print("even")
#     else:
#         print("odd")
# else:
#     print("not a valid number")


# sum = 0
# while True:
#     userInput = input("please input the number: ")
#     if userInput == "stop":
#         break
#     else:
#         if userInput.isdecimal():
#             sum += int(userInput)
#         else:
#             print("not a valid number")
# print(sum)

# userInput = input("please input the number: ")
# evensum = 0
# oddsum = 0
# if userInput.isdecimal():
#     for i in range(0,int(userInput)+1):
#         if i % 2 == 0:
#             evensum += i
#         else:
#             oddsum += i
#     print(evensum)
#     print(oddsum)
# else:
#     print('invalid input')
#     print("sum of odd number= 0")
#     print("sum of even number=0")   

# userInput = input("please input the number: ")
# oddSum = 0
# evenSum = 0
# count_even = 0
# count_odd = 0 

# if userInput.isdecimal():
#     for i in range(int(userInput)+1):
#         if i % 2 == 0:
#             evenSum += i
#             count_even += 1
#         else:
#             oddSum += i
#             count_odd += 1
#     print("averange of even number:", evenSum/count_even )
#     print("averange of even number:", oddSum/count_odd )
# else:
#     print("invalid input")

# import random
# print(random.randint(5,10))

# import random
# sum = 0
# userInput = int(input("input number: "))
# for i in range(0,userInput):
#     random_number = random.randint(2000,3000)
#     if random_number % 2 == 0:
#         sum += random_number
#         print(random_number)
#     print(f'sum of even random number: {sum} ')


# userInput = input("Enter a string: ")
# print(len(userInput))
# if userInput == '':
#     print('the string is empty')

# userInput = input("enter a string: ")
# half1 =userInput[:len(userInput)//2]
# half2 =userInput[len(userInput)//2:]
# print(half1,half2)
# if userInput =='':
#     print('the string is empty')

# userInput = input("input a sting: ")
# smallInput = userInput.lower()
# print(smallInput)
# print(userInput.lower())
# if userInput =='':
#     print("the string is empty")

# list = [100,200,300,400,500]
# # for i in list[::2]:
# #     print(i)
# list.append("seiha")
# list.extend([600,12,15,"seiha"])
# print(list)

# list = ["sda","dsad","dqwewqeqwd"]
# l2 = [len(value) for value in list]

# print(l2)

# import random
# def random_tuple(num):
#     sum = 0
#     for i in range(num):
#         random_num = random.randint(0,100)
#         sum += random_num
#         return i
        
# print(random_tuple(5))

l1 = [1,2,3,4,5,6,7,8]
l2 = [9,10,11,12,13,14]
res = dict(zip(l1,l2))
print(res)