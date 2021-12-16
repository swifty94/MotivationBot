"""main module"""

if __name__ == "__main__":
    try:
        from base import logging, RuntimeAbortionException
        #from bot import BotContainer
        logging.getLogger(__name__)
        logging.info("Application start")
        #bot = BotContainer()
        #bot.run()
        from bot import Bot
        Bot.polling()
    except Exception as e:
        logging.error(RuntimeAbortionException(e))
    finally:
        logging.info("Application end")