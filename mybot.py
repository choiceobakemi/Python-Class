import telegram.ext
from nasaapi import Client
nasa = Client('Hd4MYPY2EcR5TIPsOs7c1Iy9sM7l6DCTMefIBW9q')




TOKEN = '5856586385:AAGihSVe1agviaUFaMS3_o9buE9mt2_ZqBc'



def start(update, context):
    update.message.reply_text(''' Бот, использующий API НАСА для поиска результатов по запросам''')

def content(update, context):
    update.message.reply_text('leave')

def handle_message(update, context):
    try:
        a = nasa.nivl.search(update.message.text)
        imagelink = a['collection']['items'][2]['href']
        done = a['collection']['items'][0]['data'][0]['description']
        update.message.reply_text(done)
    except:
        update.message.reply_text('мы не смогли найти ваш запрос')

updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler('content', content))

disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))

updater.start_polling()
updater.idle()
