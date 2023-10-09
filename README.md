<p align="center"><a href="https://usememos.com"><img height="64px" src="https://raw.githubusercontent.com/BarryYangi/MemosGallery/master/public/logo-full.webp" alt="✍️ memos" /></a></p>

<p align="center">memos-ai-plug-in，通过Memos API提取内容关键词，AI生成分析报告</p>
<p align="center">AI文本能力</p>

### 🔧 工具包

- jieba
- openai
- requests

### 📃 文件结构

- config.json，存放项目的配置参数

- gpt.py，处理与 gpt 的交互

- loadData.py，处理获取 memos 数据源，加载 config.json 配置文件的配置参数

- getKeyWords.py，对记录内容进行分词，提取关键词。最后在所有内容中提取出 top5 频次的关键词

- getKeyWordsByRow.py，对记录内容进行分词，提取关键词。在每一行内容中提取出 top5 频次的关键词

- result.json，运行结果保存在 result.json 文件中，自动生成

### :rocket: 使用方法

1. 修改 config.json 文件，将 OpenApi、ApiKey、AiProxy 替换成自己的参数

2. 在 main.go 文件中启动 python

3. result.json 中查看分析结果
