from pyrogram.types import ReplyKeyboardMarkup


class KeyboardBaseClass:
    """Базовый класс для клавиатурных меню."""

    def __init__(self):
        self.keyboard = []

    def build(self):
        """Создаёт клавиатуру на основе self.keyboard."""
        return ReplyKeyboardMarkup(self.keyboard, resize_keyboard=True, one_time_keyboard=False)


class KeyboardMainMenu(KeyboardBaseClass):
    """Главное меню с основными кнопками."""

    def __init__(self):
        super().__init__()
        self.keyboard = [
            # TODO Экспорт в GSheets внутри сбора ключевых слов
            ["📂 Выбрать нишу", "🔍 Auto Keyword Collector"],
            ["🔄 AI Trends Analyzer", "AI Content Planner"],
        ]


class KeyboardNicheMenu(KeyboardBaseClass):
    """Меню выбора ниши."""
    # TODO Продумать логику добавления ниш в это меню

    def __init__(self):
        super().__init__()
        self.keyboard = [
            ["💼 Бизнес", "🏋️ Фитнес"],
            ["📚 Обучение", "↩️ Назад в главное меню"]
        ]
