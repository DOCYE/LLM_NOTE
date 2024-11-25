# 无法使用
import openai

# 初始化 OpenAI 客户端
openai.api_key = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI0MDIwMjcwMSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMjUxNDk4OSwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU3MTAxOTU4MDEiLCJ1dWlkIjoiOTRhYWFhMWYtNDMyZS00MjliLWFlZDYtZmJlNWY1ZDQyNmM0IiwiZW1haWwiOiIiLCJleHAiOjE3NDgwNjY5ODl9.hFr2wKsUbmOKdAqnARSbV3zetH7curabUs8wa390yt4o-nvawhGvBqUhNaxDq6I_XMM1z4eqDuB5v0j6wdNTig"  # 替换为你的实际 Token，不带 "Bearer"
openai.api_base = "https://internlm-chat.intern-ai.org.cn/puyu/api/v1/"

# 初始化对话历史
messages = [
    {"role": "user", "content": "你好~"}
]


def chat_with_puyu(user_input, messages):
    """
    与浦语 ChatAPI 进行对话，并更新消息历史。

    Args:
        user_input (str): 用户输入的内容。
        messages (list): 当前的消息历史。

    Returns:
        str: 助理的回复内容。
    """
    # 添加用户的输入到消息历史
    messages.append({"role": "user", "content": user_input})

    try:
        # 调用 API 获取回复
        response = openai.ChatCompletion.create(
            model="internlm2.5-latest",
            messages=messages,
            temperature=0.8,
            top_p=0.9,
            n=1
        )

        # 获取助理的回复
        assistant_message = response.choices[0].message['content']

        # 将助理的回复添加到消息历史
        messages.append({"role": "assistant", "content": assistant_message})

        return assistant_message

    except openai.error.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    while True:
        user_input = input("你: ")
        if user_input.lower() in ["退出", "exit", "quit"]:
            print("结束对话。")
            break
        reply = chat_with_puyu(user_input, messages)
        if reply:
            print(f"助理: {reply}")