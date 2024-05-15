from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я ваш бот.")

def main():
    # Замените YOUR_TELEGRAM_TOKEN на ваш токен Telegram
    updater = Updater(token='7039655596:AAF1qI4pk2QAK702DCEgp-XisMQ0ifi6jGM', use_context=True)
    dispatcher = updater.dispatcher

    # Добавляем обработчик команды /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Запускаем бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
