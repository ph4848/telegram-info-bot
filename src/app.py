import telebot
import base
import app_api

bot = telebot.TeleBot(base.token)

print("bot created ...")

@bot.message_handler(commands=["start"])
def say_hello(message):
    bot.send_message(message.chat.id, text="بات آماده دستورات شماست")

@bot.message_handler(commands=["help", "support"])
def say_help(message):
    bot.send_message(message.chat.id, text="با پشتیبانی تماس بگیرید")

@bot.message_handler(commands=["news"])
def show_news(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)

    btn_1 = telebot.types.InlineKeyboardButton(text="اخبار ورزشی", url="https://varzesh3.com")
    btn_2 = telebot.types.InlineKeyboardButton(text="اخبار عمومی", url="https://entekhab.ir")
    btn_3 = telebot.types.InlineKeyboardButton(text="اخبار اقتصادی", url="https://tradigview.com")

    markup.add(btn_1, btn_2, btn_3)

    bot.send_message(message.chat.id, text="یکی از گزینه های زیر را انتخاب کنید", reply_markup=markup)

@bot.message_handler(commands=["menu"])
def show_menu(message):
    print(message)
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)

    btn_1 = telebot.types.ReplyKeyboardButton(text="تماس با ما")
    btn_2 = telebot.types.ReplyKeyboardButton(text="درباره ما")
    btn_3 = telebot.types.ReplyKeyboardButton(text="تعیین هویت")
    btn_4 = telebot.types.ReplyKeyboardButton(text="بازگشت")

    markup.add(btn_1, btn_2, btn_3, btn_4)

    bot.send_message(message.chat.id, text="یکی از گزینه های زیر را انتخاب کنید", reply_markup=markup)

@bot.message_handler(commands=["movie"])
def show_message_1(message):
    msg = bot.send_message(message.chat.id, text="آیدی فیلم مورد نطر را وارد کنید")
    bot.register_next_step_handler(msg, get_movie_info)

def get_movie_info(message):
    movie_id = message.text
    result = app_api.get_movie_info_by_id(movie_id)
    bot.send_message(message.chat.id, text=f"{result[0]} / {result[-1]}")

@bot.message_handler(commands=["movie_name"])
def show_message_2(message):
    msg = bot.send_message(message.chat.id, text="نام فیلم مورد نطر را وارد کنید")
    bot.register_next_step_handler(msg, get_movie_info_by_name)

def get_movie_info_by_name(message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    bot.send_message(message.chat.id, text=f"{result[0]} / {result[-1]}")

@bot.message_handler(func=lambda message:True)
def handle_all_messages(message):
    if message.text == "تماس با ما":
        email = "support1545@gmail.com"
        phone = "09123651425"
        post_box = "2312453"
        info = f" : ایمیل {email} : شماره تماس / {phone} : صندوق پستی / {post_box} "

        bot.send_message(message.chat.id, text=info)

    elif message.text == "درباره ما":
        bot.send_message(message.chat.id, text="یک گروه آموزشی با ایده هایی روشن")
    elif message.text == "تعیین هویت":
        bot.send_message(message.chat.id, text="یکی از فرمت های (عادی / یکساله / نامحدود) را انتخاب کنید")
    elif message.text == "بازگشت":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text="به منوی اصلی بازگشتید", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="منظور شما را متوجه نشدم! دوباره تلاش کنید")

if __name__ == "__main__":
    bot.infinity_polling()
