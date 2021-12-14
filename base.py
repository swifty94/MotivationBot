"""Application base module"""

import logging
import json
import logging.config
from os import path


_lconf = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(_lconf)

class BotException(Exception):
    """Base applicaton Exception"""
    def __init__(self, message="Error occured"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'-> {self.message}'

class ConfigurationError(BotException):
    """JSON configuration error"""
    def __init__(self, message="JSON configuration error"):
        super().__init__(message=message)

class RuntimeAbortionException(BotException):
    """RuntimeException"""
    def __init__(self, message="RuntimeException occured!"):
        super().__init__(message=message)
    
    def __str__(self):
        print(f'Critical -> {self.message}')
        exit(1)

#
# 
#   STATIC CONSTANTS
# 
#

GREET_MSG_RU = """
Добро пожаловать в NoLazy Bot. \n
Видимо, я тебе нужен, потому что ты - ленивая задница дорогуша и вместо того, чтобы делать то, что нужно - ты прокрастинируешь как профессионал.\n
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