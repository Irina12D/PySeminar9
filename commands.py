from bot_config import bot, dp
from aiogram import types
from random import randint as rnd

total = 150
max_to_take = 28

description_game = f'Я крутой и уверенный в себе бот и могу легко обыграть тебя, поэтому первый ход всегда делаешь ты. ' \
                   f'Мы ходим по очереди. За один ход можно забрать не более 28 камней. ' \
                   f'Выигрывает тот, кто заберёт последние бриллианты из банка. '\
                   f'Все бриллианты оппонента достаются сделавшему последний ход. Итак, начинай!'



@dp.message_handler(commands=['start'])
async def start_bot(msg: types.Message):
    await bot.send_message(msg.from_user.id, text=f'{msg.from_user.first_name}'
                                                  f', да ладно! Круто! Ну, погнали! ' + description_game)
    global total
    total = 150


@dp.message_handler()
async def get_text_messages(msg: types.Message):
    global total
    if msg.text.isdigit():
        if 1 <= int(msg.text) <= min(max_to_take, total):
            total -= int(msg.text)
            await bot.send_message(msg.from_user.id, f'{msg.from_user.first_name}'
                                                     f', взял(а) {msg.text} бриллианта(ов)')
            if total > max_to_take:
                await bot.send_message(msg.from_user.id, f'В банке драгоценностей осталось {total} бриллианта(ов)')
            else:
                await bot.send_message(msg.from_user.id, f'Игра окончена! '
                                                         f'{msg.from_user.first_name}, ты проиграл(а) :( Все бриллианты остаются у меня!')
                await bot.send_message(msg.from_user.id, f'Но от меня никто не уходит с пустыми руками! '
                                                         f'Пусть не бриллианты, но десерт сандей «Frrrozen Haute Chocolate» за $25000, '
                                                         f'думаю, порадует тебя, {msg.from_user.first_name}. Наслаждайся!')

                photo = open('samoe_dorogoe_morozhenoe_v_mire.jpg', 'rb')
                await bot.send_photo(msg.from_user.id, photo)

                return

            if total - max_to_take == 29:
                motion = total - max_to_take
            else:
                motion = rnd(1, min(max_to_take, total))
                while total - motion <= max_to_take:
                    motion = rnd(1, min(max_to_take, total))
            total -= motion
            await bot.send_message(msg.from_user.id, f'Мой ход. Я забрал {motion} бриллианта(ов)')
            if total > max_to_take:
                await bot.send_message(msg.from_user.id, f'В банке драгоценностей осталось {total} бриллианта(ов)')
                await bot.send_message(msg.from_user.id, f'{msg.from_user.first_name}, твой ход')
            else:
                await bot.send_message(msg.from_user.id, f'Игра окончена! '
                                                         f'{msg.from_user.first_name}, ты  победил(а)! Все бриллианты твои!')
                await bot.send_message(msg.from_user.id, f'Для меня это неожиданно! Что ж, скрашу свою печаль конфетами.'
                                                         f'Угощайся и ты, {msg.from_user.first_name}!')

                photo = open('Candies.png', 'rb')
                await bot.send_photo(msg.from_user.id, photo)

                return
        else:
            await msg.answer(f'Можно забирать не менее 1 и не более {max_to_take} камней. '
                             f'Сейчас всего {total} бриллиантов. Вводи заново!')

