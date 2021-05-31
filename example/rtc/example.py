# -*- coding: UTF-8 -*-

from linkv_sdk import linkv_sdk


def main():
    app_id = ''
    app_secret = ''
    pool_size = 10
    if not linkv_sdk.init(app_id, app_secret, pool_size=pool_size):
        return

    rtc = linkv_sdk.LvRTC()

    print(rtc.genAuth())


if __name__ == "__main__":
    main()
