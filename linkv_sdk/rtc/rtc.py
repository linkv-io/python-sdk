# -*- coding: UTF-8 -*-

from .config import config
import time
import hmac
from datetime import datetime


class RTC(object):
    def __init__(self):
        pass

    @staticmethod
    def GenAuth() -> dict:
        now = str(int(time.mktime(datetime.now().timetuple())))
        data = '{}{}'.format(config().app_id, now)
        auth_mac = hmac.new(config().app_key.encode('utf-8'), data.encode('utf-8'), digestmod='SHA1')
        return {
            'status': True,
            'app_id': config().app_id,
            'auth': auth_mac.hexdigest(),
            'expire_ts': now,
        }


class LvRTC(RTC):
    def __init__(self):
        RTC.__init__(self)

    def GenAuth(self) -> dict:
        return super(LvRTC, self).GenAuth()
