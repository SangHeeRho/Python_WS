
#두 가지 값 어떻게입력받는건지 모르겠음
# X=int(input())
# Y=int(input())
# if (0<X<=1000) and (0<Y<=1000):
#     print('1')
# if (-1000<=X<0) and (0<Y<=1000):
#     print('2')
# if (-1000<=X<0) and (-1000<=Y<0):
#     print('3')
# if (0<X<=1000) and (-1000<=Y<0):
#     print('4')

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