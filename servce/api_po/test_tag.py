# coding=utf-8
import datetime
import json

import pytest
import requests
from jsonpath import jsonpath

from servce.api_po.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    def test_tag_list(self):
        self.tag.list()

    @pytest.mark.parametrize("tag_id, tag_name",
                             [['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1_new_'],
                              ['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1-中文字符'],
                              ['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1[中文字符]'],
                              ['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1@$#t特殊字符']])
    def test_tag_updat(self, tag_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        group_name = 'python15'
        r = self.tag.list()
        r = self.tag.update(id=tag_id, tag_name=tag_name)
        r = self.tag.list()
        tags = [tag
                for group in r.json()['tag_group'] if group['group_name'] == group_name
                for tag in group['tag']
                if tag['name'] == tag_name]
        assert tags != []
        print(jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]"))
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    def test_tag_add(self):
        group_name = "TMP888"
        tag_name = [
            {"name": "first1"},
            {"name": "second1"},
            {"name": "third1"},
        ]
        r = self.tag.add_before_detect(group_name, tag_name)
        assert r
        # assert r.status_code == 200
        # assert r.json()["errcode"] == 0
        # r = self.tag.list()
        # tags = [tag
        #         for group in r.json()['tag_group'] if group['group_name'] == group_name
        #         for tag in group['tag']
        #         if tag['name'] == tag_name]
        # assert tags != []

    def test_del_group(self):
        group_id = ["etL56nEQAA-v0kRIXRDtiiRjh9DeTmkg"]
        r = self.tag.list()
        r = self.tag.delete_group(group_id)
        # r = self.tag.list()
        # tags = [tag
        #         for group in r.json()['tag_group']
        #         for tag in group['tag']
        #         if tag['id'] == tag_id]
        # assert tags == []

    def test_del_tag(self):
        tag_id = ["etL56nEQAA5oaWxw-TeAOCMAsBvvzS_g"]
        r = self.tag.delete_tag(tag_id)
        # r = self.tag.list()
        # tags = [tag
        #         for group in r.json()['tag_group']
        #         for tag in group['tag']
        #         if tag['id'] == tag_id]
        # assert tags == []

    def test_delete_and_detect_group(self):
        r = self.tag.delete_and_detect_group(["etL56nEQAAbtIJdJdgDA0Pj0crk8LvtQ"])
        assert r.json()["errcode"] == 0
