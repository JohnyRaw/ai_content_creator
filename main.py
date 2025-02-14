from pyrogram import Client
# Вынесем обработчики в handlers.py
from bot.keyboard.handlers import keyboard_register_handlers
from config.config_loader import get_config

# Настройки бота
API_ID = get_config("bot", "api_id")
API_HASH = get_config("bot", "api_hash")
BOT_TOKEN = get_config("bot", "bot_token")

app = Client("keyword_bot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)

if __name__ == "__main__":
    print("Бот запущен...")
    keyboard_register_handlers(app)  # Регистрация обработчиков
    app.run()
