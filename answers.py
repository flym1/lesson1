dial = {
		"привет": "И тебе привет!", 
		"как дела": "Лучше всех", 
		"пока": "Увидимся"
		}
def get_dial(key, dial):
	return dial.get(key)
def ask_user(dial):
	while True:
		try:
			user_input = input("Скажи что-нибудь: ")
			dial = get_dial(user_input, dial)
			print(dial)
			if user_input == "пока":
				break
		except KeyboardInterrupt:
			print("Нее, друже, давай поговорим :)")	
if __name__ == "__main__":
	ask_user(dial)