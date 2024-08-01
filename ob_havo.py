from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests
from bs4 import BeautifulSoup as BS
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.client.session.aiohttp import AiohttpSession


session = AiohttpSession(proxy="http://proxy.server:3128")
print(session)


# toshkent shahri
t = requests.get('https://sinoptik.ua/погода-ташкент')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    t_min = min[4:]
    t_max = max[5:]
#Andijon
a = requests.get('https://sinoptik.ua/погода-андижан')
html_a = BS(a.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    a_min = min[4:]
    a_max = max[5:]

#Buxoro shahri
b = requests.get('https://sinoptik.ua/погода-бухара')
html_b = BS(b.content, 'html.parser')

for el in html_b.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    b_min = min[4:]
    b_max = max[5:]
#Farg'ona shahri
f = requests.get('https://sinoptik.ua/погода-фергана')
html_f = BS(f.content, 'html.parser')

for el in html_f.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    f_min = min[4:]
    f_max = max[5:]


#Jizzax shahri
t = requests.get('https://sinoptik.ua/погода-джизак')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    j_min = min[4:]
    j_max = max[5:]


#Navoiy shahri
t = requests.get('https://sinoptik.ua/погода-навои')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    n1_min = min[4:]
    n1_max = max[5:]


#Namangan shahri
t = requests.get('https://sinoptik.ua/погода-наманган')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    n2_min = min[4:]
    n2_max = max[5:]


#Qarshi shahri
t = requests.get('https://sinoptik.ua/погода-карши')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    q1_min = min[4:]
    q1_max = max[5:]

#Nukus shahri
t = requests.get('https://sinoptik.ua/погода-нукус')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    q2_min = min[4:]
    q2_max = max[5:]



#Samarqand shahri
t = requests.get('https://sinoptik.ua/погода-самарканд')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    s1_min = min[4:]
    s1_max = max[5:]

#Guliston shahri
t = requests.get('https://sinoptik.ua/погода-гулистан')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    s2_min = min[4:]
    s2_max = max[5:]


#Termiz shahri
t = requests.get('https://sinoptik.ua/погода-термез')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    s3_min = min[4:]
    s3_max = max[5:]
#Urganch shahri
t = requests.get('https://sinoptik.ua/погода-ургенч')
html_t = BS(t.content, 'html.parser')

for el in html_t.select('#content'):
    min = el.select('.temperature .min')[0].text
    max = el.select('.temperature .max')[0].text
    x_min = min[4:]
    x_max = max[5:]
#shaharlar tugmasi
def city():
    return [
    [InlineKeyboardButton("📌 Andijon 📌", callback_data=f"01")],[InlineKeyboardButton("📌 Buxoro 📌", callback_data=f"02")],
    [InlineKeyboardButton("📌 Farg'ona 📌", callback_data=f"03")],
    [InlineKeyboardButton("📌 Jizzax 📌", callback_data=f"04")],
    [InlineKeyboardButton("📌 Navoiy 📌", callback_data=f"05")],
    [InlineKeyboardButton("📌 Namangan 📌", callback_data=f"06")],
    [InlineKeyboardButton("📌 Qashqadaryo 📌", callback_data=f"07")],
    [InlineKeyboardButton("📌 Qoraqolg'iston Respublikasi 📌", callback_data=f"08")],
    [InlineKeyboardButton("📌 Samarqand 📌", callback_data=f"09")],
    [InlineKeyboardButton("📌 Sirdaryo 📌", callback_data=f"010")],
    [InlineKeyboardButton("📌 Surxondaryo 📌", callback_data=f"011")],
        [InlineKeyboardButton("📌 Toshkent 📌", callback_data=f"012")],
        [InlineKeyboardButton("📌 Xorazm 📌", callback_data=f"013")],
    ]

#orqaga qaytish tugmasi
def back():
    return [
        [InlineKeyboardButton("🔙", callback_data=f"back1")]
    ]

#Shahrlar tugmasiga javob
def inline_handlerlar(update, context):
    query = update.callback_query
    data = query.data.split("_")
#Buxoro
    if data[0] == "02":
        query.message.edit_text(f"Bugun Buxoro shaxrida havo harorati\n {b_min}C | "
                                f"{b_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
#Abdijon
    if data[0] == "01":
        query.message.edit_text(f"Bugun Andijon shaxrida havo harorati\n {a_min}C | "
                                f"{a_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
#Farg'ona    
    if data[0] == "03":
        query.message.edit_text(f"Bugun Farg'ona shaxrida havo harorati\n {f_min}C | "
                                f"{f_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back())) 
                                
    if data[0] == "04":
        query.message.edit_text(f"Bugun Jizzax shaxrida havo harorati\n{j_min}C | "
                                f"{j_max} \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))                           
    
    if data[0] == "05":
        query.message.edit_text(f"Bugun Navoiy shaxrida havo harorati\n {n1_min}C | "
                                f"{n1_max} C\nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    if data[0] == "06":
        query.message.edit_text(f"Bugun Namangan shaxrida havo harorati\n {n2_min}C | "
                                f"{n2_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
   
    if data[0] == "08":
        query.message.edit_text(f"Bugun Nukus shaxrida havo harorati\n {q2_min}C |  "
                                f"{q2_max} C\nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
     
    if data[0] == "07":
        query.message.edit_text(f"Bugun Qarshi shaxrida havo harorati\n {q1_min}C |  "
                                f"{q1_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
        
    if data[0] == "09":
        query.message.edit_text(f"Bugun Samarqand shaxrida havo harorati\n {s1_min}C | "
                                f"{s1_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    if data[0] == "010":
        query.message.edit_text(f"Bugun Sirdaryo shaxrida havo harorati\n {s2_min}C | "
                                f"{s2_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    if data[0] == "011":
        query.message.edit_text(f"Bugun Termiz shaxrida havo harorati\n {s3_min}C | "
                                f"{s3_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    if data[0] == "012":
        query.message.edit_text(f"Bugun Toshkent shaxrida havo harorati\n {t_min}C | "
                                f"{t_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    if data[0] == "013":
        query.message.edit_text(f"Bugun Urganch shaxrida havo harorati\n {x_min}C | "
                                f"{x_max}C \nbo`lishi kutilmoqda ⛅",
                                reply_markup=InlineKeyboardMarkup(back()))
    
    elif data[0] == 'back1':
        query.message.edit_text(
            f"Bu yerdan vilayatingizni tanglang",
            reply_markup=InlineKeyboardMarkup(city()))



#startga javob
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"""Salom {user.first_name} \nBu yerdan viloyatingizni tanglang""",
                              reply_markup=InlineKeyboardMarkup(city()))




#ishga tushuruvchi
def main():
    Token = "7233333208:AAEVwe_gzhgdNAuB1bzk71NFbb-R8zWuFP4"
    updater = Updater(Token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(inline_handlerlar))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

# Davomini o`zingiz mustaqil bajaring!!!
