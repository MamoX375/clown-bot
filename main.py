import os
import telebot

# ضع هنا التوكن الخاص بك الذي أعطاك إياه BotFather
TOKEN = '8910190517:AAG253zzoVVbMnCbG1H4_WEx7ZB86dh91bE'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    reply_text = (
        f"⚠️ **تحذير نظامي خطير** ⚠️\n\n"
        f"مرحباً بك يا {user_name}.\n"
        f"تم رصد عملية طلب المنتج: **Giggles the Clown** ($1,300).\n"
        f"جاري تأكيد عنوان IP الخاص بك وتجهيز الشحنة لتصل إليك tonight at 9 A.M...\n\n"
        f"💀 لا يمكنك التراجع عن الطلب!"
    )
    bot.reply_to(message, reply_text, parse_mode="Markdown")

print("البوت يعمل الآن على السحاب...")
bot.infinity_polling()