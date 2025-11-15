# Chat Components

Professional chat interface components for building AI conversational UIs with EidosUI. Features auto-resizing textarea, file attachments, and model selection with HTMX-first design.

## Quick Start

```python
from eidos.components.chat import Chat, ChatMessage

# In your page headers - important!
*EidosHeaders(include_chat=True)

# In your body
Chat(
    ChatMessage("Hello! How can I help?", role="assistant"),
    action="/chat"
)
```

## Components

### Chat

Complete chat interface with messages container and input.

```python
from eidos.components.chat import Chat, ChatMessage

Chat(
    ChatMessage("Hello! How can I help?", role="assistant"),
    action="/chat",
    models=[("gpt-4", "GPT-4"), ("claude-3", "Claude 3")]
)
```

**Props:**
- `*initial_messages`: Initial chat messages to display
- `action`: Form action URL (default: `"/api/chat"`)
- `container_id`: Messages container ID (default: `"chat-messages"`)
- `input_id`: Input textarea ID (default: `"chat-input"`)
- `models`: List of (model_id, model_name) tuples
- `default_model`: Default selected model ID
- `class_`: Additional CSS classes

### ChatInput

Input component with textarea, file upload, and model selector.

```python
from eidos.components.chat import ChatInput

ChatInput(
    action="/chat",
    hx_target="#messages",
    placeholder="Ask me anything..."
)
```

**Props:**
- `action`: Form action URL (default: `"/api/chat"`)
- `method`: HTTP method (default: `"post"`)
- `placeholder`: Textarea placeholder
- `textarea_id`: Textarea element ID (default: `"chat-input"`)
- `hx_target`: HTMX target (default: `"#chat-messages"`)
- `hx_swap`: HTMX swap strategy (default: `"beforeend"`)
- `accept_files`: Accepted file types (default: `"image/*,.pdf,.txt,.doc,.docx"`)
- `max_files`: Maximum files (default: `5`)
- `show_model_selector`: Show model dropdown (default: `True`)
- `models`: List of (model_id, model_name) tuples
- `default_model`: Default selected model ID
- `class_`: Additional CSS classes

### ChatMessage

Single message component with role-based styling.

```python
ChatMessage("Hello!", role="user")
ChatMessage("Hi there!", role="assistant")
ChatMessage("Connection established", role="system")
```

**Props:**
- `message`: Message text content (required)
- `role`: Message role - `"user"`, `"assistant"`, or `"system"` (default: `"user"`)
- `class_`: Additional CSS classes

**Role Styling:**
- **user**: Primary light background, right-aligned
- **assistant**: Background with border, left-aligned
- **system**: Warning light background, center-aligned

### ChatContainer

Scrollable container for chat messages with auto-scroll.

```python
ChatContainer(
    ChatMessage("Message 1", role="user"),
    ChatMessage("Response 1", role="assistant"),
    container_id="messages"
)
```

**Props:**
- `*messages`: Initial message components
- `container_id`: Container element ID (default: `"chat-messages"`)
- `class_`: Additional CSS classes

## Usage Example

```python
from air import Air, Html, Head, Body, Title, Div
from eidos import *
from eidos.components.chat import Chat, ChatMessage

app = Air()

@app.page
def chat_page():
    return Html(
        Head(
            Title("Chat"),
            *EidosHeaders(include_chat=True),  # Important!
        ),
        Body(
            Div(
                Chat(
                    ChatMessage("Hello! How can I help?", role="assistant"),
                    action="/chat",
                ),
                class_="max-w-4xl mx-auto p-6 h-screen"
            )
        )
    ).render()

@app.post("/chat")
async def handle_chat(request: dict):
    message = request.get("message", "")
    model = request.get("model", "gpt-4o")
    
    # Process with your AI service
    response = f"You said: {message}"
    
    return ChatMessage(response, role="assistant").render()
```

## Features

### Auto-resizing Textarea
- Starts at 44px height
- Grows with content up to 200px
- Automatically managed by `chat.js`

### File Attachments
- Drag and drop support (coming soon)
- Multiple file uploads
- File preview with remove buttons
- Configurable max files and file types

### Keyboard Shortcuts
- **Enter**: Submit message
- **Shift+Enter**: New line in textarea

### HTMX Integration
- Form automatically posts to action URL
- Response appended to messages
- Form resets after successful submission
- Auto-scrolls to new messages

### Model Selection
- Optional dropdown for model selection
- Submitted with form data
- Customizable model list

## Styling

All components use CSS variables from the EidosUI theme system:

- `--color-primary-light`: User message background
- `--color-warning-light`: System message background
- `--color-surface`: Container and attachment backgrounds
- `--color-border`: Borders and dividers
- `--space-*`: Spacing scale
- `--radius-*`: Border radius scale
- `--font-size-*`: Typography scale

Custom styling can be added via the `class_` parameter or by overriding CSS classes in your theme.

## Accessibility

- Proper ARIA labels for inputs and buttons
- Semantic HTML structure
- Keyboard navigation support
- Role attributes on messages
- Focus management

## Browser Support

- Modern browsers with ES6+ support
- HTMX required for server interactions
- MutationObserver for auto-scroll (widely supported)
- File API for attachments (modern browsers)

## Architecture

Following EidosUI's layered architecture:

1. **CSS Variables** (`eidos-variables.css`): Theme values
2. **CSS Classes** (`styles.css`): Component styles using variables
3. **Python Style Classes** (`styles.py`): Expose CSS classes
4. **Tags** (`tags.py`): Styled Air tags
5. **Components** (`chat.py`): Complex UI from styled tags
6. **JavaScript** (`chat.js`): Minimal behavior (auto-resize, attachments)

## Related

- [Forms](../concepts/forms.md) - Form components and validation
- [Theming](../concepts/theming.md) - Customizing component styles
- [Architecture](../concepts/architecture.md) - Understanding the layer system
