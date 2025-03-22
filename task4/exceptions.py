from functools import wraps

from colorama import Fore, init
init(autoreset=True)

class InvalidCommand(Exception):
    pass


class NoFoundContact(Exception):
    pass


class ContactAlreadyExists(Exception):
    pass


def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return f'{Fore.RED}Error in {func.__name__}: {Fore.LIGHTRED_EX}Invalid key'
        except ValueError:
            return f'{Fore.RED}Error in {func.__name__}: {Fore.LIGHTRED_EX}Invalid value'
        except IndexError:
            return f'{Fore.RED}Error in {func.__name__}: {Fore.LIGHTRED_EX}Invalid index'
        except Exception as e:
            return f'{Fore.RED}Error in {func.__name__}: {Fore.LIGHTRED_EX}{e}'
    return wrapper
