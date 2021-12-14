from base import *
from threading import Thread
import random


def background(f):
    '''
    a threading decorator
    use @background above the function you want to run in the background
    '''
    def backgrnd_func(*a, **kw):
        Thread(target=f, args=a, kwargs=kw).start()
    return backgrnd_func

class Help:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__class__.__name__)
    
    def get_message_meta_struct(self, message):
        """
        Getting only necessary struct of message metadata for logging
        """
        try:
            meta_struct = {
                "id" : message.from_user.id,
                "user": message.from_user.username,
                "msg": message.text,
            }
            return meta_struct
        except Exception as e:
            self.logger.error(BotException(e))
            raise BotException(e)

    def get_motivation(self, message) -> str:
        """
        What is the actual argument to "motivaton" command
        """
        try:
            fullcommand = str(message.text).split()            
            fullcommand.remove("/motivation")
            motivation_part = str(fullcommand).replace("[",'').replace("]",'').replace(",","").replace("\'","")            
            return motivation_part
        except Exception as e:
            self.logger.error(BotException(e))
            raise BotException(e)

    def get_random_line(self, choiseList):
        """
        Get random beginning for "motivaton" command to send
        """
        try:
            random_line = random.choice(choiseList)
            return random_line
        except Exception as e:
            self.logger.error(BotException(e))
            raise BotException(e)

    def compile_line(self, message):
        try:
            what_to_do = self.get_motivation(message)
            begin = self.get_random_line(MOTIVATION_START_RU)
            return f"{begin} {what_to_do}"
        except Exception as e:
            self.logger.error(BotException(e))
            raise BotException(e)

class Conf(object):
    """
    JSON configuration object with single Conf._get() method\n
    Details are in method annotation
    """
          
    def _get(key) -> str:
        """
        Get JSON value by key
        :param - key:str
        :param - return:str
        """
        logger = logging.getLogger(__class__.__name__)
        _confFile = "conf.json"
        _c = __class__.__name__
        try:
            with open(_confFile) as f:
                data = json.load(f)
            val = data[key]            
            return val
        except FileNotFoundError as noF:
            _l = f"CriticalException {noF} -> AppExit!"
            logger.error(_l)
            raise ConfigurationError(_l)
        except Exception as e:
            logger.error(f"Exception {e}")
            raise ConfigurationError(e)