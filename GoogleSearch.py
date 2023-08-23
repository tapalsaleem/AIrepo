import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyDZvhCBtW-mCukPgiD_S4iEvZGvSrjLGII"

os.environ["GOOGLE_CSE_ID"] = "12f59f3a6c5e04fca"

from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()

tool = Tool(
    name="Google Search",
    description="Search Google for recent results.",
    func=search.run,
)

print(tool.run("waht is the latest Samsung mobile model release in the year 2023 ?"))