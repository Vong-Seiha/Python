# num = input("Please input a Number: ")
# oddnumber = 0
# evennumber = 0

# if num.isdecimal():
#     for i in range(int(num)+1):
#         if i % 2 == 0:
#             evennumber += i
#         else:
#             oddnumber += i
#     print(f'Sum of evennumber= {evennumber} ')
#     print(f'Sum of oddnumber= {oddnumber}')
# else:
#     print("invalid number")
#     print(f'Sum of evennumber= {evennumber} ')
#     print(f'Sum of oddnumber= {oddnumber}')

num = input('Please input a number: ')   
oddnumber = 0
evennumber = 0

if num.isdecimal():
    for i in range(int(num)+1):
        if i % 2 == 0:
            evennumber += i
        else:
            oddnumber += i
    print(f"Sum of evennumber= {oddnumber}")
    print(f"Sum of oddnumber= {evennumber}")
else:
    print("Invalid number")
    print(f"Sum of evennumber= {oddnumber}")
    print(f"Sum of oddnumber= {evennumber}")

        