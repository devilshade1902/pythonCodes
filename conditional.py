# num1 = 1


# if num1 > 5 :
#     print("hello")
# else:
#     print("bye")

# print("Rest of the logic")


# num1 = int(input("Enter a number: "))

# if num1%3 == 0:
#     print(num1, " is divisible by 3")
# else:
#     print(num1, "is not divisible by 3")
# i = 0
# while i<10:
#     num1 = int(input("Enter a number: "))

#     if num1 > 0 :
#         print("positive")
#     else:
#         print("negative")



# i=0
# while i<10:
#     num1 = int(input("enter a number : "))
#     if num1 % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
    
# num1 = int(input("Enter mark of 1 subject"))
# num2 = int(input("Enter mark of 2 subject"))
# num3 = int(input("Enter mark of 3 subject"))

# total = num1+num2+num3
# avg = total/3 
# if avg>45:
#     print("Pass")
# else:
#     print("fail")


# word = str(input("Enter a alphabet: "))

# if word == 'a'or word =='e' or word=='i'or word=='o'or word== 'u':
#     print("its a vowel")
# else :
#     print("its a consonant")


# age = int(input("Enter your age: "))

# if age>=18:
#     print("eligible")
# else:
#     print("Not eligible")


num1 = int(input("enter 1 number: "))
num2 = int(input("enter 2 number: "))
num3 = int(input("enter 3 number: "))

if num1 > num2 and num1>num3:
    print(num1, "is largest: ")
elif num2 > num1 and num2>num3:
    print(num2, "is the largest: ")
elif num3>num1 and num3>num2:
    print(num3, "is largest: ")