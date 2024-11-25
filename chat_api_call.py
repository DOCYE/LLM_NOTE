import requests
import json

# API 端点
url = 'https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions'

# 请求头，包括内容类型和授权信息
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI0MDIwMjcwMSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMjUxNDk4OSwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU3MTAxOTU4MDEiLCJ1dWlkIjoiOTRhYWFhMWYtNDMyZS00MjliLWFlZDYtZmJlNWY1ZDQyNmM0IiwiZW1haWwiOiIiLCJleHAiOjE3NDgwNjY5ODl9.hFr2wKsUbmOKdAqnARSbV3zetH7curabUs8wa390yt4o-nvawhGvBqUhNaxDq6I_XMM1z4eqDuB5v0j6wdNTig'  # 替换为你的实际 token
}

# 请求数据
data = {
    "model": "internlm2.5-latest",
    "messages": [{
        "role": "user",
        "content": "你好~"
    }],
    "n": 1,
    "temperature": 0.8,
    "top_p": 0.9
}

try:
    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    # 检查响应状态码
    if response.status_code == 200:
        response_data = response.json()
        print("响应状态码:", response.status_code)
        print("完整响应内容:")
        print(json.dumps(response_data, indent=4, ensure_ascii=False))

        # 获取助手的回复
        assistant_reply = response_data["choices"][0]["message"]["content"]
        print("\n助手回复:", assistant_reply)
    else:
        print("请求失败，状态码:", response.status_code)
        print("响应内容:", response.text)
except Exception as e:
    print("请求过程中发生错误:", str(e))
