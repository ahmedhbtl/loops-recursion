

def factorial(n):
    answer = 1
    i = 1
    while i <= n:
        answer = answer * i
        i = i + 1
    return answer

print(factorial(10))










# while True:
#     i = input("What should I do?")
#     if i == "continue":
#         print("Looping again...")
#     elif i == "stop":
#         break




# # def fibonacci(n):
# #     if n == 0:
# #         return 0
# #     if n == 1:
# #         return 1

# #     return fibonacci(n-1) + fibonacci(n-2)

# def fibonacci(n):
#     n1 = 0
#     n2 = 1

#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     total = 0

#     for i in range(n - 2):
#         total = n1 + n2
#         n1 = n2
#         n2 = total
    
#     return total

# print(fibonacci(10000))








# # def factorial(n):
# #     # Base case
# #     if n == 0:
# #         return 1
# #     # Recursive case
# #     return n * factorial(n-1)

# # result = factorial(3)
# # print(result)

# # def factorial(n):
# #     answer = 1
# #     for i in range(1, n+1):
# #         answer = answer * i
# #     return answer

# # print(factorial(10000))



















