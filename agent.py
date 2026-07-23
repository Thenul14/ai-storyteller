from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

system_promt = """
You are a worldclass storyteller, create engaging, creative stories based on the user's request.

Always call the generate_title tool first.
Then write the story.
Do not include the title in the AIMessage
"""
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.8,
)


@tool
def generate_title(topic: str) -> str:
    """Generate a short and creative title for a story."""

    response = model.invoke(
        f"Generate a creative title for a story about {topic}. Only return the title."
    )

    return response.content

story_agent = create_agent(
    model = model,
    tools=[generate_title],
    system_prompt= system_promt
)

def extract_text(content):
    if isinstance(content, str):
        return content

    if isinstance(content, list):
        return "".join(
            block.get("text", "")
            for block in content
            if isinstance(block, dict)
        )

    return str(content)

def tell_story(topic: str, length: str, genre: str):
    prompt = f"""
        Topic: {topic}
        Story length: {length}
        Genre: {genre}
        Write an engaing story.
    """

    response = story_agent.invoke(
        {"messages" : [HumanMessage(prompt)]}
    )

    title = ""
    
    for message in response["messages"]:
        if isinstance(message, ToolMessage):
            title = extract_text(message.content)
            break
    
    story = extract_text(response["messages"][-1].content)

    
    return {
        "title" : title,
        "story" : story
    }