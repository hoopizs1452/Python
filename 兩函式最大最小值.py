def largeSmall1(*num):
    max = num[0]
    min = num[0]
    for i in num[1:]:
        if i > max:
            max = i
        if i < min:
            min = i
    ans = largeSmall2(maximum=max, minimum = min)
    return 
def largeSmall2(**kwargs):
    for key in kwargs:
        print('{0}: {1}'.format(key, kwargs[key]))

largeSmall1(2, 3, 5, 7, 9)