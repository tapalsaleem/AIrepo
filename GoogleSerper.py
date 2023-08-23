import os
import pprint

os.environ["SERPER_API_KEY"] = "9d48bef1b1210520195e89aaa9924fbe909f3237"


from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType

llm = OpenAI(model_kwargs={'engine':"gpt-35-turbo"},temperature=0)
search = GoogleSerperAPIWrapper()
tools = [
    Tool(
        name="Intermediate Answer",
        func=search.run,
        description="useful for when you need to ask with search",
    )
]

self_ask_with_search = initialize_agent(
    tools, llm, agent=AgentType.SELF_ASK_WITH_SEARCH, verbose=False
)
self_ask_with_search.run(
    "What is Samsung Mobile latest model released in the market in the year 2022?"
)