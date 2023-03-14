import json

import requests


class GetIphone:

    def __init__(self, iphone=0):
        self.curl = f'https://doras.vcinema.cn:3100/verification_code/get_code?phone={iphone}'
        self.cheaders = {
            "Accept-Encoding": "gzip, deflate",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
            "Content-Length": "0",
            "Host": "doras.vcinema.cn:3100",
        }

    def get_code(self):
        rest = requests.get(url=self.curl, headers=self.cheaders)
        data_json = json.loads(rest.text)

        return data_json['content']

# print(GetIphone(14500000145).get_code())
