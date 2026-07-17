from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

system_promt = """
You are a worldclass storyteller, create engaging, creative stories based on the user's request.

"""

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.8,
)

story_agent = create_agent(
    model = model,
    system_prompt= system_promt
)

def tell_story(topic: str, length: str):
    prompt = f"""
        Topic: {topic}
        Story length: {length}
        Write an engaing story.
    """
    
    response = story_agent.invoke(
        {"messages" : [HumanMessage(prompt)]}
    )

    return response["messages"][-1].content