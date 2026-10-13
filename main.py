# def check_password(p):
#     has_uppercase = any(char.isupper() for char in p)
#     has_lowercase = any(char.islower() for char in p)
#     has_digit = any(char.isdigit() for char in p)
#     if (len(p) >= 8) and has_uppercase and has_lowercase and has_digit:
#         return "Strong"
#     else:
#         return "Weak"
#
#
# print(check_password("passoQWrd123"))

# marks = [60,56,89,36,90,50]
# def find_sum(marks):
#     sum = 0
#     for num in marks:
#         sum += num
#     return sum
# def find_average(marks):
#     avg = find_sum(marks)/len(marks)
#     return avg


# def char_freq(string):
#     result = {}
#     for char in string:
#         if char not in result:
#             result[char] = 1
#         else:
#             result[char] += 1
#     return result
# print(char_freq("Programming"))


# from math import sqrt
# cnt = 0
# def is_prime(n):
#     global cnt
#     if n < 2:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for i in range(2, int(sqrt(n)) + 1):
#             cnt = cnt + 1
#             if (n % i) == 0:
#                 return False
#
#         return True
#
# def prime_in_range(start,end):
#     for i in range(start,end+1):
#         if is_prime(i):
#             print(i)
#
#
# prime_in_range(1,100)
# print("Count = " + str(cnt))



def list_rotation(num_list,step):
    new_list = num_list[-step:] + num_list[:-step]
    return new_list
print(list_rotation([1,2,3,4,5,6,7,8,9],3))