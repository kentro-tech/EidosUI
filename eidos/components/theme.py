"""Theme switching component for EidosUI"""

from typing import Literal

from air import Button

from ..utils import stringify


def ThemeSwitch(
    light_icon: str = "☀️",
    dark_icon: str = "🌙",
    class_: str = "",
    variant: Literal["icon", "text"] = "icon",
    **props,
):
    """Theme switcher button that toggles between light and dark themes.

    Works automatically when EidosHeaders(include_theme_switcher=True) is used.

    Features:
    - Respects system color scheme preference as default
    - Persists user's choice in localStorage
    - Updates the data-theme attribute on document root
    - Changes button icon/text based on current theme

    Args:
        light_icon: Icon/text shown in light mode (default: ☀️)
        dark_icon: Icon/text shown in dark mode (default: 🌙)
        class_: Additional CSS classes
        variant: Display variant - "icon" for just icons, "text" for labels
        **props: Additional button props

    Example:
        ```python
        from eidos import EidosHeaders, ThemeSwitch

        Head(*EidosHeaders())  # Includes theme switcher by default
        Body(
            NavBar(ThemeSwitch())  # Simple icon toggle
        )

        # With custom styling
        ThemeSwitch(class_="p-3 rounded-lg")

        # Text variant
        ThemeSwitch(variant="text")
        ```
    """
    button_class = stringify(
        "p-2 rounded-full cursor-pointer transition-colors",
        "hover:bg-gray-200 dark:hover:bg-gray-700",
        class_,
    )

    if variant == "icon":
        x_text_expr = f"$store.theme.getIcon('{light_icon}', '{dark_icon}')"
    else:
        x_text_expr = "$store.theme.getText()"

    return Button(
        f"{dark_icon}" if variant == "icon" else "Dark Mode",
        class_=button_class,
        type="button",
        x_text=x_text_expr,
        **{
            "@click": "$store.theme.toggle()",
            ":aria-label": "$store.theme.getLabel()",
            **props,
        },
    )
