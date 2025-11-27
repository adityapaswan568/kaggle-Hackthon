from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description="A coding agent that can write and execute code to answer user questions.",
    instruction='You are an expert software engineer Your goal is to write clean, efficient, and bug-free code.',
)
