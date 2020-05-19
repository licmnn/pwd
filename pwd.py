password = 'a123456'
x = 3
while x > 0:
	pw = input('请输入密码： ')
	if pw == password:
		print('登入成功') # quit
		break
	elif x != 0:
		x = x - 1
		print('密码错误！ 还有%d次机会！' % x)
	else:
		pirnt('')