import random

class KNB:
    bot.send_message(chat_id, text="запуск игры..")
    bot.send_message(chat_id, text="Камень, ножницы или бумага? Напишите ваш выбор или выйдите с помощью команды *Главное меню*")

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        chat_id = message.chat.id
        ms_text = message.text

    vibor = ["камень", "бумага", "ножницы"]
    choiseC = random.choice(vibor)
    print(choiseC)

    if ms_text == "Камень" or "камень":

        a = ms_text.lower

        if choiseC == a:
            bot.send_message(chat_id, text="ничья")
        elif choiseC == a:
            bot.send_message(chat_id, text="Вы проиграли")
        else:
            bot.send_message(chat_id, text="Вы победили")

    elif ms_text == "Бумага" or "бумага":

        a = ms_text.lower

        if choiseC == a:
            bot.send_message(chat_id, text="ничья")
        elif choiseC == a:
            bot.send_message(chat_id, text="Вы проиграли")
        else:
            bot.send_message(chat_id, text="Вы победили")

    elif ms_text == "Ножницы" or "ножницы":

        a = ms_text.lower

        if choiseC == a:
            bot.send_message(chat_id, text="ничья")
        elif choiseC == a:
            bot.send_message(chat_id, text="Вы проиграли")
        else:
            bot.send_message(chat_id, text="Вы победили")

    else: bot.send_message(chat_id, text="Либо я тупой, либо Вы допустили ошибку")























