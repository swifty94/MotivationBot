"""Bot module"""
from time import sleep, time
from base import *
from help import *
import telebot

Bot = telebot.TeleBot(Conf._get("API_KEY"))
logger = logging.getLogger("Bot")
helper = Help()

@Bot.message_handler(commands=["start"])
def bot_start(message):
    try:
        message_meta = helper.get_message_meta_struct(message)
        __log = f"HadlingRequest: id={message_meta['id']}, user={message_meta['user']}"
        logger.info(__log)
        Bot.reply_to(message, GREET_MSG_RU)
    except Exception as e:
        logger.error(BotException(e))
        raise BotException(e)


@Bot.message_handler(commands=["motivation", "stop"])
def motivate_or_stop(message):
    try:
        message_meta = helper.get_message_meta_struct(message)
        msg = message_meta['msg']
        __log = f"HadlingRequest: id={message_meta['id']}, user={message_meta['user']}"
        logger.info(__log)
        if "motivation" in msg and len(msg) != len("/motivation"):
            constant_update(message)
        elif "stop" in msg:
            Bot.reply_to(message, FAREWELL_MSG_RU)
        else:
            Bot.reply_to(message, "Неправильная комманда")
    except Exception as e:
        logger.error(BotException(e))
        raise BotException(e)

@background
def constant_update(message):
    try:
        days = Conf._get("DAYS_SECONDS")
        timeout = Conf._get("TIMEOUT")
        for i in range(days):
            line = helper.compile_line(message)
            Bot.reply_to(message, line)
            sleep(timeout)
    except Exception as e:
        logger.error(BotException(e))
        raise BotException(e)