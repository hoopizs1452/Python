from math import sqrt

num = int(input('請輸入一個正整數: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是質数' % num)
else:
    print('%d不是質数' % num)