import pyshorteners
import validators
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Welcome to URL Shortener Bot! Send me a long URL and I'll shorten it for you.")

def shorten_url(update, context):
    url = update.message.text
    if not validators.url(url):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Error: Please enter a valid URL.")
        return
    try:
        shortener = pyshorteners.Shortener()
        short_url = shortener.tinyurl.short(url)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Here's your shortened URL: {short_url}")
    except Exception as e:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"Error: {e}")

def main():
    # Set up the updater and add handlers
    updater = Updater(token="REPLACE_WITH_YOUR_TOKEN", use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    url_handler = MessageHandler(Filters.text & (~Filters.command), shorten_url)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(url_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
