# print("Hello world!") #manuly print 

# gretting = "Hello world!" #store value ==> variable name gretting 
# print(gretting) #value print 


a = 'Hello world'
b = "Hello world"
c = """Hello world"""

# String operator 

print(a+" "+b)  #Hello world Hello world
print(a+b) #Hello worldHello world

# version 3.0 Python 
print(f'{a} {b}') #print(a+" "+b)
print('{} {}'.format(a,b)) #String.format()



# String Slide 
# index start from 0 
    #length start from 1 
a = 'Helloworld' #0,1,2,3,4,5,6,7,8,9,10,11,.....,n
print(len(a)-1)
#index = length - 1 

# string[start:stop-1:step]
print(a[0:3])
print(a[:5]) #get from index 0 to [(1,2,3,4),5,6]
print(a[4:]) #Start from index 4 to the end 1,2,3,(4,5,6,7,8,9,...n)
print(a[0::2]) 
print("===========")
#for loop string 
# for i in range(0,len(a)): #for loop (start, stop-1)
#     print(i)

# for i in range(0,len(a),2):
#     print(a[i])
# H
# l
# o
# o
# l

#store value into variable
# a = 'Helloworld'
    # First method
# res = ""
# for i in range(0,len(a)):
#     if i % 2 == 0:
#         res += a[i]
# print(res)

    #Second method
# res = ""
# for i in range(0,len(a),2):
#     res += a[i]
# print(res)

    #Third method
# print("".join(a[i] for i in range(0,len(a),2)))

res = 0 
for i in range(1,11):
    res += i

print(res)




