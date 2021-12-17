"""Bot module"""
from time import sleep, time
from base import BotException, GREET_MSG_RU, FAREWELL_MSG_RU
from help import Conf, Help, logging, backgroundThread
import telebot

conf = Conf()
Bot = telebot.TeleBot(conf.API_KEY)
logger = logging.getLogger("Bot")
helper = Help()

@backgroundThread
def constant_update(message):
    try:
        for i in range(conf.DAYS_SECONDS):
            line = helper.compile_line(message)
            message_meta = helper.get_message_meta_struct(message)
            logger.info(f"Iteration: {i} SendPeriodicUpdateToUserId={message_meta['id']}")
            Bot.reply_to(message, line)
            sleep(conf.TIMEOUT)
    except Exception as e:
        logger.error(BotException(e))
        raise BotException(e)

@Bot.message_handler(regexp="^(?!.*(start|stop|motivation))")
def unknown_command(message):
    try:
        Bot.reply_to(message, "Неправильная комманда.\nВозможные варианты: /start, /stop, /motivation $ВашаЦель")
    except Exception as e:
        logger.error(BotException(e))
        raise BotException(e)

@Bot.message_handler(commands=["start", "motivation", "stop"])
def bot_logic(message):
    try:
        message_meta = helper.get_message_meta_struct(message)
        msg = message_meta['msg']
        if "start" in msg:
            __log = f"HadlingWelcomeRequest: UserId={message_meta['id']}, UserName={message_meta['user']}"
            logger.info(__log)
            Bot.reply_to(message, GREET_MSG_RU)
        elif "motivation" in msg:
            if len(msg) == len("/motivation"):
                __log = f"EmptyMotivationRequest: UserId={message_meta['id']}, UserName={message_meta['user']}"
                logger.info(__log)
                Bot.reply_to(message, "Цель мотивации не задана!\nПример команды: /motivation $ВашаЦель")
            else:
                constant_update(message)
        elif "stop" in msg:
            Bot.reply_to(message, FAREWELL_MSG_RU)
        else:
            unknown_command()
    except Exception as e:
        logger.error(BotException(e))
        raise BotException(e)