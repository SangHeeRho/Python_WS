# print("*****홍익 대학교 과일 판매머신 VO1*****")
# print("1. orange : 1000원")
# print("2. strawberry : 2500원")
# print("3. peach : 1500원")
# print("4. mango : 2000원")
# print("5. grape : 2000원")
# print("6. 종료")
# print("===============================")

# while True:
# 	number = int(input("구매 번호를 입력하세요(1~6)"))
# 	if number == 1:
# 		print("orange = 1000원")
# 	elif number == 2:
# 		print("strawberry = 2500원")
# 	elif number == 3 :
# 		print("peach = 1500원")
# 	elif number == 4 :
# 		print("mango = 2000원")
# 	elif number == 5 :
# 		print("grape = 2000원")
# 	elif number == 6 :
# 		print("종료되었습니다.")
# 		break

fruitList=['orange','strawberry','peach','mango','grape','종료']
PriceList=[1000,2500,1500,2000,2000]
numList=[1,2,3,4,5]
num_List=[i for i in range(0,len(fruitList))]
print('*'*6,end='')
print(" 홍익 대학교 과일 판매 머신 V01 ",end='')
print('*'*6,end='\n')
for i in range(1,len(fruitList)):
  print('%d. %s : %d원'%(i,fruitList[i-1],PriceList[i-1]))
# print('%d. %s : %d원'%(numList,fruitList,PriceList))

while True:
    print("="*30)
    n=int(input("구매 번호를 입력하세요(1~5)"))
    print("<"*30)
    if n in range(1,len(fruitList)):
		    print('%s %d원 입니다.'%(fruitList[n-1],PriceList[n-1]))
    elif n ==6:
        print('종료되었습니다.')
        break
    else:
        print("번호를 확인해주세요.")