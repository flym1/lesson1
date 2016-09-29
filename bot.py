from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

answers = { 
		"привет": "И тебе привет!", 
		"как дела?": "Лучше всех! А твои как?",
		"плохо": "Что случилось?",
		"отлично": "Оооо, это шикарно! Давай поговорим :)",
		"пока": "Не уходи, давай еще поговорим",
		"погода в Москве": "https://pogoda.mail.ru/prognoz/moskva/ , запомни у природы нет плохой погоды!",
		"как тебя зовут?": "Я - Bot Chappi. Могу рассказать тебе о python",
		"что такое python?": "Python - высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. А более подробно смотри здесь https://www.python.org",
		"кто тебя создал?": "Мой создатель fly_m1",
		"python что это?": "Python - высокоуровневый язык программирования общего назначения, ориентированный на повышение производительности разработчика и читаемости кода. А более подробно смотри здесь https://www.python.org",
		


}

def start(bot, update):
	print("Вызван /start")
	bot.sendMessage(update.message.chat_id, text = "Привет, землянин! Я бот, который помогает учиться питонить.)")
	
def talk_to_me(bot, update):
	print("Пришло сообщение: " + update.message.text)
	
	def get_answers(key, answers):
		return answers.get(key)
	user_input = update.message.text.lower().strip()
	answer = get_answers(user_input, answers)
	bot.sendMessage(update.message.chat_id, text = answer)
	

def run_bot():
	updater = Updater("247494769:AAEw0JZpLs0aKGCA4MuzG7ibFklQwDVWhJk") 

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	

	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	run_bot()
