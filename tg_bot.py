import telebot

# Замените 'YOUR_API_TOKEN' на токен вашего бота
API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

#@bot.message_handler(commands=['start', 'help'])
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я Ваш эхо-бот. Напишите мне что-нибудь! ')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Я умею отвечать только на фразы "Привет!" и "Как дела?"')

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "Привет!":
        bot.reply_to(message, "Привет! Как я могу помочь?")
    elif message.text == "Как дела?":
        bot.reply_to(message, "У меня все хорошо! А как у Вас?")
    else:
        bot.reply_to(message, "Извините, я не понимаю. Попробуйте сказать 'Привет!' или 'Как дела?'")

# Запуск бота
if __name__ == '__main__':
    print("Бот запущен...")
    bot.polling(none_stop=True)