# num1= 100
# num2 = 100 

# result = num1+num2
# print(result)

# result = num1 - num2
# print(result)

# result = num1 / num2
# print(result)

# result = num1 % num2 
# print(result)

# l = 200
# b = 100

# area_of_rectangle = l*b
# print(area_of_rectangle)

# f = 21
# ftoc = (f-32) * 5/9
# print(ftoc)


# num3 = 5
# num4= 7

# # Arthimetic
# print(num1, ">",num2,"=",(num1>num2))
# print(num1, ">=",num2,"=",(num1>=num2))
# print(num1, "<",num2,"=",(num1<num2))
# print(num1, "<=",num2,"=",(num1<=num2))
# print(num1, "==",num2,"=",(num1==num2))
# print(num1, "!=",num2,"=",(num1!=num2))

# # Relational/ comparison
# num = 20
# result = num % 3
# print("Number", num, "is divisible by 3? ", (result == 0 ))

# num = 20
# result = num % 2
# print("Number", num, "is even? ", (result == 0 ))

# num = 20
# result = num % 2
# print("Number", num, "is odd? ", (result != 0 ))

# # logical
# num = 30

# result3 = num%3
# result7 = num%7

# print(num, "is divisible by 3 and 7 both", (result3 == 0 and result7 == 0))
# print(num, "is divisible by 3 and 7 both", (result3 == 0 or result7 == 0))

# num = 12
# if num % 2 == 0:
#     print("EVEN")
# else :
#     print("ODD")


# num = 20
# result = "even" if (num%2 == 0 ) else "odd"
# print(result)

# result = (num,"divisible by 3 and 7 both") if ((num%3 == 0)and (num%7 == 0)) else (num,"neither divisible by 3 nor 7")
# print(result)

# sml= int(input("Enter small container: "))
# lg = int(input("enter large container: "))
# less_than_liter = 0.10
# more_than_liter = 0.25
# refund = (sml*less_than_liter)+(lg*more_than_liter)
# print(refund)

# name = "Dhruv Sawant"
# phone_number = "938492920"
# address = "mazgaon lovelane byculla east"
# city = "Mumbai"
# pincode = "40010"

# mailing = (name + phone_number + address+city + pincode)
# print(mailing)


# num1 = 100
# num1 += 50
# print(num1)

# num1 *= 2
# print(num1)

# num1 -= 120
# print(num1)


# p = int(input("principle amount"))
# r= int(input("Rate of interest"))
# n = int(input("No of year"))

# for i in range(n):
#     result = p*(1+r/100)**i
#     print(result)


im = 1000
roi = 0.04


b1 = im*(1+roi)
b2 = b1 * (1+roi)
b3 = b2 * (1+roi)

print("Total amount :", b3)

mpg = int(input("Enter MPG : "))
l = 235.2145831 / mpg
print(l,"/100") 

