from typing import Generator


def fibonacci(item: int) -> Generator[int]:
    a, b = 0, 1
    count = 0
    while count < item:
        if a % 2 == 0:
            yield a
            count += 1
        a, b = b, a + b
