import random
RPSList=['가위','바위','보']

count_user = 0
count_com = 0
count_all= count_user + count_com 

while True:
	print('-'*80)
	print('1.가위\t2.바위\t3.보\t4.횟수입력\t9.종료')
	num_user= int(input('번호를 선택하세요'))
	num_com = random.randint(0,2)
	if num_user == 9:
		print('총 %d회의 게임중 컴퓨터가 %d 회,당신이 %d회 이겼습니다.'%(count_all,count_com,count_user))
		if count_user > count_com:
			print('따라서	최종스코어 %d : %d로 (컴퓨터 : 당신)로 당신의 승리입니다.'%(count_com,count_user))
			break
		elif count_user < count_com:
			print('따라서	최종스코어 %d : %d로 (컴퓨터 : 당신)로 컴퓨터의 승리입니다.'%(count_com,count_user))
			break
		elif count_user == count_com:
			print('따라서	최종스코어 %d : %d로 (컴퓨터 : 당신)로 무승부입니다입니다.'%(count_com,count_user))
			break
	elif num_user==num_com+1:
		print('com : %s / User : %s'%(RPSList[num_com],RPSList[num_user]), end = '\t')
		print('Draw! 비겼습니다!')
		count_all = count_all + 1
		print('=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다.'%(count_com,count_user))
	elif (num_user == 1 and num_com == 2) or (num_user == 2 and num_com == 0) or (num_user == 3 and num_com == 1):
		print('com : %s / User : %s'%(RPSList[num_com],RPSList[num_user]), end = '\t')
		print('Win ! 당신이 이겼습니다!')
		count_user =count_user + 1
		print('=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다.'%(count_com,count_user))
	else : 
		print('com : %s / User : %s'%(RPSList[num_com],RPSList[num_user]), end = '\t')
		print('Lose ! 당신이 졌습니다!')
		count_com =count_com + 1
		print('=> 현재 스코어 %d : %d (컴퓨터 : 당신) 입니다.'%(count_com,count_user))
	