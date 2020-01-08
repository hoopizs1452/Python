num = int(input('請輸入一組數字:'))
num2 = 0
while num > 0:
    num2 = num2 * 10 + num % 10
    num //= 10
print(num2)