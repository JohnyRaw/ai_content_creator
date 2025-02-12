import configparser

# Создаём объект для чтения config.ini
config = configparser.ConfigParser()
config.read("config.ini")


def get_config(section, key):
    """Возвращает значение параметра из config.ini.

    Args:
        section (str): Секция в config.ini (например, "bot").
        key (str): Ключ в этой секции (например, "bot_token").

    Returns:
        str: Значение параметра.

    Raises:
        KeyError: Если ключ или секция отсутствует.
    """
    try:
        return config[section][key]
    except KeyError:
        raise Exception(
            f"Ошибка: параметр [{section}] -> {key} не найден в config.ini")
