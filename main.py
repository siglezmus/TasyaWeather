import datetime
from references import *
import telebot
from weather import Weather
import time
import eventlet



def main():


    bot = telebot.TeleBot(bot_id);
    timeout = eventlet.Timeout(10)
    try:
        weather = Weather()
    except eventlet.timeout.Timeout:
        print("Timeout")
    finally:
        timeout.cancel()




    def send_msg():
        if ((datetime.datetime.now() - weather.last_weather_request).total_seconds() // 60 > update_time_in_minutes):
            bot.send_message(chat_id=ch_id, text="Сейчас обновлюсь")
            time.sleep(1)
            # bot.send_message(message.from_user.id, "Сейчас обновлюсь")
            weather.update()

        m = (weather.location + ", " + weather.time) + "\n" + \
            (weather.current_temperature + deg_celc + ", " + weather.description) + "\n" + \
            (
                    "Сегодня температура будет менятся от " + weather.lower_temperature + deg_celc + " до " + weather.upper_temperature + deg_celc) + "\n" + \
            ("Влажность: " + weather.humidity) + "\n" + \
            ("Вероятность осадков: " + weather.precipitation) + "\n"
        bot.send_sticker(chat_id=ch_id,data=weather.sticker_reference)
        bot.send_message(chat_id=ch_id, text=m)
        time.sleep(1)
        # bot.send_audio(chat_id=ch_id, audio=open('felicity.mp3', 'rb'))


    def reminder(context):
        context.job_queue.run_daily(send_msg(), context=ch_id, days=(0, 1, 2, 3, 4, 5, 6),
                                    time=time(hour=11, minute=1, second=10))

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if ((message.text == "/weather") | (message.text == "/weather@TasyaW_bot")):
            send_msg()

        elif ((message.text == "/help") | (message.text == "/help@TasyaW_bot")):
            bot.send_message(chat_id=ch_id, text="Меня зовут Тася и я всегда знаю прогноз погоды))")
            time.sleep(1)
            bot.send_message(chat_id=ch_id, text="Напиши /weather \n")
            time.sleep(1)
        elif ((message.text == "/felicity") | (message.text == "/felicity@TasyaW_bot")):
            bot.send_audio(chat_id=ch_id, audio=open('felicity.mp3', 'rb'))
            time.sleep(1)
        else:
            print()

    bot.polling(none_stop=True, interval=0)

main()


