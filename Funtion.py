#what is function?
#A function is a block of code that only runs when it is called.
#type of function
#1- no arguement with return
#2- arguement with retern
#3- no arguement with no return
#4- arguement with no return


# #1-example
# def name():
#     return("seiha")
# print(name())

#2-example
def name(name):
    return(f'{name}')
name = name("chinapongthom")
print(name)
new_name = name + "tae kley"
print(new_name)

# #3-example
# def name_cam():
#     print("hello world")
# name_cam()

# #4-example
# def name_va(*num):
#     print("total:", sum(num))
# name_va(1,2,3,4,5,6,7)


def name_me(num='china', age= 100):
    print(num, 'and', age)
# name_me("seiha",30)
name_me()

# def name_go(userInput = input("my name is: ")):
#     print(f'my name is: {userInput}')
# name_go()
# name_go("kimhour")