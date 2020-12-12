# coding=utf-8
import json

import requests


class BaseApi:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww473b5f4aeb630dd7'
        corpsecret = 'r63WETXfL632oIH3Dn1D5WxXeHjuh3VOQNjBNq9Wpp8'
        data = {
            "method": "get",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {'corpid': corpid, 'corpsecret': corpsecret}
        }
        r = self.send(data)
        # r = requests.get(
        #     "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
        #     params={'corpid': corpid, 'corpsecret': corpsecret}
        # )
        # print(json.dumps(r.json(), indent=2))
        # assert r.status_code == 200
        # assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token

    def send(self, kwargs):
        r = requests.request(**kwargs)
        print(json.dumps(r.json(), indent=2))
        return r
