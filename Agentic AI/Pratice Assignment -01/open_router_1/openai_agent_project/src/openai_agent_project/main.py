import asyncio
import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled
from dotenv import load_dotenv

load_dotenv()

# Load values from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
BASE_URL = os.getenv("BASE_URL")
MODEL = os.getenv("MODEL")

# Setup client
client = AsyncOpenAI(api_key=OPENROUTER_API_KEY, base_url=BASE_URL)
set_tracing_disabled(disabled=True)

# Main logic
async def main():
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL, openai_client=client),
    )

    result = await Runner.run(agent, "Tell me about recursion in programming.")
    print("\n🎯 Final Output:\n")
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
