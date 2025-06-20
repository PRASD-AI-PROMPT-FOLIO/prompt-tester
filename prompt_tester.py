from openai import OpenAI

# ✅ Replace this with your real API key from OpenAI
client = OpenAI(api_key=" 
prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("\nGPT says:", response.choices[0].message.content)
