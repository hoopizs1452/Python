while True:
    try:
        num = int(input('請輸入一個值:'))
    except ValueError:
        print('輸入的數必須是正整數!!')
        continue
    break
guess = num / 2
middle = num / 4
step = 0
while guess != num:
    if num > guess:
        guess += middle
        print('I guess: ', guess)
    elif num < guess:
        guess -= middle
        print('I guess: ', guess)
    middle /= 2
    if middle == 0:
        middle = 1
    step += 1

print('Aha!!答案是:', guess)
print('我總共花了%d步' % step)