from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)
from langchain.schema import SystemMessage
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

from tools.sql import run_query_tool, list_tables, describe_tables_tool
from tools.report import write_report_tool
from handlers.chat_model_start_handler import ChatModelStartHandler

load_dotenv()

handler = ChatModelStartHandler()

chat = ChatOpenAI(
    callbacks=[handler]
)

tables = list_tables()

memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

prompt = ChatPromptTemplate(
    messages=[
        SystemMessage(content=("You are an AI has access to a SQLite database.\n"
                               f"the database has tables of: \n{tables}"
                               "do not make any assumptions about what table exists "
                               "or what columns exists. instead, use the 'describe_tables' function")),
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ]
)

tools = [run_query_tool,
         describe_tables_tool,
         write_report_tool
]

agent = create_openai_functions_agent(
    llm=chat,
    prompt=prompt,
    tools=tools
)

agent_executor = AgentExecutor(
    agent=agent,
    verbose=True,
    tools=tools,
    memory=memory
)

input_text = {"input": "summarize the top 5 popular products. Write the result to a report file."}

result = agent_executor.invoke(input_text)
print(result)


