from pyrogram import Client, filters
from pyrogram.types import Message
from bot.keyboard.keyboard import KeyboardMainMenu, KeyboardNicheMenu


def keyboard_register_handlers(app: Client):
    """Регистрация всех обработчиков сообщений."""

    @app.on_message(filters.command("start"))
    async def keyboard_start_command(client: Client, message: Message):
        await message.reply(
            "👋 Привет! Я бот для парсинга и генерации ключевых слов.\n\nВыберите действие:",
            reply_markup=KeyboardMainMenu().build()
        )

    @app.on_message(filters.text & filters.regex("📂 Выбрать нишу"))
    async def keyboard_niche_menu(client: Client, message: Message):
        await message.reply("🔽 Выберите нишу:", reply_markup=KeyboardNicheMenu().build())

    @app.on_message(filters.text & filters.regex("↩️ Назад в главное меню"))
    async def keyboard_main_menu(client: Client, message: Message):
        await message.reply("🔙 Главное меню:", reply_markup=KeyboardMainMenu().build())
