from aiogram import Router, types
from aiogram.types import Message
from aiogram.filters import Command

subscribe_router = Router()

# Define the command handler
@subscribe_router.message(Command(commands="subscribe"))
async def subscribe_handler(message: Message):
    text = (
        "<b>Subscribe to Our Service</b>\n\n"
        "To subscribe, please send the required payment to the following wallet:\n"
        "<code>UQD_FO97Dxtxa7nqHIUamc5KWkcOtP0HPBr-uFQeBGbBR4a5</code>\n\n"
        "Once you've made the payment, use the /validate command followed by the transaction ID to confirm your subscription."
    )
    await message.answer(text, parse_mode="HTML")