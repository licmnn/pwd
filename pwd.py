#password = 'a123456'
#x = 3
#while x > 0:
#	pw = input('请输入密码： ')
#	if pw == password:
#		print('登入成功') # quit
#		break
#	elif x != 0:
#		x = x - 1
#		print('密码错误！ 还有%d次机会！' % x)
#	else:
#		pirnt('')

pw = input('请输入您的密码： ')
x = 2
print('密码错误！ 还有%d次机会 ' % x)
while x > 0 :
	if  pw != 'a123456' and x > 0:
		pw = input('请输入您的密码： ')
		x = x - 1
		print('密码错误！ 还有%d次机会 ' % x)
	elif x == 0:
	    print('密码错误！灭有机会了')
	elif pw == 'a123456':
		print('登入成功')