import math;

# n = 10



# for i in range(1,n+1):
#     print(i**3)

# cube = 0
# n= int(input("enter value for n : "))
# for i in range(1, n+1,1):
#     cube = i*i*i
#     print(i,"*",i,"*",i,"=", cube)


# square = 0
# n = int(input("enter a number: "))
# for i in range(1,n+1):
#     square = i*i
#     print(square)


# n = int(input("enter a number: "))
# rev= 0 
# rem = 0
# temp = n

# while temp >0:
#     rem = temp%10
#     rev = rev*10+rem
#     print(rev)
#     temp = math.floor(temp / 10)



# rem = 0
# temp = n

# while temp >0:
#     rem = temp%10
#     rev = rev*10+rem
#     temp = math.floor(temp / 10)
# if rev == n:
#     print("palindrome")
# else:
#     print("Not palindrome")


# while n >0:
#     rem = n%10
#     rev = rev*10+rem
#     n = math.floor(n / 10)
# if rev == n:
#     print("palindrome")
# else:
#     print("Not palindrome")
    

n = 50

print("EVEN")
for i in range(1,n+1):
    if i%2 == 0:
        print(i)


