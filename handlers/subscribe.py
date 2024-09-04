from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

subscribe_router = Router()

@subscribe_router.message(Command(commands='subscribe'))
async def subscribe_handler(message: Message):
    web_app = WebAppInfo(url="https://oskarcv.github.io/sample-gh-pages/")
    button = InlineKeyboardButton(text="Subscribe", web_app=web_app)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])

    await message.answer("Click the button to subscribe:", reply_markup=keyboard)