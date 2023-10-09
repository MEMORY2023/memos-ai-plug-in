## json 数据的处理

学习地址：https://zhuanlan.zhihu.com/p/524972433

### 反序列化

将 json 字符串转换成 dic 对象

```
person_str = '{"name": "blueberry", "age": 4, "hobbies": ["eat", "sleep"]}'
person_dict = json.loads(person_str)
pprint.pprint(person_dict)
pprint.pprint(type(person_dict))
```

### 序列化

将 dic 对象转换成 json 字符串

```
blueberry_dict = {
    "name": "blueberry",
    "age":4,
    "hobbies": ["eat","sleep"]
}
blueberry_json_str = json.dumps(blueberry_dict)
pprint.pprint(blueberry_json_str)
pprint.pprint(type(blueberry_json_str))
```

## 文件结构

### config.json 文件

存放项目的配置参数

### gpt.py 文件

处理与 gpt 的交互

### loadData.py 文件

处理获取 memos 数据源
加载 config.json 配置文件的配置参数

### getKeyWords.py 文件

对记录内容进行分词，提取关键词。最后在所有内容中提取出 top5 频次的关键词

### getKeyWordsByRow.py 文件

对记录内容进行分词，提取关键词。在每一行内容中提取出 top5 频次的关键词

### result.json 文件

运行结果保存在 result.json 文件中，自动生成
