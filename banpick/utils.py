from random import choice
import json
import string

def get_server_info_value(key: str):

    with open('server_info.json', mode='rt', encoding='utf-8') as file:
        data = json.load(file)
        for k, v in data.items():
            if k == key:
                return v
            raise ValueError('找不到服务器信息.')
