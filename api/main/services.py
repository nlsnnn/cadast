import time
from random import randint


def server():
    time.sleep(randint(5, 30))
    return True if randint(0, 1) else False