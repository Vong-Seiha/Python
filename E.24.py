import random
def random_tuple(num):
    list1 = []                    #for put random number
    sum = 0
    for i in range(num):               #putting arguement num
        random_num = random.randint(0,100)               #random number
        print(f'random number{i+1}: {random_num}')               #to know random number
        sum += random_num                       #sum the random number
        list1.append(random_num)                               #add random number to list
    print(tuple(list1))
    print(dict(zip(list1,list1)))
    return sum
            
print(random_tuple(5))

        
