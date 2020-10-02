from youTube import YouTube
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import keyboardbutton
import logging

#Creating of the YouTube object for data retrieval
Knb22 = YouTube("Channel ID goes here","Google API KEY goes here")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


updater = Updater(token='Telegram bot token goes here')
disp = updater.dispatcher

#Runs when the bot is started by a user
def start(bot,updater):
	bot.send_message(chat_id=updater.message.chat_id, text="Welcome to the SubCountBot")
	kb = [['/youtube'],['/other']]
	reply_markup = telegram.ReplyKeyboardMarkup(kb)
	bot.send_message(chat_id=updater.message.chat_id, text="What do you want?", reply_markup=reply_markup)

#Provides commands that deal with YouTube
def youtube(bot,updater):
	kb = [['/views','/subscribers'],['/back']]
	reply_markup = telegram.ReplyKeyboardMarkup(kb)
	bot.send_message(chat_id=updater.message.chat_id, text="What would you like to check?", reply_markup=reply_markup)

#Function to return the number of views of the channel to the user
def views(bot,updater):
	bot.send_message(chat_id=updater.message.chat_id,text=Knb22.get_view_count())

#Function to return the number of subscribers of the channel to the user
def subs(bot,updater):
	bot.send_message(chat_id=updater.message.chat_id,text=Knb22.get_sub_count())

#Additional functionality to come soon.
def other(bot,updater):
	kb = [['/back']]
	reply_markup = telegram.ReplyKeyboardMarkup(kb)
	bot.send_message(chat_id=updater.message.chat_id, text="There's really nothing else so might as well just go back", reply_markup=reply_markup)

#Creates commands that can be handled by the program
youtube_handler = CommandHandler('youtube',youtube)
other_handler = CommandHandler('other',other)
subs_handler = CommandHandler('subscribers',subs)
views_handler = CommandHandler('views',views)
start_handler = CommandHandler('start',start)
back_handler = CommandHandler('back',start)

#Allows commands to be recognized by the bot
disp.add_handler(start_handler)
disp.add_handler(youtube_handler)
disp.add_handler(views_handler)
disp.add_handler(subs_handler)
disp.add_handler(back_handler)
disp.add_handler(other_handler)

updater.start_polling()
#Begins polling so the bot can be interacted with
print("Polling Started")
