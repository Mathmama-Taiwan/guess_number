import random
print('歡迎來到猜數字遊戲')
num = random.randint(1, 100)
while True:
	guessnum = int(input('請輸入1~100的整數: '))
	if guessnum == num:
		print('終於猜對了！')
		break
	elif guessnum > num:
		print('比',guessnum,'小')
	elif guessnum < num:
		print('比',guessnum,'大')
