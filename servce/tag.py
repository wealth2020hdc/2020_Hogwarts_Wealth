# coding=utf-8
import datetime
import json

import requests


class Tag:
    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'ww473b5f4aeb630dd7'
        corpsecret = 'r63WETXfL632oIH3Dn1D5WxXeHjuh3VOQNjBNq9Wpp8'
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={'corpid': corpid, 'corpsecret': corpsecret}
        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0
        token = r.json()['access_token']
        return token

    def add(self, group_id, group_name, tag):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={"access_token": self.token},
            json={"group_id": group_id,
                  "group_name": group_name,
                  "tag": tag}
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={'tag_id': []}
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={'access_token': self.token},
            json={'id': id,
                  'name': tag_name}
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, tag_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={"tag_id": tag_id}
        )
        print(json.dumps(r.json(), indent=2))
        return r
