from aiogram import Dispatcher, Bot
import asyncio
from config import TOKEN
from handler.commands import command_router
from handler.commands import callbacks_router
dp = Dispatcher()
dp.include_router(command_router)
dp.include_router(callbacks_router)
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())