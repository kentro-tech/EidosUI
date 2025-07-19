from typing import Any, Literal

from air import Button, Div, Tag

from .. import styles
from ..utils import stringify


def TabContainer(
    *content: Tag,
    initial_tab_url: str,
    class_: str = "",
    target_id: str = "tabs",
    **kwargs: Any,
) -> Tag:
    """HTMX-based tab container that loads tabs dynamically.

    Args:
        initial_tab_url: URL to load the initial tab content
        cls: Additional classes for the container
        target_id: ID for the tab container (default: "tabs")

    Returns:
        Tag: The tab container that will be populated via HTMX

    Example:
        TabContainer("/settings/general")
    """
    return Div(
        *content,
        id=target_id,
        hx_get=initial_tab_url,
        hx_trigger="load delay:100ms",
        hx_target=f"#{target_id}",
        hx_swap="innerHTML",
        class_=stringify(styles.tabs.container, class_),
        **kwargs,
    )


def TabList(
    *tabs: tuple[str, str],
    selected: int = 0,
    class_: str = "",
    hx_target: str = "#tabs",
    hx_swap: Literal[
        "innerHTML", "outerHTML", "beforebegin", "afterbegin", "beforeend", "afterend", "delete", "none"
    ] = "innerHTML",
    **kwargs: Any,
) -> Tag:
    """HTMX-based tab list for server-rendered tabs.

    Args:
        *tabs: Variable number of (label, url) tuples
        selected: Index of the selected tab (0-based)
        tab_cls: Additional classes for tab buttons
        hx_target: HTMX target for tab content (default: "#tabs")
        hx_swap: HTMX swap method (default: "innerHTML")

    Returns:
        Tag: The tab list component

    Example:
        TabList(
            ("General", "/settings/general"),
            ("Security", "/settings/security"),
            ("Advanced", "/settings/advanced"),
            selected=0
        )
    """
    tab_buttons = []

    for i, (label, url) in enumerate(tabs):
        is_selected = i == selected

        tab_button = Button(
            label,
            hx_get=url,
            hx_target=hx_target,
            hx_swap=hx_swap,
            role="tab",
            aria_selected="true" if is_selected else "false",
            aria_controls="tab-content",
            class_=stringify(styles.tabs.tab, styles.tabs.tab_active if is_selected else "", class_),
        )
        tab_buttons.append(tab_button)

    return Div(
        *tab_buttons,
        role="tablist",
        class_=styles.tabs.list,
        **kwargs,
    )


def TabPanel(
    content: Tag,
    class_: str = "",
    **kwargs: Any,
) -> Tag:
    """Tab panel content wrapper.

    Args:
        content: The content to display in the tab panel
        panel_cls: Additional classes for the panel

    Returns:
        Tag: The tab panel component
    """
    return Div(
        content,
        id="tab-content",
        role="tabpanel",
        class_=stringify(styles.tabs.panel, styles.tabs.panel_active, class_),
        **kwargs,
    )


def Tabs(
    tab_list: Tag,
    tab_panel: Tag,
    cls: str = "",
    **kwargs: Any,
) -> Tag:
    """Complete tab component with list and panel.

    Args:
        tab_list: The TabList component
        tab_panel: The TabPanel component
        cls: Additional classes for the container

    Returns:
        Tag: The complete tabs component

    Example:
        # In your route handler:
        tab_list = TabList(
            ("General", "/settings/general"),
            ("Security", "/settings/security"),
            selected=0
        )
        tab_panel = TabPanel(general_settings_content)
        return Tabs(tab_list, tab_panel)
    """
    return Div(
        tab_list,
        tab_panel,
        class_=stringify(styles.tabs.container, cls),
        **kwargs,
    )
