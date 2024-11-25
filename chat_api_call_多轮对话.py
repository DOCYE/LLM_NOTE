import requests
import json

# 您的 API Token，请妥善保管，勿在公开环境中暴露
API_TOKEN = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI0MDIwMjcwMSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMjUxNDk4OSwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU3MTAxOTU4MDEiLCJ1dWlkIjoiOTRhYWFhMWYtNDMyZS00MjliLWFlZDYtZmJlNWY1ZDQyNmM0IiwiZW1haWwiOiIiLCJleHAiOjE3NDgwNjY5ODl9.hFr2wKsUbmOKdAqnARSbV3zetH7curabUs8wa390yt4o-nvawhGvBqUhNaxDq6I_XMM1z4eqDuB5v0j6wdNTig"

# API 端点
url = 'https://internlm-chat.intern-ai.org.cn/puyu/api/v1/chat/completions'

# 初始化对话历史
messages = [
    {"role": "system", "content": "你是一个乐于助人的助手。"}
]


def get_response(user_input):
    global messages

    # 添加用户输入到对话历史
    messages.append({"role": "user", "content": user_input})

    # 构建请求数据
    data = {
        "model": "internlm2.5-latest",
        "messages": messages,
        "n": 1,
        "temperature": 0.8,
        "top_p": 0.9
    }

    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {API_TOKEN}"
    }

    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        res_json = response.json()
        assistant_message = res_json["choices"][0]["message"]["content"]
        print(f"助手: {assistant_message}\n")

        # 将助手回复添加到对话历史
        messages.append({"role": "assistant", "content": assistant_message})
    else:
        print(f"请求失败，状态码: {response.status_code}")
        print(f"错误信息: {response.text}")


# 示例对话
if __name__ == "__main__":
    print("欢迎使用多轮问答系统。输入 '退出' 结束对话。\n")
    while True:
        user_input = input("用户: ")
        if user_input.lower() in ['退出', 'exit']:
            print("结束对话。")
            break
        get_response(user_input)