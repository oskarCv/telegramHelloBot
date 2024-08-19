import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import BotCommand

from handlers.start import start_router
from handlers.subscribe import subscribe_router

ssm = boto3.client('ssm', region_name='us-east-2')
BOT_TOKEN = ssm.get_parameter(Name='TELEGRAM_TOKEN', WithDecryption=True)['Parameter']['Value']

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Include the router for subscribe commands
    dp.include_router(start_router)
    dp.include_router(subscribe_router)

    # Set bot commands
    await bot.set_my_commands(
        [
            BotCommand(command="start", description="Start the bot"),
            BotCommand(command="subscribe", description="Subscribe to the service"),
        ]
    )

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())