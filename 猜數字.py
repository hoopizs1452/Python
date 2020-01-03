import random

num = random.randrange(1, 100)
run = True

while run:
    guess = int(input('猜一個數字(1~100):'))

    if guess == num:
        print('恭喜您！！答對啦！！')
        run = False
    elif guess < num:
        print('您猜的數字太小囉！！:(')
    else:
        print('您猜的數字過大囉！！:(')