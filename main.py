import telegram

# Replace YOUR_TOKEN_HERE with your bot token
bot = telegram.Bot(token='5993587987:AAH0yL0tqROch-LB29hvEoYNTBFjR4p_2L8')

# Replace YOUR_CHAT_ID_HERE with the chat_id of the user you want to send the message to
chat_id = 407712064

# Send the message "Hello" to the user with chat_id = YOUR_CHAT_ID_HERE
bot.send_message(chat_id=chat_id, text='Hello')
