answers = {'привет':'Привет',
		   'как дела': 'Хорошо',
		   'что делаешь': 'Программирую'
			}


def get_answer(question, answers):
	return answers.get(question)


def ask_user(answers):
	while True:
		try:
			user_say = input('Скажи что-нибудь:')
			answer = get_answer(user_say, answers)

			if user_say == 'пока':
				print('До встречи')
				break

			if answer is None:
				print(f'Сам ты {user_say}')
			else:
				print(answer)
		except KeyboardInterrupt:
			print('Пока!')
			break

if __name__ == '__main__':
	ask_user(answers)