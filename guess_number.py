import random

print('歡迎來到猜數字遊戲')
first = int(input('決定範圍，請輸入最小數字:'))
last = int(input('請輸入最大數字:'))
num = random.randint(first, last)
count = 0
while True:
	count += 1 # count = count + 1
	guessnum = int(input("請猜數字: "))
	if guessnum == num:
		print('終於猜對了！')
		break
	elif guessnum > num:
		print('比', guessnum, '小')
	elif guessnum < num:
		print('比', guessnum, '大')
print('你總共猜了', count, '次')
