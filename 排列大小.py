num = [1, 3, 4, 2, 6, 10, 7, 9, 8, 5]
array = []
for i in range(len(num)):
    if num[i] > num[0]:
        array.append(i)
print(array)