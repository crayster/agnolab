from agno.agent import Agent  
from agno.models.google import Gemini  
from agno.memory.v2 import Memory  
from agno.storage.sqlite import SqliteStorage  
from rich.prompt import Prompt  
from rich.console import Console  
import uuid  
  
def create_chat_agent():  
    """创建支持session和memory的Gemini聊天代理"""  
    # 创建内存管理器  
    memory = Memory(  
        model=Gemini(id="gemini-2.0-flash-exp")  
    )  
      
    # 创建存储管理器  
    storage = SqliteStorage(  
        table_name="chat_sessions",   
        db_file="tmp/chat_storage.db"  
    )  
      
    # 创建Agent  
    agent = Agent(  
        model=Gemini(id="gemini-2.0-flash-exp"),  
        memory=memory,  
        storage=storage,  
        # 启用历史消息添加到上下文  
        add_history_to_messages=True,  
        # 保留最近3轮对话历史  
        num_history_runs=3,  
        # 启用session摘要  
        enable_session_summaries=True,  
        description="你是一个友好的AI助手，能够记住对话上下文并进行多轮交互。"  
    )  
      
    return agent  
  
def main():  
    """主聊天循环"""  
    console = Console()  
    agent = create_chat_agent()  
      
    # 生成唯一的session ID  
    session_id = str(uuid.uuid4())  
    user_id = "default_user"  
      
    console.print("[bold green]🤖 Gemini聊天助手已启动！[/bold green]")  
    console.print(f"[dim]Session ID: {session_id}[/dim]")  
    console.print("[dim]输入 'exit' 退出聊天[/dim]\n")  
      
    conversation_count = 0  
    max_conversations = 20  # 设置对话上限  
      
    while True:  
        try:  
            # 获取用户输入  
            user_input = Prompt.ask("[bold blue]您[/bold blue]")  
              
            # 检查退出条件  
            if user_input.lower() in ['exit', 'quit', '退出']:  
                console.print("[yellow]👋 再见！[/yellow]")  
                break  
              
            # 检查对话数量限制  
            conversation_count += 1  
            if conversation_count > max_conversations:  
                console.print(f"[yellow]⚠️  对话已达到上限({max_conversations}轮)，会话将被重置...[/yellow]")  
                # 重置session  
                session_id = str(uuid.uuid4())  
                conversation_count = 1  
                console.print(f"[dim]新的 Session ID: {session_id}[/dim]\n")  
              
            # 发送消息并获取回复  
            console.print("[bold green]🤖 Gemini[/bold green]: ", end="")  
            agent.print_response(  
                message=user_input,  
                session_id=session_id,  
                user_id=user_id,  
                stream=True,  
                markdown=True  
            )  
              
            print()  # 添加换行  
              
        except KeyboardInterrupt:  
            console.print("\n[yellow]👋 聊天已中断，再见！[/yellow]")  
            break  
        except Exception as e:  
            console.print(f"[red]❌ 发生错误: {e}[/red]")  
            continue  
  
if __name__ == "__main__":  
    main()
