def three_six_nine(n):
    count_n = 0
    clap = ["3", "6", "9"]
    list = [i for i in range(1,n)]
    for i, value in enumerate(list):
        a = str(value)
        count_n += a.count("3")
        count_n += a.count("6")
        count_n += a.count("9")
    print(count_n)


call = int(input())
three_six_nine(call)
