"""Example demonstrating EidosUI chat components."""

import air
from eidos import *
from eidos.components.chat import Chat, ChatMessage
from eidos.components.navigation import NavBar
from eidos.components.theme import ThemeSwitch
from eidos.utils import get_eidos_static_files

# Create Air app
app = air.Air()

# Mount static files
for mount_path, directory in get_eidos_static_files().items():
    app.mount(mount_path, air.StaticFiles(directory=directory), name=mount_path.strip("/"))


@app.page
def index():
    """Professional chat interface with navigation."""
    return Html(
        Head(
            Title("AI Chat Assistant - EidosUI"),
            *EidosHeaders(include_chat=True),
            Script(src="https://unpkg.com/htmx.org@2.0.3"),
        ),
        Body(
            # Navigation bar
            NavBar(
                ThemeSwitch(),
                lcontents=Div(
                    H2("AI Assistant", class_="text-xl font-bold"),
                ),
                sticky=True,
            ),
            # Main content
            Div(
                # Header section
                Div(
                    H1("Chat with AI"),
                    P(
                        "Ask questions, get help with coding, or just have a conversation.",
                        class_="text-gray-600 dark:text-gray-400",
                    ),
                    class_="mb-6",
                ),
                # Chat interface
                Div(
                    Chat(
                        ChatMessage(
                            "Hello! I'm your AI assistant. I can help you with coding questions, explanations, or general conversation. What would you like to know?",
                            role="assistant",
                        ),
                        action="/chat",
                        models=[
                            ("gpt-4o", "GPT-4o"),
                            ("claude-opus-4", "Claude Opus"),
                            ("gemini-pro", "Gemini Pro"),
                        ],
                    ),
                    class_="border rounded-lg shadow-sm h-[calc(100vh-300px)] min-h-[500px]",
                ),
                class_="max-w-5xl mx-auto p-6",
            ),
        ),
    ).render()


@app.post("/chat")
async def handle_chat(message: str = "", model: str = "gpt-4o"):
    """Handle chat messages and echo back."""
    # Build response
    response_parts = [f"You said: {message}"]
    response_parts.append(f"\nModel: {model}")
    
    response = "\n".join(response_parts)
    return ChatMessage(response, role="assistant").render()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
