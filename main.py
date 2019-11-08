#!/usr/bin/env python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging 
import requests
import re

update_id = None

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def get_verse():
    """Access the verse using the API."""
    contents = requests.get('http://www.ourmanna.com/verses/api/get?format=json&order=random&type=json').json()
    bible_verse = contents['verse']['details']['text'] + " - "  + contents['verse']['details']['reference'] + " (" + contents['verse']['details']['version'] + ")"
    return bible_verse

def start(bot, update):
    """Send a message when the command /start is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Hello, and God bless you!')

def verse(bot, update):
    """Send a RandomBibleVerse when the command /verse is issued."""
    my_verse = get_verse()
    id_chat = update.message.chat_id
    bot.send_message(chat_id=id_chat, text=my_verse)

def wrong_command(bot, update):
    """Send a message when a noncommand is issued."""
    bot.send_message(chat_id=update.message.chat_id, text='Incorrect Command: Type /verse for a verse.')

def error(bot, update):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', bot, update.error)

def main():
    # Create updater to pass in the bot's token
    updater = Updater('TOKEN') ## TO-DO: udpate with your own token generated from the Telegram Bot
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    
    # On different commands, answer in Telegram
    dp.add_handler(CommandHandler('verse', verse))
    dp.add_handler(CommandHandler('start', start))
    
    # on noncommands, tell user to try a different 
    dp.add_handler(MessageHandler(Filters.text, wrong_command))
    
    # log all errors 
    dp.add_error_handler(error)

    # Start the Bot and run until Ctrl-C
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
