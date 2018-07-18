#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.

This program is dedicated to the public domain under the CC0 license.

This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
Welcome new KRONOS Fans! 👽👽

Our team (including the founders) is available to answer any questions regarding KRONOS and to keep you updated about our newest developments.
''')

def kronos(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
KRONOS seeks to revolutionize the asset management space by equalizing access to the most exclusive investment strategies globally. We have formed a supportive ecosystem of talented traders, entrepreneurs and marketers to bring our vision to market.

With the KRON token, users can access all of our services from market-making, asset management and block trade execution to market insights. So whether you are a crypto exchange, fund, project or investor, you can do more with Kronos on your side!

''')

def social(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
English Telegram: https://t.me/KRONOS_E
Chinese Telegram: https://t.me/Kronos_C
Airdrop discussion: https://t.me/KRONOS_Airdrop
Official announcement: https://t.me/KronosToken
Facebook: https://www.facebook.com/kronostoken/
Twitter: https://twitter.com/kronostoken
LinkedIn: https://www.linkedin.com/company/kronostoken/
Reddit: https://www.reddit.com/r/kronostoken/
''')

def admins(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
⚡️Official Admins:
Mark - @markpimentel
Jack - @jaxonomy
Ran - @ranyi1115
Wenwen - @wenwen000
Jennifer - @wangthewhale
Joe - @Jscherp

⚡️Community Managers:
Shawn - @Shawntw
Zane - @krypto_max

''')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def rules(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
• Don't talk about Airdrop
• We are privately funded, and not onboarding any new capital from the chat room!
• Please keep discussions around Kronos developments, Solidity development, and things that add value to our ecosystem.
• Spam advertisements / adult content = immediate ban.
• Please keep discussions polite and constructive.''')

def wp(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
⚡️Official website: https://kronostoken.com/

✨Whitepaper username: kronos
✨password: KRONOS99

''')

def the_most_awesome_project(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('''
KRONOS for sure!!!!!!!!!!!!🚀🌕
''')



def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("678188631:AAFHkfaMpURE6MzBu9ndpyNY5nC8hsBRjAQ")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    # dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("whatkronos", kronos))
    dp.add_handler(CommandHandler("socialmedia", social))
    dp.add_handler(CommandHandler("admins", admins))
    dp.add_handler(CommandHandler("wp", wp))
    dp.add_handler(CommandHandler("the_most_awesome_project", the_most_awesome_project))
    # on noncommand i.e message - echo the message on Telegram
    # dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
