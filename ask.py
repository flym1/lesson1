while True:
	user_ask = input('Как дела?')
	if user_ask == 'Хорошо':
		print('Отлично, пока')
		break
	else:
		print('Как дела? %s' % user_ask)
