# word = 'welcome'
# result = word.capitalize()
# print(result)
# result1 = word[::-1]
# print(result1)


# def reverseString(s):
#     chars = list(s)
#     left = 0
#     right = len(chars) - 1
#     while left < right:
#         chars[left] , chars[right] = chars[right], chars[left]
#         left +=1
#         right -=1
#     return ''.join(chars)


# print(reverseString('friends'))

# numbers = [1,2,3,4,5]
# squares = [x*2 for x in numbers]
# print(squares)



# def reverse_string(s):
#     result = ""
#     for i in s:
#         print(i)
#         result = i+result
#     return result


# print(reverse_string("hello"))


# def reverse_string(s):
#     return s[::-1]


# print(reverse_string("dhruv"))

# def check_palindrom(s):
#     rev = s[::-1]
#     print(rev)
#     if (rev == s):
#         print("its a palindrome")
#     else:
#         print("its not a palindrome")
    

# check_palindrom("dhruv")


# def fibonacci_recursive(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
    
    
# print(fibonacci_recursive(6))


# 1 , 2 , 6, 24 , 


# def are_anagrams(s1, s2):
#     # Remove spaces and convert to lowercase
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     print(sorted(s1),sorted(s2))
#     return sorted(s1) == sorted(s2)


# print(are_anagrams("listen","silent"))