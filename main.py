# Importing Telegram Bot API Library
import telebot
from datetime import datetime

currentDateAndTime = datetime.now()
# Setting up token
bot_token = '6231433718:AAEZZwxnshxxO0-IXJZPYdnr5Ckk_T0xOGk'
bot = telebot.TeleBot(bot_token)

hi = ["hi","hello","what's_up","good_morning"]
name = ["what's_your_name", "what_is_your_name", "name", "who_are_you",]
build = ["who_made_you?", "who_build_you?", "who_made_you", "who_build_you"]
year = ["how_old_are_you"]
time = ["what's_the_time","what_is_the_time","what's_the_time_now","what_is_the_time_now"]
song = ["sing_for_me_a_song", "sing_song_for", "sing_song"]
beatbox = ["can_you_beatbox_for_me", "can_you_make_beatbox_for_me", "can_you_beatbox", "can_you_make_beatbox"]
love = ["i_love_you"]
date = ["what's_the_date","what_is_the_date","what's_the_date_today","what_is_the_date_today"]
# Create commands handler
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Hi! Welcome to my chatbot! \n Note:Replace any space with (_)')

# Create message handler
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    words = message.text.split()

    if words[0].lower() in hi :
        return bot.reply_to(message,"Hello!")

    if words[0].lower() in name :
        return bot.reply_to(message,"My Name Is (X Chat)")

    if words[0].lower() in build :
        return bot.reply_to(message,"X ChatBot Grope Build Me And they are my family 😊")

    if words[0].lower() in year :
        return bot.reply_to(message,"I Have 23 Years, and You?")

    if words[0].lower() in time :
        return bot.reply_to(message,currentDateAndTime.strftime("%H:%M"))
    
    if words[0].lower() in song :
        return bot.reply_to(message,"Don’t know much about history, don’t know much biology, don’t know much about a science book, don’t know much about the French I took. But I do know that I love you, and I know that if you loved me too what a wonderful world this would be.")

    if words[0].lower() in beatbox :
        return bot.reply_to(message,"Bom Bom, tack, Bom Bom Bom, tack, Bom Bom Bom Bom, tack")
    
    if words[0].lower() in love :
        return bot.reply_to(message,"Me Too 😍")

    if words[0].lower() in date :
        return bot.reply_to(message,currentDateAndTime.strftime("%d/%m/%Y"))    

    else:
        return bot.reply_to(message,"How Can I help You ?😀")
# Start the bot
bot.polling()
