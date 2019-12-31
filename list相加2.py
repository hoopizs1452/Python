def check(a, b):
    startNum = a
    array = [startNum]
    while b > 1:
        a *= 10
        a += startNum
        array.append(a)
        b -= 1
    return sum(array)
start = input('輸入初始值：')
numRange = input('輸入幾個數：')
start = int(start)
numRange = int(numRange)
print(check(start, numRange))