import random
num = int(input('請輸入一個數字(1~100):'))
step = 0
run = True
while run:
    guess = random.randrange(1, 100)
    if guess == num:
        print('Aha!!答案是:', guess)
        run = False
    else:
        print('我猜是:', guess)
    step += 1
print('我總共花了 %d 步' % step)