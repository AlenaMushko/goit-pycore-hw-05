from typing import Callable, Dict


def caching_fibonacci() -> Callable[[int], int]:
    """ Returns a function that calculates the n-th Fibonacci number. """
    cache: Dict[int, int]  = {}

    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n not in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))  # 55
print(fib(15))
