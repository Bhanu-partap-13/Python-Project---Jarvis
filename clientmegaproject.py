from openai import OpenAI
client=OpenAI(api_key="<Enter your API KEY>",)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant Jarvis, skilled in general tak like alexa,google"},
    {"role": "user", "content": "What is coding."}
  ]
)

print(completion.choices[0].message)