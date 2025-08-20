from agno.agent import Agent  
from agno.models.google import Gemini  
from agno.app.agui.app import AGUIApp
  
# create Gemini agent
agent = Agent(  
    model=Gemini(id="gemini-2.0-flash-001"),  
    name="Gemini Chat Agent",  
    instructions="You are a helpful assistant.",  
    markdown=True,  
)  
  
agui_app = AGUIApp(agent=agent)

# get fastapi instance
app = agui_app.get_app()

# debug - print all routes
for route in app.routes:  
    print(f"Route: {route.path}") 
  
# start server
if __name__ == "__main__":    
    agui_app.serve(app=app, port=8000, reload=False)