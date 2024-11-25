import openai

def initialize_openai_client():
    """
    初始化 OpenAI 客户端配置
    """
    openai.api_key = "eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI0MDIwMjcwMSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMjUxNDk4OSwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU3MTAxOTU4MDEiLCJ1dWlkIjoiOTRhYWFhMWYtNDMyZS00MjliLWFlZDYtZmJlNWY1ZDQyNmM0IiwiZW1haWwiOiIiLCJleHAiOjE3NDgwNjY5ODl9.hFr2wKsUbmOKdAqnARSbV3zetH7curabUs8wa390yt4o-nvawhGvBqUhNaxDq6I_XMM1z4eqDuB5v0j6wdNTig"  # 直接在此处替换为你的实际 token
    openai.api_base = "https://internlm-chat.intern-ai.org.cn/puyu/api/v1/"  # 替换为你的 base_url
    # 根据需要设置 api_type 和 api_version，如果不需要可以省略
    openai.api_type = "custom"  # 如果需要的话
    openai.api_version = "v1"   # 根据具体 API 需求设置

def create_chat_completion(client, messages, model="internlm2.5-latest", temperature=0.8, top_p=0.9):
    """
    创建聊天完成请求
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=top_p
        )
        return response
    except openai.error.OpenAIError as e:
        print(f"OpenAI API 错误: {e}")
        return None
    except Exception as e:
        print(f"其他错误: {e}")
        return None

def main():
    # 初始化 OpenAI 客户端
    initialize_openai_client()
    client = openai

    # 初始化对话历史
    messages = [
        {
            "role": "system",
            "content": "你是一个友好的助手。"
        }
    ]

    print("欢迎使用聊天助手！输入 'exit' 或 'quit' 以结束对话。\n")

    while True:
        user_input = input("你: ")
        if user_input.strip().lower() in ['exit', 'quit']:
            print("结束对话。再见！")
            break

        # 添加用户消息到对话历史
        messages.append({
            "role": "user",
            "content": user_input
        })

        # 发送消息并获取回复
        chat_rsp = create_chat_completion(client, messages)

        if chat_rsp and 'choices' in chat_rsp and len(chat_rsp['choices']) > 0:
            assistant_reply = chat_rsp['choices'][0]['message']['content']
            print(f"助手: {assistant_reply}")
            # 将助手的回复添加到对话历史
            messages.append({
                "role": "assistant",
                "content": assistant_reply
            })
        else:
            print("未能获得有效的回复，请稍后重试。")

if __name__ == "__main__":
    main()