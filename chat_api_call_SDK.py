from openai import OpenAI

client = OpenAI(
    api_key="eyJ0eXBlIjoiSldUIiwiYWxnIjoiSFM1MTIifQ.eyJqdGkiOiI0MDIwMjcwMSIsInJvbCI6IlJPTEVfUkVHSVNURVIiLCJpc3MiOiJPcGVuWExhYiIsImlhdCI6MTczMjUxNDk4OSwiY2xpZW50SWQiOiJlYm1ydm9kNnlvMG5semFlazF5cCIsInBob25lIjoiMTU3MTAxOTU4MDEiLCJ1dWlkIjoiOTRhYWFhMWYtNDMyZS00MjliLWFlZDYtZmJlNWY1ZDQyNmM0IiwiZW1haWwiOiIiLCJleHAiOjE3NDgwNjY5ODl9.hFr2wKsUbmOKdAqnARSbV3zetH7curabUs8wa390yt4o-nvawhGvBqUhNaxDq6I_XMM1z4eqDuB5v0j6wdNTig",  # 此处传token，不带Bearer
    base_url="https://internlm-chat.intern-ai.org.cn/puyu/api/v1/",
)

chat_rsp = client.chat.completions.create(
    model="internlm2.5-latest",
    messages=[{"role": "user", "content": "hello"}],
)

for choice in chat_rsp.choices:
    print(choice.message.content)

