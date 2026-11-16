from config.config import agent_llm

response = agent_llm.call(
    messages=[
        {
            "role": "user",
            "content": "Reply with exactly: GPT connection successful"
        }
    ]
)

print("\nLLM RESPONSE:")
print(response)