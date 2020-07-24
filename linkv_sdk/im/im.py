from .config import config


class _IM:
    def __init__(self):
        self.cfg = config()


_im = None


def im():
    global _im
    if _im:
        return _im
    _im = _IM()
    return _im
