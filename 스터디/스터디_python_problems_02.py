#----------------02(method01)-----------------
# n=input('s')
# if len(n)==1 or len(n)==2: #문자 길이가 1,2인 경우 그대로 출력
#     print(n)
# elif 2<len(n)<=100:
#     if len(n) % 2 ==1:
#         print(n[int((len(n)+1)/2)])
#     else:
#         print(n[int(len(n)/2)-1],end='')
#         print(n[int((len(n)/2))])
# else:
#     print('번호를 확인하세요.')
#------------------02(method02)--------------
def solution():
    if len(n)==1 or len(n)==2: #문자 길이가 1,2인 경우 그대로 출력
        print(n)
    elif 2<len(n)<=100:
        if len(n) % 2 ==1:
            print(n[int((len(n)+1)/2)])
        else:        #print_result 활용*
            print(n[int(len(n)/2)-1],end='')
            print(n[int((len(n)/2))])
    else:
        print('번호를 확인하세요.')

n=input('s')
solution()



#-----------#2번solution--------------
input_str1 = "abcde"
input_str2 = "qwer"

def solution(input_str):
    index = len(input_str) / 2
    return input_str[int(index) - 1 : int(index) + 1] if index % 2 == 0 else input_str[int(index)]
    
def print_result(result):
    print(result)

print("str1's result = ", end = '')
print_result(solution(input_str1))
print("str2's result = ", end = '')
print_result(solution(input_str2))


#--------------method02--------
def solution(n):
    L=len(n)/2
    if len(n)==1 or len(n)==2: #문자 길이가 1,2인 경우 그대로 출력
        print(n)
    elif 2<len(n)<=100:
        if len(n) % 2 ==1:
            print(n[int((L+0.5)])
        else:        #print_result 활용*
            print(n[int(L)-1],end='')
            print(n[int(L)])
    else:
        print('번호를 확인하세요.')

n=input('s')
solution()