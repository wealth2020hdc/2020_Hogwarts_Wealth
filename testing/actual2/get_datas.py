# --*-HogWarts-HDC-*--
# --*-UTF-8-*--
import yaml


def get_datas():
    with open("./datas/calculator.yml") as f:
        datas = yaml.safe_load(f)
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    sub_datas = datas['sub']['datas']
    sub_ids = datas['sub']['ids']
    mul_datas = datas['mul']['datas']
    mul_ids = datas['mul']['ids']
    div_datas = datas['div']['datas']
    div_ids = datas['div']['ids']
    return [add_datas, add_ids, sub_datas, sub_ids, mul_datas, mul_ids, div_datas, div_ids]
