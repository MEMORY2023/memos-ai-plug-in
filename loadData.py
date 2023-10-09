# -*- coding: UTF-8 -*-
import json
import requests


def loadConfig():
    # 通过config.json获取项目配置信息
    path = "config.json"
    with open(path, "r", encoding="utf-8") as f:
        global CONFIG
        CONFIG = json.load(f)
    return CONFIG


def loadMemoData():
    url = CONFIG["OpenApi"]
    r = requests.get(url)
    result = r.json()["data"]
    return json.dumps(result)
