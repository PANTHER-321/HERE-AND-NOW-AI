from google.adk.agents import Agent

hello_agent = Agent(
    name="Greeting Agent",
    model="gemini-2.5-flash",
    description="An friendly assistant that greets the user.",
    instruction="First, greet the user.and then Answer user questions politely."
)

root_agent = hello_agent