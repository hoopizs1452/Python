def poker():
    suit = ['愛心', '菱形', '黑桃', '梅花']
    num = []
    x = 'A'
    y = 'J'
    z = 'Q'
    u = 'K'
    count = 1
    while count < 53:
        num.append(count)
        count += 1
    for i in num:
        for j in suit:
            if i%13==1:
                print(j, x)
            elif i%13==11:
                print(j, y)
            elif i%13==12:
                print(j, z)
            elif i%13==0:
                print(j, u)
            else:
                print(j, i%13)
            
poker()