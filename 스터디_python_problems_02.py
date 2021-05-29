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
        else:
            print(n[int(len(n)/2)-1],end='')
            print(n[int((len(n)/2))])
    else:
        print('번호를 확인하세요.')

n=input('s')
solution()