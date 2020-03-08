import datetime
from references import *
import telebot;
from weather import Weather
import MyThread



### init ###
bot = telebot.TeleBot(bot_id);
weather = Weather()

def send_msg():
    if ((datetime.datetime.now() - weather.last_weather_request).total_seconds() // 60 > update_time_in_minutes):
        bot.send_message(chat_id=ch_id, text="Сейчас обновлюсь")
        # bot.send_message(message.from_user.id, "Сейчас обновлюсь")
        weather.update()

    m = (weather.location + ", " + weather.time) + "\n" + \
        (weather.current_temperature + deg_celc + ", " + weather.description) + "\n" + \
        (
                "Сегодня температура будет менятся от " + weather.lower_temperature + deg_celc + " до " + weather.upper_temperature + deg_celc) + "\n" + \
        ("Влажность: " + weather.humidity) + "\n" + \
        ("Вероятность осадков: " + weather.precipitation) + "\n" + \
        ("Sticker placeholder")
    bot.send_message(chat_id=ch_id, text=m)
    bot.send_audio(chat_id=ch_id, audio=open('felicity.mp3', 'rb'))

#timer_thread = MyThread.MyThread()
#timer_thread.start()
### end ###

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/weather":
        send_msg()
        #bot.send_message(message.from_user.id, m)

    elif(message.text == "/help"):
        print()
        bot.send_message(chat_id=ch_id, text = "Меня зовут Тася и я всегда знаю прогноз погоды))")
        bot.send_message(chat_id=ch_id, text = "Напиши /weather \n")
    else:
        print()


bot.polling(none_stop=True, interval=0)



