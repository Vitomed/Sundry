def fib1(n: int) -> int:
    """
    >>> fib1(2)
    1
    >>> fib1(3)
    2
    >>> fib1(4)
    3
    >>> fib1(10)
    55
    """
    if n < 2:
        return n
    return fib1(n - 2) + fib1(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
