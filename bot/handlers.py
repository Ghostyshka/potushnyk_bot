from telegram import Update
from telegram.ext import ContextTypes
import random
from typing import Optional

from .responses import (
    POTUZHNO_VARIATIONS,
    TEXT_RESPONSES,
    GIFS,
    ANTISEMITIC_GIFS
)
from .services import get_currency_rate

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return

    message_text = update.message.text.lower()
    config = context.bot_data.get('config', {})

    # Handle currency rate request
    if "потужник курс" in message_text or "потужник, курс" in message_text:
        if api_key := config.get('EXCHANGE_RATE_API_KEY'):
            currency_rate = get_currency_rate(api_key)
            if currency_rate:
                await update.message.reply_text(currency_rate)
            else:
                await update.message.reply_text("Не вдалося отримати курс валют.")
        else:
            await update.message.reply_text("Сервіс курсів валют недоступний. Check: EXCHANGE_RATE_API_KEY in config.")

    # Handle "потужно" variations
    elif any(variation in message_text for variation in POTUZHNO_VARIATIONS):
        response_type = random.choice(["text", "gif"])

        if response_type == "text":
            response_text = random.choice(TEXT_RESPONSES)
            await update.message.reply_text(response_text)
        elif response_type == "gif":
            gif_url = random.choice(GIFS)
            if gif_url:  # Skip empty URLs
                await update.message.reply_animation(animation=gif_url)
                
    # Handle antisemitic comments
    elif "жид" in message_text:
        gif_url = random.choice(ANTISEMITIC_GIFS)
        if gif_url:
            await update.message.reply_animation(animation=gif_url)