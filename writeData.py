import json


def writeJsonFile(CONFIG, data):
    with open(CONFIG["ResultFileName"], "w") as f:
        # ensure_ascii=False保证json转中文字符，而不是ascill码
        json.dump(data, f, ensure_ascii=False)
