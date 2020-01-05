a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a + b > c and b + c > a and c + a > b:
    print('周長: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面積: %f' % area)
else:
    print('不能構成三角形!!')