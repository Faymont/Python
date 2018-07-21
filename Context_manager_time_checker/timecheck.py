from time import time


class TimeCheck(object):
    """
    A class for the context manager to measure the code execution time
    """
    def __init__(self):
        self.start = 0

    def __enter__(self):
        self.start = time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(time() - self.start, "seconds")


def test():
    x = range(10 ** 10000000)


with TimeCheck():
    test()

"""
7.538440465927124 seconds
"""