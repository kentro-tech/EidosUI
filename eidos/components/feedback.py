"""Feedback collection component for EidosUI.

Simple feedback widget with modal dialog and form submission.
"""

from collections.abc import Callable
from typing import Any

import air
from airpine import Alpine

from .. import styles
from ..tags import H3, Button, Div, Form, Input, Strong, Textarea
from ..utils import stringify


class Feedback:
    """Flexible feedback collection system using Eidos styling and Airpine."""

    def __init__(
        self,
        on_save: Callable[[int, str, str | None], Any],
        route_path: str = "/feedback",
        button_text: str = "💬 Feedback",
        success_message: str = "✓ Thanks for your feedback!",
        error_message: str = "Feedback cannot be empty",
    ):
        """
        Initialize Feedback component.

        Args:
            on_save: Async callback(user_id, text, route) to save feedback
            route_path: URL path for feedback submission (default: /feedback)
            button_text: Text for feedback button (default: 💬 Feedback)
            success_message: Message shown on successful submission
            error_message: Message shown on validation error
        """
        self.on_save = on_save
        self.route_path = route_path
        self.button_text = button_text
        self.success_message = success_message
        self.error_message = error_message

    async def _submit_handler(self, request: air.Request, user: Any):
        """Handle feedback submission."""
        form = await request.form()
        text = form.get("text", "").strip()
        route = form.get("route", "")

        if text:
            # Get user ID - flexible to handle different user objects
            user_id = user.id if hasattr(user, "id") else user

            await self.on_save(user_id, text, route if route else None)

            return Div(
                Strong(self.success_message, style="color: var(--color-success)"),
                id="feedback-result",
            )

    def widget(
        self,
        button_class: str = "",
        modal_class: str = "",
        title: str = "Share Your Feedback",
        title_class: str = "",
        placeholder: str = "What's on your mind? Bugs, feature requests, or just say hi!",
        submit_text: str = "Submit",
        cancel_text: str = "Cancel",
    ) -> air.Div:
        """
        Returns complete feedback widget (button + modal) with shared Alpine.js scope.

        Args:
            button_class: Additional CSS classes for button
            modal_class: Additional CSS classes for modal backdrop
            title: Modal title text
            title_class: Additional CSS classes for title
            placeholder: Textarea placeholder text
            submit_text: Text for submit button
            cancel_text: Text for cancel button
        """
        # Alpine.js data initialization at container level
        alpine_data = Alpine.x.data(
            {
                "feedbackModal": False, # Modal visibility state
                "feedbackRoute": "", # Current page route for context
            }
        )

        # Modal backdrop with click-outside-to-close
        modal_backdrop_classes = stringify(
            "fixed inset-0 flex items-center justify-center z-50",
            "transition-opacity duration-200",
            modal_class,
        )

        # Modal content container
        modal_content_classes = stringify(
            "rounded-lg shadow-xl",
            "max-w-lg w-full mx-4 p-6",
        )

        return Div(
            # Button
            Button(
                self.button_text,
                class_=stringify(styles.buttons.ghost, button_class),
                **Alpine.at.click("feedbackModal = true; feedbackRoute = window.location.pathname"),
            ),
            # Modal
            Div(
                Div(
                    Form(
                        H3(
                            title,
                            class_=title_class,
                        ),
                        Textarea(
                            placeholder=placeholder,
                            name="text",
                            rows=5,
                            required=True,
                        ),
                        Input(
                            type="hidden",
                            name="route",
                            **Alpine.x.model("feedbackRoute"),
                        ),
                        Div(id="feedback-result", class_="mb-4"),
                        Div(
                            Button(
                                submit_text,
                                type="submit",
                                class_=styles.buttons.primary,
                            ),
                            Button(
                                cancel_text,
                                type="button",
                                class_=styles.buttons.secondary,
                                # Close modal and reset form on cancel
                                **Alpine.at.click(
                                    "feedbackModal = false; $el.closest('form').reset(); "
                                    "document.querySelector('#feedback-result').innerHTML = ''"
                                ),
                            ),
                            class_="flex justify-end gap-2",
                        ),
                        hx_post=self.route_path,
                        hx_target="#feedback-result",
                        hx_swap="innerHTML",
                        # Reset form and close modal after htmx request
                        **{
                            "@htmx:after-request": (
                                "setTimeout(() => { "
                                "feedbackModal = false; "
                                "$el.reset(); "
                                "document.querySelector('#feedback-result').innerHTML = ''; "
                                "}, 800)"
                            )
                        },
                    ),
                    class_=modal_content_classes,
                    style="background-color: var(--color-surface-elevated); border: 1px solid var(--color-border)",
                    **Alpine.at.click.stop(""),  # Prevent click from bubbling to backdrop
                ),
                class_=modal_backdrop_classes,
                style="background-color: rgba(0, 0, 0, 0.5)",
                # Close modal on backdrop click
                **(Alpine.at.click("feedbackModal = false") | Alpine.x.show("feedbackModal")),
            ),
            # Alpine.js data scope
            **alpine_data,
        )
