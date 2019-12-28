start = input('輸入初始值：')
num = input('輸入幾個數：')
num = int(num)
start = int(start)
secondStart = start
array = [start]
while num > 1:
    start *= 10
    start += secondStart
    array.append(start)
    num -= 1
print(sum(array))