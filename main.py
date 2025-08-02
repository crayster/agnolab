from agno.agent import Agent  
from agno.models.google import Gemini  
from agno.playground import Playground, serve_playground_app
  
# create Gemini agent
agent = Agent(  
    model=Gemini(id="gemini-2.0-flash-001"),  
    name="Gemini Chat Agent",  
    instructions="You are a helpful assistant.",  
    markdown=True,  
)  
  
# create Playground
playground = Playground(  
    agents=[agent],  
    app_id="gemini-demo",  
    name="Gemini Demo",  
    description="A simple Gemini chat agent"  
)

# get fastapi instance
app = playground.get_app()

# debug - print all routes
for route in app.routes:  
    print(f"Route: {route.path}") 
  
# start server
if __name__ == "__main__":    
    serve_playground_app(app=app, port=7777)