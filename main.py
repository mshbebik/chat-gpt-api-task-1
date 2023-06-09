import os
import openai
import telebot
import telebot
import requests
import json




# Імпорт телеграм бота, вставте свій токен
bot = telebot.TeleBot('API-TOKEN')
openai.api_key = "API-TOKEN"


# Стартова функція запуску бота 
@bot.message_handler(commands=['start'])
def send_welcome(message): 
    bot.send_message(message.chat.id, text="Задайте питання на яке хотілиб отримати відповідь від ChatGPT")


# функція котра приймає написане користувачем місто, записує його до зміннної, потім виводить список по вказаному місту
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    while True:
        theme = message.text
        messages = [{"role": "user", "content": theme}]
    
        completion = openai.ChatCompletion.create(
        model="text-davinci-002",
        messages=messages
        )

        chat_response = completion.choices[0].message.content
        bot.send_message(message.chat.id, text=f"ChatGPT: {chat_response}")
        messages.append({"role": "assistant", "content": chat_response})






bot.infinity_polling()