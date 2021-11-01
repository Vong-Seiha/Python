# def fun_calc(num1,num2):
#     res = num1 * num2
#     return res
# print(fun_calc(50,2))


# def fun_split(givenStr):
#     return givenStr.split()
# print(fun_split("hello welcome to python programming language"))

# def make_list(num1,string,num2):
#     list = []
#     list.extend([num1,string,num2])
#     return list
# print(make_list(12,"seiha",23))

# import random
# def random_tuple(givenNum):
#     lst = []
#     sum = 0
#     for i in range(givenNum):
#         random_num = random.randint(0,100)
#         sum += random_num
#         print(f'random number {i+1}: {random_num} ')
#         lst.append(random_num)
#     print(tuple(lst))
#     return sum
# print(random_tuple(5))
# print(sum)

# import random
# def random_tuple(num):
#     lst = []
#     sum = 0
#     for i in range(num):
#         random_num = random.randint(0,100)
#         sum += random_num
#         lst.append(random_num)
#     print(tuple(lst))
#     return sum
# print(random_tuple(5))
# print(sum)


# def make_list(num1,string,num2):
#     lst = []
#     lst.extend([num1,string,num2])
#     return lst
# print(make_list(21,"seiha",31))

# import random
# def random_tuple(num):
#     lst = []
#     sum = 0
#     for i in range(num):
#         random_num = random.randint(0,100)
#         sum += random_num
#         lst.append(random_num)
#     print(tuple(lst))
#     return sum
# print(random_tuple(5))
# print(sum)

# def sum_of_list(lst):
#     return sum(lst)
# print(sum_of_list([20,15,10,30]))

# def search_in_tuple(tup,ind):
#     if ind in tup:
#         return f"element found at index: {tup.index(ind)}"
#     else:
#         return "element not found"
# print(search_in_tuple ((20,15,10,30),12))

# def mean_of_list(lst):
#     listsum = sum(lst)
#     avg = listsum/len(lst)
#     return avg
# print(mean_of_list([50,10,62,32]))


# def slice_list(lst,index):
#     return lst[index:-index]
# print(slice_list([10,20,30,40,50,60,70],2))

# def make_dict(lst,tup):
#     tup = list(tup)
#     newzip = zip(lst,tup)
#     return dict(newzip)
# print(make_dict([50,10,62],("china","kimhour","rith")))


# def fun_calc(num1,num2):
#     res = num1 * num2
#     return res
# print(fun_calc(50,2))


# def fun_split(lst):
#     return lst.split()
# print(fun_split("hello my name is vong seiha"))

# def make_list(num1,string,num2):
#     list = []
#     list.extend([num1,string,num2])
#     return list
# print(make_list(21,"heeloo",35))

# import random
# def random_tuple(userInput):
#     list = []
#     sum = 0
#     for i in range(userInput):
#         random_num = random.randint(0,100)
#         print(f'random number is {i+1}: {random_num}')
#         sum += random_num
#         list.append(random_num)
#     print(tuple(list))
#     return sum

# print(random_tuple(5))
# print(sum)

# def sum_of_list(lst):
#     lstSum = sum(lst)
#     return lstSum
# print(sum_of_list([20,15,10,30]))

# def search_in_tuple(tup,ind):
#     if ind in tup:
#         return f"element found at index: {tup.index(ind)}"
#     else:
#         return "element not found in tuple"
# print(search_in_tuple((10,20,30,30,40,30,50),20))


# def mean_of_list(givenLst):
#     sumLst = sum(givenLst)
#     avg = sumLst/len(givenLst)
#     return avg
# print(mean_of_list([50,10,62,32]))


# def slice_list(lst,slc):
#     return lst[slc:-slc]
# print(slice_list([50,10,62,32,64,78,90],2))


# def make_dict(lst,tup):
#     make_dict = {}
#     tup = list(tup)
#     for i in lst:
#         for j in tup:
#             make_dict[i] = j
#     return make_dict
# print(make_dict([50,10,62],("china","kimhour","rith")))

