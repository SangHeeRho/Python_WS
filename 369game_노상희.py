#-------------method01(fail)------------------
#-> 일의자리, 십의자리 경우의수로 하고싶었지만 함수를 생각해내지못했습니다..
# game=[3,6,9]
# N=int(input('박수 친 횟수를 구하여라.'))
# M=str(N)
# for i in range(1,N+1):
    # if len(M) ==1:
    #     if N in game:
    #         count+=1
    #         print(count(N))

#------------------internet01--------------
N=int(input())
nList=[str(i) for i in range(1,N+1)]
count=0
for num in nList:    
    if '3' in num:
        count+= num.count('3')
    if '6' in num:
        count+= num.count('6')
    if '9' in num:
        count+= num.count('9')
print(count)
    # if count>0:
    #     print('짝'*count,end=' ')
    # else:
    #     print(num,end=' ')
# print(count)
# #--------------internet03-----------------