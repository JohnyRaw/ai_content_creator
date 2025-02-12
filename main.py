from pyrogram import Client, filters
from pyrogram.types import Message
from bot.keyboard.keyboard import KeyboardMainMenu, KeyboardNicheMenu
from config.config_loader import get_config

# Настройки бота
API_ID = get_config("bot", "api_id")
API_HASH = get_config("bot", "api_hash")
BOT_TOKEN = get_config("bot", "bot_token")

app = Client("keyword_bot", api_id=API_ID,
             api_hash=API_HASH, bot_token=BOT_TOKEN)

# Команда /start


# Главное меню


def keyboard_register_handlers(app: Client):
    @app.on_message(filters.command("start"))
    async def keyboard_start_command(client: Client, message: Message):
        await message.reply(
            "👋 Привет! Я бот для парсинга и генерации ключевых слов.\n\nВыберите действие:",
            reply_markup=KeyboardNicheMenu().build())

    @app.on_message(filters.text & filters.regex("📂 Выбрать нишу"))
    async def keyboard_niche_menu(client: Client, message: Message):
        """Показывает подменю для выбора ниши."""
        await message.reply("🔽 Выберите нишу:", reply_markup=KeyboardNicheMenu().build())

    @app.on_message(filters.text & filters.regex("↩️ В главное меню"))
    async def keyboard_main_menu(client: Client, message: Message):
        """Возвращает пользователя в главное меню."""
        await message.reply("🔙 Главное меню:", reply_markup=KeyboardMainMenu().build())


# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    app.run()
