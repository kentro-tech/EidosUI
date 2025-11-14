"""Chat input component for EidosUI.

Provides a chat interface with textarea, file attachments, and model selection.
Designed for HTMX-first interactions.
"""

from typing import Any, Literal

import air
from air import Button, Div, Form, Input, Label, Span, Tag, Template, Textarea

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
    models: list[tuple[str, str]] | None = None,
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Chat input component with textarea, file upload, and optional model selector.

    Args:
        action: Form action URL for HTMX post
        method: HTTP method (post or get)
        placeholder: Placeholder text for textarea
        textarea_id: ID for the textarea element
        hx_target: HTMX target for chat messages
        hx_swap: HTMX swap strategy
        accept_files: File types to accept for upload
        max_files: Maximum number of files allowed
        models: List of (model_id, model_name) tuples. If None, no model selector shown. First model is selected by default
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
            ]
        )
    """
    # Model selector setup
    model_selector = ""
    if models:
        default_model = models[0][0]
        model_selector = Div(
            Label("Model:", for_=f"{textarea_id}-model", class_="eidos-chat-model-label"),
            Select(
                *[Option(name, value=model_id, selected=(model_id == default_model)) for model_id, name in models],
                id=f"{textarea_id}-model",
                name="model",
                class_="eidos-chat-model-select",
            ),
            class_="eidos-chat-input-model",
        )

    # File attachment button
    attach_button = Button(
        air.I(data_lucide="paperclip", class_="w-4 h-4"),
        type="button",
        class_=stringify(styles.buttons.ghost, "eidos-chat-input-tool"),
        **{
            "@click": f"$el.closest('form').querySelector('#{textarea_id}-files').click()",
            "aria-label": "Attach files",
        },
    )

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
                **{
                    "data-max-files": str(max_files),
                    "@change": f"if ($el.files.length > {max_files}) {{ alert('Maximum {max_files} files'); $el.value = ''; return; }} files = Array.from($el.files)",
                },
            ),
            # Attachments preview
            Div(
                Template(
                    Div(
                        Span(class_="eidos-chat-attachment-name", **{"x-text": "file.name"}),
                        Button(
                            "✕",
                            type="button",
                            class_="eidos-chat-attachment-remove",
                            **{
                                "@click": f"files = files.filter(f => f !== file); if (!files.length) $el.closest('form').querySelector('#{textarea_id}-files').value = ''",
                                "aria-label": "Remove file",
                            },
                        ),
                        class_="eidos-chat-attachment",
                    ),
                    **{"x-for": "file in files", ":key": "file.name"},
                ),
                id=f"{textarea_id}-attachments",
                class_="eidos-chat-attachments",
                **{":class": "{ 'has-files': files.length > 0 }"},
            ),
            # Main input
            Div(
                Textarea(
                    id=textarea_id,
                    name="message",
                    placeholder=placeholder,
                    rows=1,
                    class_="eidos-chat-input-textarea",
                    **{
                        "aria-label": "Chat message input",
                        "@input": "$el.style.height = '44px'; $el.style.height = Math.min($el.scrollHeight, 200) + 'px'",
                        "@keydown.enter.prevent": "if (!$event.shiftKey) $el.closest('form').requestSubmit()",
                    },
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
                Div(attach_button, class_="eidos-chat-input-tools"),
                model_selector,
                class_="eidos-chat-input-footer",
            ),
            **{
                "hx-post": action if method == "post" else "",
                "hx-target": hx_target,
                "hx-swap": hx_swap,
                "@htmx:after-request": f"$el.reset(); $el.querySelector('#{textarea_id}').style.height = '44px'; files = []",
                "x-data": "{ files: [] }",
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
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Complete chat interface with messages and input.

    Args:
        initial_messages: Initial chat messages to display
        action: Form action URL for sending messages
        container_id: ID for messages container
        input_id: ID for input textarea
        models: List of (model_id, model_name) tuples. First model is selected by default
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
        ),
        class_=stringify("eidos-chat", class_),
        **kwargs,
    )
