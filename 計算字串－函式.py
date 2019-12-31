import string

def check(count):
    letter = 0
    num = 0
    space = 0
    other = 0
    for i in count:
        if i.isalpha():
            letter += 1
        elif i.isdigit():
            num += 1
        elif i.isspace():
            space += 1
        else:
            other += 1
    print('字母:', letter, '數字:', num, '空格:', space, '其他:', other)

word = input('輸入字串：')
check(word)