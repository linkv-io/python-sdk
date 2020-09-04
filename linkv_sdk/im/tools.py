# -*- coding: UTF-8 -*-

import random
import string
import time


def genGUID() -> str:
    return '{}-{}-{}-{}'.format(
        ''.join(random.sample(string.ascii_letters + string.digits, 9)),
        ''.join(random.sample(string.ascii_letters + string.digits, 4)),
        ''.join(random.sample(string.ascii_letters + string.digits, 4)),
        ''.join(random.sample(string.ascii_letters + string.digits, 12)))


def getTimestampS() -> str:
    t = time.time()
    return str(int(t))


def getTimestampMS() -> str:
    t = time.time()
    return str(int(t * 1000))
