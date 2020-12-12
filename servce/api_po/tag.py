# coding=utf-8
import datetime
import json

import requests

from servce.base_api import BaseApi


class Tag(BaseApi):
    def __init__(self):
        super().__init__()

    def add(self, group_name, tag, **kwargs):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag",
            "params": {"access_token": self.token},
            "json": {
                "group_name": group_name,
                "tag": tag,
                **kwargs}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
        #     params={"access_token": self.token},
        #     json={
        #         "group_name": group_name,
        #         "tag": tag,
        #         **kwargs}
        # )
        # print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list",
            "params": {"access_token": self.token},
            "json": {'tag_id': []}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        #     params={"access_token": self.token},
        #     json={'tag_id': []}
        # )
        # print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        data = {
            "method": "post",
            "url": "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag",
            "params": {"access_token": self.token},
            "json": {'id': id,
                     'name': tag_name}
        }
        r = self.send(data)
        # r = requests.post(
        #     'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        #     params={'access_token': self.token},
        #     json={'id': id,
        #           'name': tag_name}
        # )
        # print(json.dumps(r.json(), indent=2))
        return r

    def find_group_id_by_name(self, group_name):
        # 查询元素是否存在，如果不存在报错
        for group in self.list().json()["tag_group"]:
            if group_name in group["group_name"]:
                print("group_name in group")
                print(group["group_id"])
                return group["group_id"]
        print("group_name not in group")
        # raise ValueError("group_name not in group")
        return ""

    def group_id_exist(self, group_id):
        # 查询元素是否存在，如果不存在报错
        for group in self.list().json()["tag_group"]:
            if group_id in group["group_id"]:
                print("group_id in group")
                print(group["group_id"])
                return True
        return False

    def add_before_detect(self, group_name, tag, **kwargs):
        r = self.add(group_name, tag, **kwargs)
        print("添加标签")
        print(group_name)
        print(r.json()["errcode"])
        # 如果删除的元素存在
        if r.json()["errcode"] == 40071:
            print("元素存在")
            group_id = self.find_group_id_by_name(group_name)
            if not group_id:
                return ""
            self.delete_group(group_id)
            print("删除已有标签")
            self.add(group_name, tag, **kwargs)
            print("add success")
        result = self.find_group_id_by_name(group_name)
        if not result:
            print("add not success")
        return result

    def delete_group(self, group_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={"group_id": group_id}
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_tag(self, tag_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={"tag_id": tag_id}
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete_and_detect_group(self, group_ids):
        deleted_group_ids = []
        r = self.delete_group(group_ids)
        if r.json()["errcode"] == 40068:
            # 如果标签不存在，就添加一个标签，将group_id存储进来
            for group_id in group_ids:
                if not self.group_id_exist(group_id):
                    group_id = self.add_before_detect("TMP666", [{"name": "666"}])
                    deleted_group_ids.append(group_id)
                # 如果不存在，就将它存入标签组
                else:
                    deleted_group_ids.append(group_id)
            r = self.delete_group(deleted_group_ids)
        return r
