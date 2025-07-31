from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub
from langchain.tools import tool
from dotenv import load_dotenv
import os
import ast 

load_dotenv()
google_api_key = os.getenv("GEMINI_API_KEY")    
model = "gemini-2.5-flash-lite"

@tool
def web_scrape_tool(urls: str) -> str:
    """
    Scrapes content from a list of URLs.
    The input should be a sting representation of a python list of URLs
    (e.g., "['https://hereandnowai.com', 'https://hereandnowai.co.in']")
    Returns the concatenated text of all the scraped pages.
    """

    try:
        url_list = ast.literal_eval(urls)
        if not isinstance(url_list, list) or not all(isinstance(url, str) for url in url_list):
            return "Invalid input format. Please provide a list of URLs as a string (e.g.,\" ['https://hereandnowai.com', 'https://hereandnowai.co.in']\")."
    except (ValueError, SyntaxError):
        return "Invalid input format. Please provide a list of URLs as a string (e.g., \"['https://hereandnowai.com', 'https://hereandnowai.co.in']\")."

    combined_content = []
    for url in url_list:
        try:
            loader = WebBaseLoader(
                [url], requests_kwargs={"headers": {"User-Agent": "Caramel AI"}}
            )
            documents = loader.load()
            for doc in documents:
                combined_content.append(doc.page_content)  
        except Exception as e:
            combined_content.append(f"Error scraping {url}: Error: {e}")
    return "\n\n".join(combined_content)

def run_web_scraping_agent():
    """"
    Creates and runs an agent that can use the wen scrape tool
    """                
    llm = ChatGoogleGenerativeAI(model=model, google_api_key=google_api_key)
    tool = [web_scrape_tool]
    prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm, tool, prompt=prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tool, verbose=True,handle_parsing_errors=True)

    print("\n--- Query 1: Get the content from the Home page  ---")
    question_home_page = "What is the story of HERE AND NOW AI? The url is https://hereandnowai.com"
    response_home_page = agent_executor.invoke({"input": question_home_page})
    print(f"Agent's response: {response_home_page['output']}")

if __name__ == "__main__":
    run_web_scraping_agent()    