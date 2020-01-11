num = int(input('請輸入一個10000內的數:'))
lis = []
for i in range(1, num+1):
    if num % i == 0:
        lis.append(i)
total = sum(lis) - num
if(total == num):
    print(num, '是完全數!!')
else:
    print(num, '不是完全數!!')