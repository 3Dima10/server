#######################################################
# """___________________Маша сервер________________"""#
#######################################################
import logging
from aiogram import Dispatcher, Bot, executor, types

logging.basicConfig(level=logging.INFO)
bot = Bot(token="5672305585:AAFc-6Y5tB0jYyvIt6WUBp8R6XzOFkBSH0o")
dp = Dispatcher(bot)  # токен 


#######################################################
# """___________________Старт_______________________"""#
#######################################################
@dp.message_handler(commands=['start'])  # запуск бота
async def start(message):
    sto = open('фото.png', 'rb')  # преветственая клавиатура
    await bot.send_photo(message.chat.id, sto)
    # клавиатура
    clav = types.ReplyKeyboardMarkup(resize_keyboard=True)
    it1 = types.KeyboardButton("Помолиться🙏 ")  # кнопка 1
    it2 = types.KeyboardButton("Пожертвовать богине 💸 ")  # кнопка 2

    clav.add(it1, it2)

    # Приветствие
    await bot.send_message(message.chat.id,
                           f"Добро пожаловать прихожанин, <b>{message.from_user.full_name}!</b>\n Я - <b>Mary temple</b>, бот храм созданный для того, чтобы служить нашей богини Марий.",
                      parse_mode='html', reply_markup=clav)


#############################################################
# ""_____________________Обычные Кнопки___________________""#
#############################################################

@dp.message_handler(content_types=['text'])  # обработчик сообщений
async def lop(message):
    dop = open('икона1.png', 'rb')  # Икона
    col = open('икона2.png', 'rb')  # Икона
    # платеж стикер
    cod = open('stickes.webp', 'rb')
    if message.chat.type == 'private':

        # ""_____Помолица_____""
        if message.text == 'Помолиться🙏':  # Зачения кнопки помолица

            kls = types.InlineKeyboardMarkup(
                row_width=1)  # клавиатура номер два
            # Значение клавиатура номер два
            itm = types.InlineKeyboardButton(
                "Отпустить грех ", callback_data='good')

            kls.add(itm)  # Клавиатура номер два

            await bot.send_photo(message.chat.id, dop)  # Иконы для молитвы
            await bot.send_photo(message.chat.id, col)  # Иконы для молитвы
            await bot.send_message(message.chat.id, str("Царица моя Преблагая, Надежда моя, Богородица,\n"
                                                  "Приют сирот и странников Защитница, скорбящих Радость,\n"
                                                  "Обиженных Покровительница!\n"
                                                  "Видишь мою беду, видишь мою скорбь;\n"
                                                  "Помоги мне, как немощному, направь меня, как странника.\n"
                                                  "Обиду мою знаешь: разреши ее по Своей воле."),
                             reply_markup=kls)  # Ответ на кнопку помалица Молитва

            # ""_____Пожертвовать 💳_____""

        elif message.text == 'Пожертвовать богине 💸':  # Пожертвувание
            dc = types.InlineKeyboardMarkup(row_width=1)
            ito = types.InlineKeyboardButton(
                "Пожертвовать 💳 ", callback_data='gool')
            dc.add(ito)
            await bot.send_sticker(message.chat.id, cod)  # Стикер пожертв
            await bot.send_message(message.chat.id, str("Пожертвуй богини 🙏\n"
                                                  "И она спустит на тебя удачу😇\n"
                                                  "И отпустит сразу все грехи😇"),
                             reply_markup=dc)  # ответ на пожертвовать
        else:
            # на случай если воспользуюце не клавиатурой
            await bot.send_message(message.chat.id, "Пишы правильно еретик")


####################################################################
# ""_____________________Инлайновая клавиатура___________________""#
####################################################################

@dp.callback_query_handler(lambda query: True)
async def callback_inline(call):
    try:
        if call.message:

            # ""______Помолиться______""

            if call.data == 'good':  # Инлайтова клавиатура помолица
                # после нажатия текст
                await bot.send_message(call.message.chat.id, 'Грех отпущен')
                await bot.edit_message_text(chat_id=call.message.chat.id,
                                      message_id=call.message.message_id,
                                      text="Молива окончена",
                                      reply_markup=None)  # замена кнопки инлайтовой клавиатуры
                await bot.answer_callback_query(callback_query_id=call.id,
                                          show_alert=False,
                                          text="Грех отпущен")

                # ""______Пожертвовать______""

            if call.data == 'gool':
                await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="5355280002536686")
                await bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Да неспашлет богиння на тебя удачу ")

    # ""______Поиск ошыбок______""

    except Exception as e:
        print(repr(e))  # поиск ошыбок


#####################################################
# ""_____________________Запуск___________________""#
#####################################################
try:
    if __name__ == "__main__":
        print("Бот 'Храм Машы' запущен проблем нет")
        executor.start_polling(dp, skip_updates=True)
except Exception as e:
    print(repr(e))
