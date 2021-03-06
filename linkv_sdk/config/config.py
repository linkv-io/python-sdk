# -*- coding: UTF-8 -*-

from linkv_sdk.im.config import dict_config as dict_im_config
from linkv_sdk.rtc.config import dict_config as dict_rtc_config
from linkv_sdk.live.config import dict_config as dict_live_config
from linkv_sdk.http.http import http
from linkv_sdk import __version__
from .bindings.binding import download_library, binding
from json import loads


def init(app_id: str, app_secret: str, pool_size: int = 10, version: str = __version__) -> bool:
    http(version=version, pool_size=pool_size)
    if not download_library():
        return False
    json_data = binding().decrypt(app_id, app_secret)
    d = loads(json_data)
    dict_im_config(d['im'] if 'im' in d.keys() else {})
    dict_rtc_config(d['rtc'] if 'rtc' in d.keys() else {})
    dict_live_config(d['sensor'] if 'sensor' in d.keys() else {})
    return True
