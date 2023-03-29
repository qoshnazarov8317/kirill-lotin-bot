from transliterate import to_cyrillic, to_latin
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton , InlineKeyboardMarkup

TOKEN = "5985962196:AAG2N84aydv7bm38ROnQzsQlQ41RheIf6ME"
logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    user = message['chat'] ["first_name"]
    matn = f"Assaomu alaykum {user} botimizga xush kelibsiz.\nBu botda so'zlar yoki matinlarni lotindan-kirillga, kirilldan-lotinga o'girishingiz mumkin.\nMatn kiriting:"
    await message.reply(matn)

@dp.message_handler()
async def echo(message: types.Message):
	a = message["text"]
	if a.isascii():
		javob = to_cyrillic(a)
	else:
		javob = to_latin(a)
	await message.answer(text=f"<code>{javob}</code>", parse_mode="HTML")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)