start = 100
array = []
count = 10
high = start

while len(array)<count:
    array.append(high * 2)
    high /= 2

print('共經過多少公尺：', sum(array)-start)
print('第十次反彈高度：', high)