def make_list(*newlist):
    return list(newlist)
print("""make_list(21,"hello",35)""")
print(make_list(21,"hello",35))

def make_list(num1,string,num2):
    list = []
    list.extend([num1,string,num2])              #add arguement to list
    return list
print(make_list(21,"hello",35))

