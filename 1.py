from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS
import os
import logging

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Dictionary to store weather data
weather_data = {}

def fetch_weather(city_code, url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        soup = BS(response.content, 'html.parser')
        content = soup.select_one('#content')
        min_temp_element = content.select_one('.temperature .min')
        max_temp_element = content.select_one('.temperature .max')

        if min_temp_element and max_temp_element:
            min_temp = min_temp_element.text.strip().split()[1]
            max_temp = max_temp_element.text.strip().split()[1]
        else:
            min_temp = "N/A"
            max_temp = "N/A"

        weather_data[city_code] = (min_temp, max_temp)
    except requests.RequestException as e:
        logger.error(f"Error fetching weather data for {city_code}: {e}")
        weather_data[city_code] = ("N/A", "N/A")
    except Exception as e:
        logger.error(f"Error parsing weather data for {city_code}: {e}")
        weather_data[city_code] = ("N/A", "N/A")

def load_weather_data():
    urls = {
        "01": 'https://sinoptik.ua/погода-андижан',
        "02": 'https://sinoptik.ua/погода-бухара',
        "03": 'https://sinoptik.ua/погода-фергана',
        "04": 'https://sinoptik.ua/погода-джизак',
        "05": 'https://sinoptik.ua/погода-навои',
        "06": 'https://sinoptik.ua/погода-наманган',
        "07": 'https://sinoptik.ua/погода-карши',
        "08": 'https://sinoptik.ua/погода-нукус',
        "09": 'https://sinoptik.ua/погода-самарканд',
        "10": 'https://sinoptik.ua/погода-гулистан',
        "11": 'https://sinoptik.ua/погода-термез',
        "12": 'https://sinoptik.ua/погода-ташкент',
        "13": 'https://sinoptik.ua/погода-ургенч'
    }
    for city_code, url in urls.items():
        fetch_weather(city_code, url)

def city_buttons():
    return [
        [InlineKeyboardButton("📌 Andijon 📌", callback_data="01")],
        [InlineKeyboardButton("📌 Buxoro 📌", callback_data="02")],
        [InlineKeyboardButton("📌 Farg'ona 📌", callback_data="03")],
        [InlineKeyboardButton("📌 Jizzax 📌", callback_data="04")],
        [InlineKeyboardButton("📌 Navoiy 📌", callback_data="05")],
        [InlineKeyboardButton("📌 Namangan 📌", callback_data="06")],
        [InlineKeyboardButton("📌 Qarshi 📌", callback_data="07")],
        [InlineKeyboardButton("📌 Nukus 📌", callback_data="08")],
        [InlineKeyboardButton("📌 Samarqand 📌", callback_data="09")],
        [InlineKeyboardButton("📌 Sirdaryo 📌", callback_data="10")],
        [InlineKeyboardButton("📌 Surxondaryo 📌", callback_data="11")],
        [InlineKeyboardButton("📌 Toshkent 📌", callback_data="12")],
        [InlineKeyboardButton("📌 Urganch 📌", callback_data="13")],
    ]

def back_button():
    return [[InlineKeyboardButton("🔙", callback_data="back1")]]

def inline_handler(update, context):
    query = update.callback_query
    city_code = query.data
    if city_code == "back1":
        query.message.edit_text("Bu yerdan viloyatingizni tanglang", reply_markup=InlineKeyboardMarkup(city_buttons()))
    else:
        min_temp, max_temp = weather_data.get(city_code, ("N/A", "N/A"))
        query.message.edit_text(f"Bugun {city_code} shaxrida havo harorati: {min_temp}C | {max_temp}C", reply_markup=InlineKeyboardMarkup(back_button()))

def start(update, context):
    update.message.reply_text("Salom! Bu yerdan viloyatingizni tanglang", reply_markup=InlineKeyboardMarkup(city_buttons()))

def main():
    load_weather_data()
    Token ="7556345182:AAENmlDcesvrALhyOh1FHS7oDSgqFxLU34Q"  # Use environment variable for the token
    updater = Updater(Token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(inline_handler))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
