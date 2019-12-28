ent = input('請輸入字串：')
e = 0
s = 0
n = 0
o = 0
for i in ent:
	if i.isalpha():
		e += 1
	elif i.isspace():
		s += 1
	elif i.isdigit():
		n += 1
	else:
		o += 1
print('字母：', e)
print('空格：', s)
print('數字：', n)
print('其他：', o)