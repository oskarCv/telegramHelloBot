from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command

start_router = Router()

# Define the command handler
@start_router.message(Command(commands="start"))
async def start_command_handler(message: Message):
    await message.answer(
        "👋 Welcome to the Crypto Signals Subscription Bot!\n\n"
        "This bot will help you subscribe to crypto signals so you can plan your trading with deeper knowledge.\n\n"
        "Here are the commands I understand:\n"
        "/subscribe - Generate a link to make a payment for the subscription.\n"
        "/validate - Validate your transaction after payment.\n"
        "/help - Get help on how to use this bot.",
        parse_mode="HTML"
    )