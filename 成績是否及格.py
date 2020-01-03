def passDown(lis):
    array = []
    for i in lis:
        if i < 60:
            array.append(False)
        else:
            array.append(True)
    return array

arr = []
num = int(input('請輸入成績(-1結束):'))
while num != -1:
    arr.append(num)
    num = int(input('請輸入成績(-1結束):'))
    
print(passDown(arr))