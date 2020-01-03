def square(n):
    return n * n

num = input('輸入數字:')
num = int(num)
total = 0
while num > 0:
    total += square(num)
    num -= 1
print(total)