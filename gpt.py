import requests
import openai
import loadData
import json


def sendGPT(CONFIG, context):
    # 将这里换成你在aiproxy api keys拿到的密钥
    openai.api_key = CONFIG['ApiKey']
    # 这里将官方的接口访问地址，替换成aiproxy的入口地址
    openai.api_base = CONFIG["AiProxy"]
    # 请求chat接口，调用gpt3.5模型
    res = openai.ChatCompletion.create(
        max_tokens=1000,
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": context}],
    )
    # 封装返回结果

    model = res.model
    created = res.created
    role = res.choices[0].message.role
    content = res.choices[0].message.content
    res_dict = {"model": model, "created": created,
                "role": role, "content": content}
    # 将dict对象序列化为json字符串
    return json.dumps(res_dict)

# gpt 返回 res 数据样式
# {
#   "model": "gpt-3.5-turbo",
#   "object": "chat.completion",
#   "usage": {
#     "prompt_tokens": 12,
#     "completion_tokens": 440,
#     "total_tokens": 452
#   },
#   "id": "chatcmpl-86utYJussgY9GYTtpKwpVrBYloZ9Q",
#   "created": 1696659364,
#   "choices": [
#     {
#       "index": 0,
#       "delta": null,
#       "message": {
#         "role": "assistant",
#         "content": "1. Developing new innovative products: Brainstorming ideas for product development can focus on identifying emerging trends and consumer needs. This could include exploring AI technologies, sustainable and eco-friendly products, smart home devices, etc.\n\n2. Expanding into new markets: Brainstorm ideas for entering new markets or expanding existing markets. This could involve conducting market research to identify untapped regions, exploring strategic partnerships, or developing localized products.\n\n3. Enhancing customer experience: Brainstorm ways to improve the overall customer experience on Alibaba's platform. This could involve improving website design and functionality, implementing personalized recommendations, or developing user-friendly mobile apps.\n\n4. Strengthening supply chain and logistics: Brainstorm ideas to optimize Alibaba's supply chain and logistics operations. This could involve exploring new technologies like blockchain for increased transparency, improving delivery speeds, or enhancing warehouse operations.\n\n5. Supporting small businesses: Brainstorm ways to better support small businesses and entrepreneurs using Alibaba's platform. This could include developing educational resources, providing mentorship programs, or offering additional funding options.\n\n6. Promoting sustainability: Brainstorm ideas for promoting sustainability within Alibaba's operations and encouraging green practices among its partners and suppliers. This could involve implementing eco-friendly packaging, incentivizing suppliers to use renewable energy, or supporting sustainable farming practices.\n\n7. Leveraging data analytics: Brainstorm ways to utilize Alibaba's vast data resources more effectively. This could involve developing new data analytics tools and insights to help sellers better understand and target their customers, or using data to identify emerging market trends.\n\n8. Strengthening brand reputation: Brainstorm ideas to enhance Alibaba's brand reputation. This could include initiatives to build trust and transparency, increase corporate social responsibility efforts, or engage in philanthropic endeavors.\n\n9. Empowering employees: Brainstorm ways to empower Alibaba's employees and foster a culture of innovation within the organization. This could include implementing employee training and development programs, encouraging cross-functional collaboration, or creating platforms for idea sharing.\n\n10. Expanding Alibaba's ecosystem: Brainstorm opportunities to expand Alibaba's ecosystem beyond e-commerce. This could involve exploring partnerships or acquisitions in sectors like fintech, entertainment, or healthcare to create a more comprehensive and interconnected ecosystem for users."
#       },
#       "finish_reason": "stop"
#     }
#   ]
# }
