# -*- coding: UTF-8 -*-
import loadData
import gpt
import json
import getKeyWords
import writeData

if __name__ == "__main__":
    # 加载配置文件config.json
    CONFIG = loadData.loadConfig()

    # 获取memo数据
    data_json = loadData.loadMemoData()
    # 将json反序列化为dic对象，便于后续操作
    data_dic = json.loads(data_json)

    # 获取全部数据的K个关键词
    K = 20
    keywords = getKeyWords.getAllKeywords(data_dic, K)
    # 选取最高频的5个关键词进行头脑风暴
    result = {}
    result["keywords"] = keywords
    result["brain storms"] = []
    for i in range(5):
        keyword = keywords[i]["keyword"]
        context = "头脑风暴关于" + keyword
        res_json = gpt.sendGPT(CONFIG, context)
        # 将json字符串反序列化为dict对象，便于后续操作
        res_dic = json.loads(res_json)
        res_dic["keyword"] = keyword
        result["brain storms"].append(res_dic)
    writeData.writeJsonFile(CONFIG, result)
