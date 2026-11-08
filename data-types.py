# # city1 = "mumbai"
# # print("city : ",city1)
# # city3 = "this is delhi city"
# # print("city : ", city3)

# # print(city1.upper())
# # print(city3.split())

# # print(city1.replace('mu', 'M'))
# # print("city1 after string operations : ", city1)
# # data ="hello,world"
# # print(data[4:10])
# # print(data[:10])
# # print(data[4:])
# # print(data[4:10:2])

# # lists

# # data = ["dhruv","dhruv@gmail.com",19,"mumbai","+91-874383920","dhruv123"]
# # print("my name is : ",data[0])

# # for i in data:
# #     print(i)

# # list1 = [100,200,300,400]
# # list2 = [400,300,500,700]
# # print(list1+list2)
# # result = list1[1]+list2[1]
# # print(result)

# # fruits = ["apple","banana","kiwi","oranges","grapes"]
# # print(fruits[0])
# # print(fruits[1])
# # print(fruits[2])
# # print(fruits[3])
# # print(fruits[4])

# # fruits[3] = 'pineapples'
# # print(fruits)

# # fruits.append("watermelon")
# # print(fruits)
# # fruits.insert(3,"mangoes")
# # print(fruits)

# # fruits.remove("banana")
# # print(fruits)

# # fruits.pop(5)
# # print(fruits)

# # fruits.clear()
# # print(fruits)


# # mylist = [234,789,567,455]
# # currency = [inr*72 for inr in mylist]
# # print(currency)


# # numbers = [100,200,300,400,500,300]
# # print(numbers[0])
# # print(numbers[1])
# # print(numbers[2])
# # print(numbers[3])
# # print(numbers[4])
# # print(numbers[5])


# # numbers2 = [num*2 for num in range (20,31)]
# # print(numbers2)

# # fruits = {"appple","kiwi","banana","lemons","kiwi"}
# # print(fruits)

# # fruits2 = set(["apple","banana","oranges","kiwi","oranges"])
# # print(fruits2)


# # fruits2.add("pineapple")
# # fruits2.update(["melons","guava","avocado"])
# # print(fruits2)

# # fruits.remove("kiwi")
# # print(fruits2)

# # fruits.remove("kiwi")
# # print(fruits2)

# # fruits2.discard("melons")
# # print(fruits2)

# # fruits2.discard("melons")
# # print(fruits2)



# # person ={"name":"dhruv","age":19,"email":"dhruv@gmail.com"}
# # print(person)

# # employee = dict({"name":"akash","age":19,"email":"dhruv@gmail.com"})
# # print(employee)

# # print(employee["name"])
# # print(employee["email"])


# # matrix = [
# #     [1,2,3],
# #     [4,5,6],
# #     [7,8,9]
# # ]

# # print(matrix)

# # print(matrix[0])
# # print(matrix[1])
# # print(matrix[2])


# # print(matrix[0][2])

# # seats_patter = [
# #     ["seat1","seat2","seat3"],
# #     ["seat4","seat5","seat6"],
# #     ["seat7","seat8","seat9"]
# # ]

# # print(seats_patter[1][1])

# # matrix2 = [
# #     [11,12,13],
# #     [14,15,16],
# #     [17,18,19]
# # ]

# # for r in matrix2:
# #     print()
# #     for item in r:
# #         print(item,end=' ')


# # matrix3 = [
# #     [1,2],
# #     [3,4]
# # ]

# # matrix4=[
# #     [5,6],
# #     [7,8]
# # ]

# # for i in matrix3:
# #     for num in i:
# #         print(num)
    

# # data = ()
# # print(data)
# # data = (1,2,3,4)
# # print(data)
# # data = ("hi","hello","welcome","bye")
# # print(data)
# # data =(1234,"dhruv","mumbai",400017,True,1234.6758)
# # print(data)

# # data = (11,12,13,11,12,13)
# # print(data[2])
# # result = data[0]+data[3]
# # print(result)

# # data = (12,("welcome","bye"),"hello")
# # print(data)

# # data = ("delhi",[100,200,300,'mumbai'],'kolkata',203904)

# # tuple1 = (110,120,130)
# # tuple2 = (210,220,230)

# # result = tuple1+tuple2
# # print(result)

# # tuple4 = (1,2,3)*4
# # print(tuple4)

# # tuple5 = (123,124,125,126,123,131,125)
# # print(tuple5.count(123))
# # print(tuple5.index(126))
# tuple7 = (89,56,99,34,101,73,123,45,56)

# max_num_tuple = tuple7[0]

# # for i in tuple7:
# #     if i > max_num_tuple:
# #         max_num_tuple = i

# # print(max_num_tuple)

# # min_num_tuple1 = tuple7[0]
# # for i in tuple7:
# #     if i < min_num_tuple1:
# #         min_num_tuple1 = i

# # print(min_num_tuple1)

# # tuple9 = (89,56,99,89,34,101,34,73)
# # occ = int(input("enter a number: "))
# # count = 0
# # for i in range(len(tuple9)):
# #     if  tuple9[i] == occ:
# #         count+=1

# # print(count)



# # print(count)
# # students = (1,"dhrub",18)
# # id,name,age = students
# # print(id,name,age)

# # set1 = {10,20,30,40}
# # set2 = {30,40,50,60}

# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # print(set1.difference(set2))

# # set3 = {12,13,15,16}
# # print(set3)

# # print(13 in set3)
# # print(144 in set3)

# # def addition(a,b):
# #     result = a+b
# #     print(result)

# # addition(20,10)
# # def isstringunique():
# #     strdata = input("Enter string data : ")
# #     message = True

# #     for i in range(len(strdata)):
# #         for j in range(i+1,len(strdata)):
# #             if (strdata[i] == strdata[j]):
# #                 message=False

# #     print("is string unique?: " , message)


# # isstringunique()

# # def greeting (message = "hello all...!"):
# #     print("The default value of message: ", message)

# # greeting()
# # greeting("Welcome")

# # def addition(num2,num1 = 100,num3 = 90):
# #     result = num1 + num2 - num3
# #     print(result)


# # addition(10)

# # def multiply(*args):
# #     print(*args)

# # multiply(1,2,3,4,5)


# # def greetings(*args):
# #     print(*args)

# # greetings("hello","welcome","mumbai")


# # def addition():
# #     num1 = 10
# #     print(num1)
# #     num2 = 20
# #     result = num1+num2
# #     return result


# # x1 = 100
# # result1 = x1-addition()
# # print("result: ",result1)


# # def subtraction(num1,num2):
# #     return num1-num2



# # print("Result of subtraction: ", subtraction(100,345))

# # result = lambda n1,n2 : n1+n2
# # print("result of addition using lambda function : ",result(12,3))

# # result = lambda n1,n2 : n1*n2
# # print("result of multiplying using lambda function : ",result(12,3))
# # result = lambda n1,n2 : n1/n2
# # print("result of division using lambda function : ",result(12,3))
# # result = lambda n1,n2 : n1**n2
# # print("result of power using lambda function : ",result(12,3))

# # numbers = [1,2,3,4,5,6,7,8]
# # result = list(filter(lambda x:x%2  == 0,numbers))
# # print(result)

# # numbers = [1,2,3,4,5,6,7,8]
# # result = list(filter(lambda x:x%2  != 0,numbers))
# # print(result)

# # numbers = [-10,-5,0,5,10,15]
# # result= list(filter(lambda x: x>=0,numbers))
# # print(result)

# # chart = ["hi","hello","a","world","cat"]
# # result = list(filter(lambda x : len(x)>3,chart))
# # print(result)

# # numbers = [1,2,3,4,5]
# # result = list(map(lambda x:x+100,numbers))
# # print(result)

# # numbers = [1,2,3,4,5,6,7]
# # result = list(map(lambda x:x**2,numbers))
# # print(result)

# # numbers = [1,2,3,4,5,6,7]
# # result = list(filter(lambda x: x%2 == 0,numbers))
# # double = list(map(lambda x:x**2,result))
# # print(double)

# # from functools import reduce

# # numbers = [1,2,3,4,5]
# # result = reduce(lambda x,y:(x+y)/len(numbers),numbers)
# # print(result)

# # numbers = [1,2,3,4,5]
# # result = reduce(lambda x,y:x+y,numbers)
# # result1 = result // len(numbers)
# # print(result1)


# # import math

# # print(math.sqrt(25))
# # print(math.factorial(5))
# # print(math.pow(3,2))
# # print(math.floor(1234.456))
# # print(math.ceil(1234.456))


# # import datetime 

# # print(datetime.datetime.now())

# import my_module
# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# result = my_module.addition(num1,num2)
# print(result)


