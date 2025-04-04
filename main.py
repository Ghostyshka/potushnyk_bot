import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, MessageHandler, filters

from bot.handlers import handle_message

def load_config():
    return {
        'BOT_TOKEN': os.getenv('BOT_TOKEN'),
        'EXCHANGE_RATE_API_KEY': os.getenv('EXCHANGE_RATE_API_KEY')
    }

def main():
    load_dotenv()
    config = load_config()
    
    if not config['BOT_TOKEN']:
        raise ValueError("BOT_TOKEN environment variable is not set")

    app = ApplicationBuilder().token(config['BOT_TOKEN']).build()
    app.bot_data['config'] = config

    app.add_handler(MessageHandler(filters.ALL, handle_message))

    print("Bot has started!")
    app.run_polling()

if __name__ == "__main__":
    main()