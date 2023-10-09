<p align="center"><a href="https://usememos.com"><img height="64px" src="https://raw.githubusercontent.com/BarryYangi/MemosGallery/master/public/logo-full.webp" alt="✍️ memos" /></a></p>

<p align="center">memos-ai-plug-in，通过Memos API提取内容关键词，AI生成分析报告</p>
<p align="center">AI文本能力</p>

### 🔧工具包

- jieba
- openai
- requests

### 📃文件结构

- config.json，存放项目的配置参数

- gpt.py，处理与 gpt 的交互

- loadData.py，处理获取 memos 数据源，加载 config.json 配置文件的配置参数

- getKeyWords.py，对记录内容进行分词，提取关键词。最后在所有内容中提取出 top5 频次的关键词

- getKeyWordsByRow.py，对记录内容进行分词，提取关键词。在每一行内容中提取出 top5 频次的关键词

- result.json，运行结果保存在 result.json 文件中，自动生成

### :rocket: 使用方法

1. 修改config.json文件，将OpenApi、ApiKey、AiProxy替换成自己的参数

   <img src="/Users/liangyuliang/Library/Application Support/typora-user-images/image-20231009213119322.png" alt="image-20231009213119322" style="zoom:50%;" />

2. 在main.go文件中启动python

3. result.json中查看分析结果

