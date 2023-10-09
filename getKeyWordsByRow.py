'''
    每条记录分别提取K个关键词
'''
import jieba
from collections import Counter
import re

# 获取一条记录的K个关键词
def getKeywords(record,K):
    # 获取笔记id及内容
    id = record["id"]
    content = record["content"]
    print("--Original Text:",content)

    # 提炼关键词
    ## 去除#后面的文字标签
    content = re.sub("#.* ", "", content)
    print("--Remove label Text:", content)

    ## 分词
    cutContent = jieba.lcut(str(content))
    # print("--Cut Text:",cutContent)

    ## 去除停用词
    with open('./utils/stoplist.txt', 'r', encoding='utf-8') as f:
        stops = f.read()
    stops = stops.split()
    cutContent = [word for word in cutContent if word not in stops]
    # print("--Remove Stop Text:", cutContent)

    ## 去除否定词
    with open('./utils/chinese_dictionary-master/chinese_dictionary-master/dict_negative.txt', 'r', encoding='utf-8') as f:
        notWords = f.read()
    notWords = notWords.split()
    cutContent = [word for word in cutContent if word not in notWords]
    # print("--Remove Not Text:", cutContent)

    ## 去除程度词
    with open('./utils/degree.csv', 'r', encoding='gbk') as f:
        degrees = f.readlines()
    degrees = [dl.split(',')[0] for dl in degrees]
    cutContent = [word for word in cutContent if word not in degrees]
    # print("--Remove Degree Text:", cutContent)

    ## 去除空格、\n等字符
    otherWords = [' ','','\n','\r\n','\r']
    cutContent = [word for word in cutContent if word not in otherWords]
    # print("--Remove Others Text:", cutContent)

    ## 统计词语次数从而获取关键词（前k个为关键词）
    k = K # 设置保留几个关键词
    wordsCount = Counter(cutContent)
    # print("--Count Words:", wordsCount)
    k = k if len(wordsCount)>=k else len(wordsCount)
    keywords = sorted(wordsCount.items(), key=lambda x: x[1], reverse=True)[:k]
    keywords = [kw[0] for kw in keywords]

    # 返回结果
    res = {
        "id":id,
        "keywords":keywords
    }
    print("--Result:",res,end="\n\n")
    return res

# 获取所有记录的K个关键词
def getAllKeywords(records,K):
    resultList = []
    for record in records:
        resultList.append(getKeywords(record,K))
    return resultList

