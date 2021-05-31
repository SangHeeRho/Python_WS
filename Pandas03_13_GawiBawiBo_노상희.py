import random

GBB=['가위','바위','보','횟수입력','종료']
RSP=['가위','바위','보']
a=random.choice(RSP)
# for i in range(0,len(GBB)):
#     print("-"*60)
#     print('%d. %s'%(i+1,GBB[i]))
n=int(input('번호를 선택하세요. '))
if a == '가위':

