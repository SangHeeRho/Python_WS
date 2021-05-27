



# 3의 배수일 시 Fizz
# 5의 배수일 시 Buzz
# 3과 5의 공배수일 시 FizzBuzz출력
num_list = [i for i in range(1, 101)]


# method1
# for i in num_list:
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# method2
# for i in num_list:
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# method3
# for i in num_list:
#     print("Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) or i)


# method4
# n = ["Fizz"*(i % 3 == 0) + "Buzz"*(i % 5 == 0) for i in num_list or i]
# print(n)


# method5 with function
# def FizzBuzz(num):
#     if num % 3 == 0 and num % 5 == 0:
#         return "FizzBuzz"
#     elif num % 3 == 0:
#         return "Fizz"
#     elif num % 5 == 0:
#         return "Buzz"
#     else:
#         return num

# for i in num_list:
#     print(FizzBuzz(i))



