from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(model='claude-3.5-sonnet-20241022', temperature = 1.4, max_completion_token = 15)
result = model.invoke("Tell me something I don't know")

print(result.content)

