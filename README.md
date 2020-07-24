[![API Reference](https://img.shields.io/badge/api-reference-blue.svg)]()
[![Build Status](https://img.shields.io/static/v1?label=build&message=passing&color=32CD32)]()
[![Apache V2 License](https://img.shields.io/badge/license-Apache%20V2-blue.svg)](https://github.com/linkv-io/python-sdk/blob/master/LICENSE)

# python-sdk

LINKV SDK for the Python programming language.

## Download
```sh
git clone https://github.com/linkv-io/python-sdk
```

## Install
```sh
cd python-sdk
python setup.py build
python setup.py install --record log
```

## Uninstall
```sh
cat log |sudo xargs rm -rf
rm -rf build dist linkv_sdk.egg-info log
```

## Usage

```python
from json import dumps

from linkv_sdk import linkv_sdk


def main():
    app_id = 'qOPBZYGqnqgCSJCobhLFRtvvJzeLLzDR'
    app_secret = '1EE940FB2E0AB99368DDEF4A7446A17E3418CE9B1721464624A504BBD977A4FC1477F6A1A02B22AF64070A49C32E05B1AC23E47D86BF6C490D637A42735E6DF7589D5644B3DF1BCD489186940ADE4C3D61C6028FCAF90D57FDCA7BA1888DD4B060B2996BCF41087A8CDEE52D775548166FC92B83D88125434597B9394AC3F7C81C9B8A41C0191B0A09AD59F20881A087574C51B0288A1867D8B7EE9CABC97C322F6469E4E19261C7A26527CD65299A564B319F42DB70E016537A5AFAAE896BEE'

    if not linkv_sdk.init(app_id, app_secret):
        return

    print(dumps(obj=linkv_sdk.im().cfg.__dict__, ensure_ascii=False))
    print(dumps(obj=linkv_sdk.rtc().cfg.__dict__, ensure_ascii=False))


if __name__ == "__main__":
    main()
```

## License

This SDK is distributed under the
[Apache License, Version 2.0](http://www.apache.org/licenses/LICENSE-2.0),
see LICENSE.txt and NOTICE.txt for more information.