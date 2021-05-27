# 3의 배수일 시 Fizz
# 5의 배수이면 Buzz
# 3과 5의 공배수 -> 15이면 FizzBuzz
# list -> 0-100


# method 01
for i in range(0,100):
    if i % 15 == 0:
        print("FizzBuzz")    
    elif i % 3 ==0:
        print("Fizz")
    elif i % 5 ==0:
        print("Buzz")
    else:
        print(i)

DIV=[3,5,15]
for i in range(0, 100):
    print(Fizz*)