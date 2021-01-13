import telegram
token='1585093264:AAEWaF4iUSU5SifZSWVHT2Tyt6aBqw4LRdM'
bot = telegram.Bot(token=token)

#search token
for i in bot.getUpdates():
    print(i.message)


#send message s
bot.sendMessage(chat_id='1396571541', text='1')