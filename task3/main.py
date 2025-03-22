from pathlib import Path
import re
from functools import wraps, reduce

from colorama import Fore, init
init(autoreset=True)

def logs_error(func):
    """ Handle errors in function """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            print(f'{Fore.RED}File not found.')
        except PermissionError:
            print(f'{Fore.RED}Permission denied.')
        except Exception as e:
            print(f'{Fore.RED}Error: {e}')
    return wrapper

@logs_error
def load_logs(file_path: str) -> list:
    path = Path(file_path)
    log_list = []

    if not path.exists():
        return []
    with open(file_path) as file:
        logs = file.readlines()
        for log in logs:
            result = parse_log_line(log)
            log_list.append(result)
    return log_list

def parse_log_line(line: str) -> dict:
    """ Parse log line and return dict with log parts """
    try:
        pattern = re.compile(
            r"^(?P<date>\d{4}-\d{2}-\d{2})\s"
            r"(?P<time>\d{2}:\d{2}:\d{2})\s"
            r"(?P<level>INFO|DEBUG|ERROR|WARNING)\s"
            r"(?P<message>.+)$"
        )
        match = pattern.match(line.strip())
        return match.groupdict()
    except Exception as e:
        print(f'{Fore.RED}Parse error: {e}')
        return {}

@logs_error
def filter_logs_by_level(logs: list, level: str) -> list:
    """ Filter logs by level """
    return list(filter(lambda x: x['level'] == level, logs))

@logs_error
def count_logs_by_level(logs: list) -> dict:
    """ Count logs by level """
    counts = {}
    for log in logs:
        level = log['level']
        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1
    return counts

@logs_error
def display_log_counts(counts: dict) -> None:
    """ Display table log counts """
    level_colors = {
        'INFO': Fore.YELLOW,
        'DEBUG': Fore.BLUE,
        'ERROR': Fore.RED,
        'WARNING': Fore.MAGENTA
    }

    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in ['INFO', 'DEBUG', 'ERROR', 'WARNING']:
        color = level_colors.get(level, Fore.WHITE)
        print(f"{color}{level:<17}| {counts.get(level, 0)}")
    print()


if __name__ == '__main__':
    load_log_list = load_logs("logs.txt")
    # filtered_logs_by_level = filter_logs_by_level(load_log_list, "INFO")
    # print(f'{Fore.LIGHTBLUE_EX}Filtered by level:{Fore.RESET} {filtered_logs_by_level}')
    counted_logs_by_level = count_logs_by_level(load_log_list)
    display_log_counts(counted_logs_by_level)
