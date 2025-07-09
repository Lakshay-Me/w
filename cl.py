from pyscript import pyscript
from openai import OpenAI

# Set up client with OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

print("yo")
cz=document.querySelector("ta")
cz.innerText = "hi"
# Loop for user interaction
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break

    try:
        completion = client.chat.completions.create(
            model="deepseek/deepseek-chat-v3-0324:free",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        print("AI:", completion.choices[0].message.content)
    except Exception as e:
        print("Error:", e)
