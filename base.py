"""Application base module"""

import logging
import json
import logging.config
from os import path

logging.config.fileConfig(path.join(path.dirname(path.abspath(__file__)), 'logging.ini'))

class BotException(Exception):
    """Base applicaton Exception"""
    def __init__(self, message="Error occured"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        logging.error(f"{self.message}", exc_info=1)
        return f'-> {self.message}'

class ConfigurationError(BotException):
    """JSON configuration error"""
    def __init__(self, message="JSON configuration error"):
        super().__init__(message=message)
        super().__str__()

class RuntimeAbortionException(BotException):
    """RuntimeException"""
    def __init__(self, message="RuntimeException occured!"):
        super().__init__(message=message)
        super().__str__()


# 
#   STATIC CONSTANTS
# 

GREET_MSG_RU = """
Добро пожаловать в NoLazy Bot. \n
Видимо, я тебе нужен, потому, что ты - ленивая задница, дорогуша, и вместо того, чтобы делать то, что нужно - ты профессионально прокрастинируешь \n
Для того что бы получать мотивацию каждые 15 минут в течении следующих 30 дней - просто выполни команду:\n
/motivation "Дальше пишешь то, на что, у тебя не хватает мотивации". \n
Пример:\n

/motivation заниматься спортом\n
P.S No emodji in messages supported yet.  
"""

MOTIVATION_START_RU = ["Бездельничаем? А кто хотел", "Привет, ленивая задница. Может тебе уже пора", "Эй ты! Ты должен", "Опять нифига не делаешь? Тебе ведь нужно", "Чего сидишь!? Тебу же нужно", "Как насчёт наконец-то уже"]

FAREWELL_MSG_RU = """
До новых встреч, мой ленивый друг :)
"""