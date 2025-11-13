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
        "eidos-theme-switch p-2 rounded-full cursor-pointer transition-colors",
        "hover:bg-gray-200 dark:hover:bg-gray-700",
        class_,
    )

    initial_content = light_icon if variant == "icon" else "Theme"

    return Button(
        initial_content,
        class_=button_class,
        type="button",
        aria_label="Toggle theme",
        data_light_icon=light_icon,
        data_dark_icon=dark_icon,
        data_variant=variant,
        **props,
    )
