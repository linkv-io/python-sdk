# -*- coding: UTF-8 -*-
from linkv_sdk import linkv_sdk


def main():
    app_id = ''
    app_secret = ''
    pool_size = 10
    if not linkv_sdk.init(app_id, app_secret, pool_size=pool_size):
        return

    im = linkv_sdk.LvIM()

    third_uid = 'python3'
    # r = im.getTokenByThirdUID(third_uid)
    # if not r['status']:
    #     print('im.getTokenByThirdUID(%s)' % r['error'])
    #     return
    #
    # third_token = r['token']
    to_uid = '123456'
    object_name = 'RC:textMsg'
    content = 'I\'m python3'
    r1 = im.pushConverseData(third_uid, to_uid, object_name, content)
    if not r1['status']:
        print('im.pushConverseData(%s)' % r1['error'])
        return

    if r1['ok']:
        print('success')
    else:
        print('fail')


if __name__ == "__main__":
    main()
