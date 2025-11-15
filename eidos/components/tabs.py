from typing import Any, Literal

from air import Button, Div, Tag
from airpine import Alpine

from .. import styles
from ..utils import stringify


def AlpineTabs(
    *tabs: tuple[str, Tag],
    selected: int = 0,
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Alpine.js-based tabs with client-side switching.

    Args:
        *tabs: Variable number of (label, content) tuples
        selected: Index of the initially selected tab (0-based)
        class_: Additional classes for the container

    Returns:
        Tag: Complete tabs component with Alpine.js interactivity

    Example:
        AlpineTabs(
            ("General", Div(P("General settings content"))),
            ("Security", Div(P("Security settings content"))),
            ("Advanced", Div(P("Advanced settings content"))),
            selected=0
        )
    """
    tab_buttons = []
    tab_panels = []

    for i, (label, content) in enumerate(tabs):
        tab_button = Button(
            label,
            role="tab",
            class_=stringify(styles.tabs.tab, class_),
            **(
                Alpine.at.click(f"activeTab = {i}")
                | Alpine.x.bind.aria_selected(f"activeTab === {i}")
                | Alpine.x.bind.class_(f"{{'{ styles.tabs.tab_active}': activeTab === {i}}}")
            ),
        )
        tab_buttons.append(tab_button)

        tab_panel = Div(
            content,
            role="tabpanel",
            class_=stringify(styles.tabs.panel, styles.tabs.panel_active),
            **Alpine.x.show(f"activeTab === {i}"),
        )
        tab_panels.append(tab_panel)

    return Div(
        Div(
            *tab_buttons,
            role="tablist",
            class_=styles.tabs.list,
        ),
        *tab_panels,
        class_=stringify(styles.tabs.container, class_),
        **Alpine.x.data({"activeTab": selected}),
        **kwargs,
    )



def HTMXTabs(
    *tabs: tuple[str, str, Tag | None] | tuple[str, str],
    selected: int = 0,
    class_: str = "",
    panel_id: str = "tab-content",
    **kwargs: Any,
) -> Tag:
    """HTMX-based tabs with server-side content switching.

    Args:
        *tabs: Variable number of (label, url) or (label, url, content) tuples
        selected: Index of the initially selected tab (0-based)
        class_: Additional classes for the container
        panel_id: ID for the tab content panel (default: "tab-content")

    Returns:
        Tag: Complete tabs component with HTMX interactivity

    Example:
        HTMXTabs(
            ("General", "/settings/general", Div(P("General settings"))),
            ("Security", "/settings/security"),
            ("Advanced", "/settings/advanced"),
            selected=0
        )
    """
    tab_buttons = []
    initial_content = None

    for i, tab in enumerate(tabs):
        label, url = tab[0], tab[1]
        content = tab[2] if len(tab) > 2 else None
        is_selected = i == selected

        if is_selected and content:
            initial_content = content

        tab_button = Button(
            label,
            hx_get=url,
            hx_target=f"#{panel_id}",
            hx_swap="innerHTML",
            role="tab",
            aria_selected="true" if is_selected else "false",
            aria_controls=panel_id,
            class_=stringify(styles.tabs.tab, styles.tabs.tab_active if is_selected else "", class_),
        )
        tab_buttons.append(tab_button)

    tab_list = Div(
        *tab_buttons,
        role="tablist",
        class_=styles.tabs.list,
    )

    tab_panel = Div(
        initial_content if initial_content else "",
        id=panel_id,
        role="tabpanel",
        class_=stringify(styles.tabs.panel, styles.tabs.panel_active),
        hx_get=tabs[selected][1] if not initial_content else None,
        hx_trigger="load delay:100ms" if not initial_content else None,
        hx_swap="innerHTML" if not initial_content else None,
    )

    return Div(
        tab_list,
        tab_panel,
        class_=stringify(styles.tabs.container, class_),
        **kwargs,
    )

