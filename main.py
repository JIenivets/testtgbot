import logging
from aiogram import Bot, types, executor, Dispatcher


logging.basicConfig(level=logging.INFO)
bot = Bot(token="5129415684:AAHfrQbaoAe3pLPD8powCR28oswwY3-tk6U")
dp = Dispatcher(bot)


@dp.message_handler()
async def echo(message: types.Message):
   print(f'{message.date} {message.from_user.full_name}({message.from_user.id}) {message.text}')
   await message.answer(message.text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)