# 문자열로 뽑고싶었는데 안뽑힘
#그래서 list화시킴


arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
arr3 = [46, 33, 33 ,22, 31, 50]
arr4 = [27 ,56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    list1 = [str(bin(num))[2:] for i, num in enumerate(arr1)]
    list1 = [str(bin(num))[2:] for num in arr1]

    list2 = [str(bin(num))[2:] for i, num in enumerate(arr2)]
    list1_convert = []
    list2_convert = []
    for j, num in enumerate(list1):
        # list1_convert.append(list(f"{num:0>5}"))
        list1_convert.append(list(f"{num:0>n}"))
    for m,num2 in enumerate(list2):
        list2_convert.append(list(f"{num2:0>n}"))
    for k in range(n):
        for l in range(5):
            if list1_convert[k][l] == "1" or list2_convert[k][l] == "1" :
                list1_convert[k][l] = "#"
            else :
                list1_convert[k][l] = " "
        list1_convert[k] = "".join(list1_convert[k])        

    answer = list1_convert
    print(answer)

solution(6,arr3,arr4)


