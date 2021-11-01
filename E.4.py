urname = input("please input name: ")
times = int(input("input number of time to print: "))
if urname == '':                                                    
    print("No name entered")

else:
    for i in range(times):
        print(urname)
# if len(urname) == 0: