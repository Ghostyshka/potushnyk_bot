from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import random
import requests

POSITIVE_RESPONSES = [
    "Ти сьогодні просто супер! 🌟",
    "Це неймовірно потужно! 💪",
    "Я радий, що ти так думаєш! 🤗"
]

NEGATIVE_RESPONSES = [
    "Не переживай, все буде добре! 😊",
    "Все налагодиться, не засмучуйся! 💪",
    "Тримайся, все мине! 🌈"
]

NEUTRAL_RESPONSES = [
    "Цікаво... 🤔",
    "Ммм, розумію... 😌",
    "Це цікава думка. 🔍"
]

POTUZHNO_VARIATIONS = [
    "потужно", "потужненько", "потужна", "потужний", 
    "потужність", "потужненький", "потужняк", "потуж"
]

TEXT_RESPONSES = [
    "Справді потужно! 💪",
    "Так, це потужно! 🔥",
    "Щось не дуже потужно...",
    "Вау! Це реально потужно! ⚡",
    "Хуюжно!",
    "У ВАШОМУ КОМЕНТАРІ ВИЯВЛЕНО ПОТУЖНІСТЬ. ПОТУЖНИЙ КОМЕНТАР ВІД ПОТУЖНОЇ ОСОБИСТОСТІ",
]

GIFS = [
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExamlmcXdkbDhtbDh1MzhjejNzcThvd2dvNm1ndnp4MjJubmd5cm1ybiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LodHgnktVlp7gMAo3L/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGFrY3Fnbm85aXo4ZjR6dzV3Z3R1ZzZ1YW1mbzhwY2o2b3pwemFmMCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BZJhRUb9r0pJTNxEII/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjRmZm94bnJuY2JpaG1mZHptOWN5NW42a3V1MDJsa3dhZDczamdjcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MNT1izQLGMprDFBRAx/giphy.gif",
    "https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjUzODg4dmk4bjVzNHdhbXI4ZzVhbmVyMGIyNGM0bTFudXkxM21rMiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/RYcVFsLzORPkl28hIj/giphy.gif",
    "",

]

def get_currency_rate():
    API_KEY = "key"
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD"
    
    response = requests.get(url)
    data = response.json()

    if data['result'] == 'success':
        rates = data['conversion_rates']
        usd_to_uah = rates['UAH']
        return f"1 USD = {usd_to_uah} UAH"
    else:
        return "Не вдалося отримати курс валют."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message and update.message.text:
        message_text = update.message.text.lower()

        if "потужник курс" in message_text or "потужник, курс" in message_text:
            currency_rate = get_currency_rate()
            await update.message.reply_text(currency_rate)

        elif any(variation in message_text for variation in POTUZHNO_VARIATIONS):
            response_type = random.choice(["text", "gif"])

            if response_type == "text":
                response_text = random.choice(TEXT_RESPONSES)
                await update.message.reply_text(response_text)
            elif response_type == "gif":
                gif_url = random.choice(GIFS)
                await update.message.reply_animation(animation=gif_url)

        else:
            pass

def main():
    BOT_TOKEN = "BOT_TOKEN"
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot has started!")
    app.run_polling()

if __name__ == "__main__":
    main()