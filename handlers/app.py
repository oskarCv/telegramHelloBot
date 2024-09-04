import requests
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

app_router = Router()

@app_router.message(Command(commands='app'))
async def launch_app_handler(message: Message):
    """
    Handler para abrir la aplicación web al recibir el comando /app.

    Args:
        message (Message): Objeto de mensaje de Telegram.
    """

    # Mensaje de confirmación al usuario
    await message.answer("¡Abriendo la aplicación web! ")

    # Opción 1: Abrir directamente el enlace (recomendado para la mayoría de los casos)
    await message.answer_url("https://oskarcv.github.io/sample-twa-react/")

    # Opción 2: Crear un botón personalizado con el enlace (más flexible)
    # keyboard = InlineKeyboardMarkup(row_width=1)
    # button = InlineKeyboardButton(text="Abrir Aplicación", url="https://oskarcv.github.io/sample-twa-react/")
    # keyboard.add(button)
    # await message.answer("¿Quieres abrir la aplicación?", reply_markup=keyboard)