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
    for i in suit:
        for j in num:
            if j<=13:
                print(suit[0])
            elif j<=26:
                print(suit[1])
            elif j<=39:
                print(suit[2])
            elif j<=52:
                print(suit[3])
            if j%13==1:
                print(x)
            elif j%13==11:
                print(y)
            elif j%13==12:
                print(z)
            elif j%13==0:
                print(u)
            else:
                print(j%13)
            
poker()