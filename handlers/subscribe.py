import requests
from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.filters import Command

subscribe_router = Router()

@subscribe_router.message(Command(commands='subscribe'))
async def subscribe_handler(message: Message):
    acceptedCoins = [
        "TON",
        "TCAT",
        # "TCOMPASS",
        # "TSE",
        # "TONBEAM"
    ]

    text = "<b>Choose a Payment Method:</b>\n\n"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    # Create buttons for each coin type
    for coinType in acceptedCoins:
        button = InlineKeyboardButton(text=f"{coinType}", callback_data=f"subscribe_{coinType}")
        keyboard.inline_keyboard.append([button])

    await message.answer(text, parse_mode="HTML", reply_markup=keyboard)

@subscribe_router.callback_query(lambda callback: callback.data and callback.data.startswith("subscribe_"))
async def coin_chosen_handler(callback: CallbackQuery):
    coin_type = callback.data.split("_")[1]  # Extract the coin type from the callback data

    # Mapping the coin names to their CoinGecko IDs
    coin_prices = {
        "TON": "the-open-network",
        "TCAT": "ton-cat",
        # "TCOMPASS": "toncompass",
        # "TSE": "tonstarter",
        # "TONBEAM": "tonbeam"
    }

    coin_id = coin_prices.get(coin_type)

    if not coin_id:
        await callback.message.answer(f"Coin not supported: {coin_type}")
        return

    # Get the current price of the coin in USD
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd")
        response.raise_for_status()
        coin_price = response.json().get(coin_id, {}).get("usd")
        if not coin_price:
            raise ValueError("Price data missing")
    except Exception as e:
        await callback.message.answer("Failed to fetch the coin price. Please try again later.")
        return

    # Subscription plans in USD
    plans_usd = {
        1: 30,
        3: 90,
        6: 180,
        12: 360
    }

    text = f"<b>Choose a Plan for {coin_type}:</b>\n\n"
    keyboard = InlineKeyboardMarkup(inline_keyboard=[])

    # Create buttons for each plan with calculated price in the selected coin
    for plan, price_usd in plans_usd.items():
        price_in_coin = round(price_usd / coin_price, 2)  # Calculate and round the price
        button = InlineKeyboardButton(text=f"{plan} Months ({price_in_coin} {coin_type})", callback_data=f"plan_{coin_type}_{plan}")
        keyboard.inline_keyboard.append([button])

    await callback.message.edit_text(text, parse_mode="HTML", reply_markup=keyboard)
