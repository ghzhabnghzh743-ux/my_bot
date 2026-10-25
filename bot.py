import telebot

TOKEN = '8268530046:AAEbRXyRb9rSExiiWlW8BEWXmmY8VvQlabw'
bot = telebot.TeleBot(8268530046:AAEbRXyRb9rSExiiWlW8BEWXmmY8VvQlabw")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send the target UID to get the fix instructions.")

@bot.message_handler(func=lambda message: True)
def handle_uid(message):
    target_uid = message.text.strip()
    if target_uid.isdigit():
        instructions = (
            f"Target UID: {target_uid}\n\n"
            "To clear the graveyard and stop the spam:\n"
            "1. Open the game and go to Settings.\n"
            "2. Tap on Privacy.\n"
            "3. Change Team/Room Invites to 'Friends Only' or 'Reject'.\n\n"
            "The spam will stop immediately!"
        )
        bot.reply_to(message, instructions)
    else:
        bot.reply_to(message, "Please send a valid numeric UID.")

if __name__ == '__main__':
    print("Bot is running...")
    bot.infinity_polling()
