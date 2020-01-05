score = int(input('請輸入成績:'))
if score >= 90:
    grade = 'A'
elif score <= 89 and score >= 80:
    grade = 'B'
elif score <= 79 and score >= 70:
    grade = 'C'
elif score <= 69 and score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('該成績等級為:', grade)