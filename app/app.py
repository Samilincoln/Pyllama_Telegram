import os 
import json
import telebot
from dotenv import load_dotenv
from groq import Groq

from flask import Flask, request
import requests

app = Flask(__name__)

load_dotenv()
API_KEY = os.environ.get("TELEGRAM_API_KEY")
#client = Groq(api_key="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")

def get_groq_response(content):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"),)

    #jsn_content = json.dumps(content)

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "Do not repeat the question, then you answer the query and be very conversational"
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-70b-8192",
    )

    return str((chat_completion.choices[0].message.content))



bot = telebot.TeleBot(API_KEY)
bot.remove_webhook()





'''@bot.message_handler(commands=["start", "help"])
def send_start_help_message(message):
    bot.reply_to(message, "Hello this is PyLLAma, How can I help you today")'''

@bot.message_handler(func=lambda message: True)
def all_other_messages(message):
    response = get_groq_response(message.text)
    bot.reply_to(message, str(response))



@app.route('/api/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data(as_text=True)
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'OK', 200
    #bot.infinity_polling()
    #return ("Bot is up and running")


def set_webhook():
    webhook_url = 'https://your-vercel-project.vercel.app/api/webhook'
    response = requests.get(
        f'https://api.telegram.org/bot{os.getenv("TELEGRAM_API_KEY")}/setWebhook?url={webhook_url}'
    )

    if response.json().get("ok"):
        print('Webhook set successfully')
    else:
        print('Error setting webhook:', response.json().get("description"))


    


if __name__ == '__main__':
    set_webhook()
    app.run(debug=True)

    