import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio

TOKEN = os.getenv("BOT_TOKEN")  # токен бота из Render → Environment
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")  # id админа или группы

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message()
async def complaint(message: Message):
    """Обработка всех входящих сообщений"""
    if message.text:
        await bot.send_message(
            ADMIN_CHAT_ID,
            f"⚠️ Новая анонимная жалоба:\n{message.text}"
        )
        await message.answer("✅ Ваша жалоба отправлена анонимно!")
    else:
        await message.answer("⚠️ Пожалуйста, отправьте текстовую жалобу.")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
