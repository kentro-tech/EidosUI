"""Render API documentation using EidosUI components"""

import re
from textwrap import dedent
from typing import Any

from air.tags import H1, H3, A, Code, Div, Li, P, Span, Strong, Ul


def render_signature(name: str, signature: str) -> Any:
    """Render a function/method signature with syntax highlighting"""
    # Simple approach: just show the signature with colored name
    return Span(
        Span(name, style="color: var(--color-primary); font-weight: 600;"),
        Span(signature, style="color: var(--color-text-muted);"),
    )


def format_docstring(doc: str) -> list[Any]:
    """Format a docstring for better readability"""
    if not doc:
        return []

    elements = []
    lines = doc.strip().split("\n\n")  # Split into paragraphs

    for paragraph in lines:
        paragraph = paragraph.strip()
        if not paragraph:
            continue

        # Check for common section headers
        if paragraph.startswith(
            (
                "Args:",
                "Arguments:",
                "Parameters:",
                "Returns:",
                "Example:",
                "Note:",
                "Raises:",
            )
        ):
            header, _, content = paragraph.partition(":")
            elements.append(
                P(
                    Strong(header + ":"),
                    style="margin-top: 1rem; margin-bottom: 0.5rem;",
                )
            )
            if content.strip():
                # Parse parameter lists
                if header in ["Args", "Arguments", "Parameters"]:
                    param_lines = content.strip().split("\n")
                    items = []
                    for line in param_lines:
                        line = line.strip()
                        if ":" in line:
                            param_name, desc = line.split(":", 1)
                            items.append(Li(Code(param_name.strip()), ": ", desc.strip()))
                        elif line:
                            items.append(Li(line))
                    if items:
                        elements.append(
                            Ul(
                                *items,
                                style="margin: 0.5rem 0 1rem 1rem; list-style: disc;",
                            )
                        )
                else:
                    elements.append(
                        P(
                            content.strip(),
                            style="margin: 0.5rem 0 1rem 0; color: var(--color-text-muted);",
                        )
                    )

        # Code blocks (indented or with >>> )
        elif paragraph.startswith("    ") or ">>>" in paragraph:
            elements.append(
                Div(
                    Code(paragraph, style="display: block; white-space: pre;"),
                    style=dedent("""background-color: var(--color-surface);
                    padding: 1rem;
                    border-radius: 0.25rem;
                    margin: 0.5rem 0;
                    overflow-x: auto;
                    font-family: monospace;
                    font-size: 0.875rem;
                    """),
                )
            )

        # Regular paragraph
        else:
            # Basic inline formatting
            text = paragraph
            # Bold text
            text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
            text = re.sub(r"__(.*?)__", r"<strong>\1</strong>", text)
            # Italic text
            text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
            text = re.sub(r"_(.*?)_", r"<em>\1</em>", text)
            # Inline code
            text = re.sub(
                r"`(.*?)`",
                r'<code style="background:var(--color-surface);padding:2px 4px;border-radius:4px;">\1</code>',
                text,
            )

            elements.append(P(Span(text, _unsafe=True), style="margin: 0.5rem 0; line-height: 1.6;"))

    return elements


def render_item(item: dict[str, Any], module_name: str) -> Any:
    """Render a single API item"""
    item_type = item["type"]

    # Constants - simple one-liner
    if item_type == "constant":
        return P(
            Code(item["name"], style="color: var(--color-primary); font-weight: 600;"),
            Span(" = ", style="color: var(--color-text);"),
            Code(item["value"], style="color: var(--color-success);"),
            Span(
                f"  # {item['value_type']}",
                style="color: var(--color-text-subtle); font-size: 0.875rem;",
            ),
            style="margin: 1rem 0; font-family: monospace;",
        )

    elements = []

    # Header with GitHub link
    if item_type == "function":
        header = H3(
            render_signature(item["name"], item["signature"]),
            style="font-family: monospace; font-size: 1.125rem; margin-bottom: 0.5rem;",
        )
        border_color = "var(--color-primary)"
    else:  # class
        header = H3(
            Span("class ", style="color: var(--color-text-muted);"),
            Span(item["name"], style="color: var(--color-primary); font-weight: 600;"),
            Span(
                f"({', '.join(item.get('bases', []))})" if item.get("bases") else "",
                style="color: var(--color-text-muted);",
            ),
            style="font-family: monospace; font-size: 1.125rem; margin-bottom: 0.5rem;",
        )
        border_color = "var(--color-accent)"

    # Add GitHub link
    file_path = module_name.replace(".", "/") + ".py"
    github_link = A(
        "GitHub",
        href=f"https://github.com/kentro-tech/eidosui/blob/main/{file_path}#{item['name']}",
        target="_blank",
        style="color: var(--color-primary); font-size: 0.75rem; float: right; opacity: 0.7;",
    )

    elements.append(Div(header, github_link, style="overflow: hidden;"))

    # Docstring with formatting
    if item.get("doc"):
        elements.extend(format_docstring(item["doc"]))

    # Parameters (simplified but readable)
    if item_type == "function" and item.get("params"):
        # Only show if params have annotations or defaults
        meaningful_params = [p for p in item["params"] if p.get("annotation") or p.get("default")]
        if meaningful_params:
            param_list = []
            for param in meaningful_params:
                parts = [
                    Code(param["name"], style="color: var(--color-accent);"),
                ]
                if param.get("annotation"):
                    parts.append(Span(": ", style="color: var(--color-text);"))
                    parts.append(
                        Span(
                            param["annotation"],
                            style="color: var(--color-text-muted); font-style: italic;",
                        )
                    )
                if param.get("default"):
                    parts.append(Span(" = ", style="color: var(--color-text);"))
                    parts.append(Span(param["default"], style="color: var(--color-success);"))
                param_list.append(Li(*parts, style="margin: 0.25rem 0;"))

            if param_list:
                elements.append(
                    Div(
                        P(Strong("Parameters:"), style="margin: 1rem 0 0.5rem 0;"),
                        Ul(
                            *param_list,
                            style="list-style: none; padding-left: 1rem; font-family: monospace; font-size: 0.875rem;",
                        ),
                        style="margin: 1rem 0;",
                    )
                )

    # Return type
    if item.get("return_type"):
        elements.append(
            P(
                Strong("Returns: "),
                Code(
                    item["return_type"],
                    style="background-color: var(--color-surface); padding: 0.125rem 0.25rem; border-radius: 0.25rem;",
                ),
                style="margin: 0.5rem 0; font-size: 0.875rem;",
            )
        )

    # Methods (simplified)
    if item_type == "class" and item.get("methods"):
        method_items = []
        for method in item["methods"]:
            doc_preview = f" — {method['doc']}" if method.get("doc") else ""
            method_items.append(
                Li(
                    Code(
                        f"{method['name']}{method['signature']}",
                        style="color: var(--color-primary);",
                    ),
                    Span(
                        doc_preview,
                        style="color: var(--color-text-muted); font-size: 0.875rem;",
                    ),
                    style="margin: 0.5rem 0;",
                )
            )

        if method_items:
            elements.append(
                Div(
                    P(Strong("Methods:"), style="margin-top: 1rem;"),
                    Ul(
                        *method_items,
                        style="list-style: none; padding-left: 1rem; font-family: monospace; font-size: 0.875rem;",
                    ),
                    style="margin: 1rem 0;",
                )
            )

    return Div(
        *elements,
        style=f"border-left: 3px solid {border_color}; padding-left: 1.5rem; margin: 2rem 0;",
    )


def render_api_page(api_data: dict[str, Any]) -> Any:
    """Render API documentation page"""
    if "error" in api_data:
        return Div(H1("Error", style="color: var(--color-error);"), P(api_data["error"]))

    elements = [H1(api_data["module"], style="font-size: 2rem; margin-bottom: 1rem;")]

    if api_data.get("doc"):
        module_doc = Div(
            *format_docstring(api_data["doc"]),
            style=dedent("""font-size: 1.125rem;
            margin-bottom: 2rem;
            padding: 1rem;
            background-color: var(--color-surface);
            border-radius: 0.5rem;
            """),
        )
        elements.append(module_doc)

    # Render all items in order
    for item in api_data.get("items", []):
        elements.append(render_item(item, api_data["module"]))

    return Div(*elements, style="max-width: 60rem; margin: 0 auto; padding: 2rem;")


def render_api_index(modules: list[str]) -> Any:
    """Render API index page"""
    return Div(
        H1("API Reference", style="font-size: 2rem; margin-bottom: 2rem;"),
        Ul(
            *[
                Li(
                    A(
                        module,
                        href=f"/api/{module}",
                        style="color: var(--color-primary);",
                    )
                )
                for module in sorted(modules)
            ],
            style="list-style: none; line-height: 1.8;",
        ),
        style="max-width: 40rem; margin: 0 auto; padding: 2rem;",
    )
