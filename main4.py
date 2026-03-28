from agno.agent import Agent  
from agno.models.google import Gemini  
  
agent = Agent(model=Gemini(id="gemini-3-flash-preview"), markdown=True)  
agent.print_response("Share a 2 sentence horror story")
