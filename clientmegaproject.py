from openai import OpenAI
client=OpenAI(api_key="sk-proj-mcwmFhYcMI4dpMtJrB4OT3BlbkFJ5JK1cSkj2jQxEM5XYNdL",)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant Jarvis, skilled in general tak like alexa,google"},
    {"role": "user", "content": "What is coding."}
  ]
)

print(completion.choices[0].message)