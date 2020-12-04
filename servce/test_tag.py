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

    @pytest.mark.parametrize("tag_id, tag_name",
                             [['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1_new_'],
                              ['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1-中文字符'],
                              ['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1[中文字符]'],
                              ['etL56nEQAAMOpKEfqVi6xZHpUE6AddRw', 'tag1@$#t特殊字符']])
    def test_tag_list(self, tag_id, tag_name):
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

    def test_tag_list_fail(self):
        pass

    def test_tag_add(self):
        group_id = "etL56nEQAAEkZ5vJQZgXrCpYlQaJZ-rA"
        group_name = "python15"
        tag_name = "tag_name_add" + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.add(group_id=group_id,
                         group_name=group_name,
                         tag=[{"name": tag_name}])
        r = self.tag.list()
        tags = [tag
                for group in r.json()['tag_group'] if group['group_name'] == group_name
                for tag in group['tag']
                if tag['name'] == tag_name]
        assert tags != []

    def test_tag_del(self):
        tag_id = "etL56nEQAAk3FtL63_rLhey1pG2lEEMg"
        r = self.tag.list()
        r = self.tag.delete(tag_id=tag_id)
        r = self.tag.list()
        tags = [tag
                for group in r.json()['tag_group']
                for tag in group['tag']
                if tag['id'] == tag_id]
        assert tags == []
