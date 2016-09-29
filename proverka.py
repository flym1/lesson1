answers = { 
		"привет": "И тебе привет!", 
		"как дела": "Лучше всех", 
		"пока": "Увидимся"
}

def get_answers(key, answers):
	return answers.get(key)
user_input = input().lower().strip()
answer = get_answers(user_input, answers)
print(answer)