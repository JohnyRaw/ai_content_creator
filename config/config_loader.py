import configparser
import os

config = configparser.ConfigParser()


def get_config(section, key):
    config_path = os.path.join(os.path.dirname(__file__), "config.ini")
    if not config.read(config_path):
        raise Exception("Ошибка: файл config.ini не найден или пуст.")

    if section not in config or key not in config[section]:
        raise Exception(
            f"Ошибка: параметр [{section}] -> {key} не найден в config.ini")

    return config[section][key]
