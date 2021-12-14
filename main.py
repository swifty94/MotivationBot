"""main module"""

if __name__ == "__main__":
    try:
        from base import logging, RuntimeAbortionException
        logging.getLogger(__name__)
        logging.info("Application start")
        from bot import Bot
        Bot.polling()
    except Exception as e:
        logging.error(RuntimeAbortionException(e))
