# -*- coding: UTF-8 -*-

import random
import hashlib
import time
from datetime import datetime


def genUniqueIDString(app_key: str) -> str:
    return '{}-{}'.format(
        app_key[2:],
        ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 9)),
    )


def genRandomString() -> str:
    return '{}{}{}'.format(
        ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8)),
        str(int(time.mktime(datetime.now().timetuple()))),
        ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 8)))


def genSign(params: dict, md5_secret: str) -> str:
    data = __encode(params) + "&key=" + md5_secret
    obj = hashlib.new('md5')
    obj.update(bytes(data, encoding='utf8'))
    return obj.hexdigest().lower()


def __encode(params: dict) -> str:
    keys = sorted(params.keys())
    container = ''
    for k in keys:
        if len(container) > 0:
            container += '&'
        container += '%s=%s' % (k, params[k])
    return container
