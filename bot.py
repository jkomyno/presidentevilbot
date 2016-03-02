from telegram import Updater
updater = Updater(token='216663815:AAHS1Wfu-PM1Q9cozBhPv1VTMiK64sqk0PY')
dispatcher = updater.dispatcher

def start(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text="Pollo")

dispatcher.addTelegramCommandHandler('start', start)

update.start_polling()
