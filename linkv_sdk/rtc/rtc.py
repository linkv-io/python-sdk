from .config import config


class _RTC:
    def __init__(self):
        self.cfg = config()


_rtc = None


def rtc():
    global _rtc
    if _rtc:
        return _rtc
    _rtc = _RTC()
    return _rtc
