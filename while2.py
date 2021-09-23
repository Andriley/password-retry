pw = 'a123456'
x = 0
while x < 3:
	u_pw = input('please input ur pw: ')
	if u_pw == pw:
		print('login successfully')
		break
	else:
		print('wrong pw, you still got', 2-x, 'chance')
		x = x + 1

