from typing import Callable, Generator
import re

def generator_numbers(text: str) -> Generator[float, None, None]:
    """ Function for finding numbers in a string """
    pattern = r"(?<= )\d+(?:[.,]\d+)?(?= )"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable) -> float:
    """ Function for calculating the total income of an employee """
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
