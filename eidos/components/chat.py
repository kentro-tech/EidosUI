"""Chat input component for EidosUI.

Provides a chat interface with textarea, file attachments, and model selection.
Designed for HTMX-first interactions.
"""

from typing import Any, Literal

import air
from air import Button, Div, Form, Input, Label, Span, Tag, Textarea

from .. import styles
from ..tags import Select, Option
from ..utils import stringify


def ChatInput(
    *,
    action: str = "/api/chat",
    method: Literal["post", "get"] = "post",
    placeholder: str = "What would you like to know?",
    textarea_id: str = "chat-input",
    hx_target: str = "#chat-messages",
    hx_swap: Literal[
        "innerHTML", "outerHTML", "beforebegin", "afterbegin", "beforeend", "afterend", "delete", "none"
    ] = "beforeend",
    accept_files: str = "image/*,.pdf,.txt,.doc,.docx",
    max_files: int = 5,
    show_model_selector: bool = True,
    models: list[tuple[str, str]] | None = None,
    default_model: str | None = None,
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Chat input component with textarea, file upload, and model selector.

    Args:
        action: Form action URL for HTMX post
        method: HTTP method (post or get)
        placeholder: Placeholder text for textarea
        textarea_id: ID for the textarea element
        hx_target: HTMX target for chat messages
        hx_swap: HTMX swap strategy
        accept_files: File types to accept for upload
        max_files: Maximum number of files allowed
        show_model_selector: Whether to show model dropdown
        models: List of (model_id, model_name) tuples
        default_model: Default selected model ID
        class_: Additional CSS classes

    Returns:
        Tag: The chat input component

    Example:
        ChatInput(
            action="/chat",
            hx_target="#messages",
            models=[
                ("gpt-4", "GPT-4"),
                ("claude-3", "Claude 3")
            ],
            default_model="gpt-4"
        )
    """
    if models is None:
        models = [
            ("gpt-4o", "GPT-4o"),
            ("claude-opus-4", "Claude 4 Opus"),
        ]

    if default_model is None and models:
        default_model = models[0][0]

    return Div(
        Form(
            # Hidden file input
            Input(
                type="file",
                id=f"{textarea_id}-files",
                name="files",
                accept=accept_files,
                multiple=True,
                class_="hidden",
                **{"data-max-files": str(max_files)},
            ),
            # Attachments preview
            Div(id=f"{textarea_id}-attachments", class_="eidos-chat-attachments"),
            # Main input
            Div(
                Textarea(
                    id=textarea_id,
                    name="message",
                    placeholder=placeholder,
                    rows=1,
                    class_="eidos-chat-input-textarea",
                    **{"aria-label": "Chat message input"},
                ),
                Button(
                    air.I(data_lucide="send", class_="w-5 h-5"),
                    type="submit",
                    class_=stringify(styles.buttons.primary, "eidos-chat-input-submit"),
                    **{"aria-label": "Send message"},
                ),
                class_="eidos-chat-input-main",
            ),
            # Footer with tools
            Div(
                Div(
                    Button(
                        air.I(data_lucide="paperclip", class_="w-4 h-4"),
                        type="button",
                        class_=stringify(styles.buttons.ghost, "eidos-chat-input-tool"),
                        onclick=f"document.getElementById('{textarea_id}-files').click()",
                        **{"aria-label": "Attach files"},
                    ),
                    class_="eidos-chat-input-tools",
                ),
                Div(
                    Label("Model:", for_=f"{textarea_id}-model", class_="eidos-chat-model-label")
                    if show_model_selector
                    else Span(),
                    Select(
                        *[
                            Option(name, value=model_id, selected=(model_id == default_model))
                            for model_id, name in models
                        ],
                        id=f"{textarea_id}-model",
                        name="model",
                        class_="eidos-chat-model-select",
                    )
                    if show_model_selector
                    else Span(),
                    class_="eidos-chat-input-model",
                ),
                class_="eidos-chat-input-footer",
            ),
            **{
                "hx-post": action if method == "post" else "",
                "hx-target": hx_target,
                "hx-swap": hx_swap,
                "data-chat-input": textarea_id,
            },
        ),
        class_=stringify("eidos-chat-input", class_),
        **kwargs,
    )


def ChatMessage(
    message: str,
    role: Literal["user", "assistant", "system"] = "user",
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Single chat message component.

    Args:
        message: The message text
        role: Message role (user, assistant, or system)
        class_: Additional CSS classes

    Returns:
        Tag: The chat message component

    Example:
        ChatMessage("Hello!", role="user")
        ChatMessage("Hi there!", role="assistant")
    """
    role_labels = {
        "user": "You",
        "assistant": "Assistant",
        "system": "System",
    }

    return Div(
        Div(
            Span(role_labels[role], class_="eidos-chat-message-role"),
            Div(message, class_="eidos-chat-message-text"),
            class_="eidos-chat-message-content",
        ),
        class_=stringify(
            "eidos-chat-message",
            f"eidos-chat-message-{role}",
            class_,
        ),
        **{"data-role": role},
        **kwargs,
    )


def ChatContainer(
    *messages: Tag,
    container_id: str = "chat-messages",
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Container for chat messages with auto-scroll.

    Args:
        messages: Initial message components
        container_id: ID for the container element
        class_: Additional CSS classes

    Returns:
        Tag: The chat messages container

    Example:
        ChatContainer(
            ChatMessage("Hello!", role="user"),
            ChatMessage("Hi there!", role="assistant"),
            container_id="messages"
        )
    """
    return Div(
        Div(
            *messages,
            class_="eidos-chat-messages",
        ),
        id=container_id,
        class_=stringify("eidos-chat-container", class_),
        **{"data-chat-container": "true"},
        **kwargs,
    )


def Chat(
    *initial_messages: Tag,
    action: str = "/api/chat",
    container_id: str = "chat-messages",
    input_id: str = "chat-input",
    models: list[tuple[str, str]] | None = None,
    default_model: str | None = None,
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Complete chat interface with messages and input.

    Args:
        initial_messages: Initial chat messages to display
        action: Form action URL for sending messages
        container_id: ID for messages container
        input_id: ID for input textarea
        models: List of (model_id, model_name) tuples
        default_model: Default selected model ID
        class_: Additional CSS classes

    Returns:
        Tag: The complete chat interface

    Example:
        Chat(
            ChatMessage("Welcome!", role="assistant"),
            action="/chat",
            models=[("gpt-4", "GPT-4"), ("claude-3", "Claude 3")]
        )
    """
    return Div(
        ChatContainer(*initial_messages, container_id=container_id),
        ChatInput(
            action=action,
            textarea_id=input_id,
            hx_target=f"#{container_id} .eidos-chat-messages",
            hx_swap="beforeend",
            models=models,
            default_model=default_model,
        ),
        class_=stringify("eidos-chat", class_),
        **kwargs,
    )
