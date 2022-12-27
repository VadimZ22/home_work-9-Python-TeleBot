from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config import TOKEN
import input_output as io

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
async def on_startup(_):
    print('Bot is running...')

@dp.message_handler(commands=['start', 'help'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЯ умею вести телефонный справочник!\n"
                        "Внесите данные в формате: ФИО №телефона комментарий\n"
                        "или создайте запрос с ключевым словом 'найти'(пример: найти Зубенко Вадим)")


@dp.message_handler()
async def action(message: types.Message):
    if 'найти' in message.text:
        response = io.output_data(message.text.replace('найти', '').strip())
        if type(response) == list:
            for i in response:
                await message.answer(i)
        else: await message.answer(response)


    else:
        response = io.input_data(message.text)
        await message.answer(response)




# await message.answer(message.text)
# await message.reply(message.text)
#await bot.send_message(message.from_user.id, message.text)

# @dp.message_handler(commands=['меню'])
# async def menu_command(message: types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)







