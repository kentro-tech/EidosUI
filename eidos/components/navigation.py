from typing import Any, Final
from uuid import uuid4

from air import A, Div, I, Tag

from ..tags import *
from ..utils import stringify


class ScrollspyT:
    underline: Final[str] = "navbar-underline"
    bold: Final[str] = "navbar-bold"


def NavBar(
    *c: Any,
    lcontents: Tag | None = None,
    right_cls: str = "items-center space-x-4",
    mobile_cls: str = "",
    sticky: bool = False,
    scrollspy: bool = False,
    cls: str = "p-4",
    scrollspy_cls: str = ScrollspyT.underline,
    menu_id: str | None = None,
) -> Tag:
    """Pure Tailwind responsive navigation bar with optional scrollspy.

    Mobile menu uses best practice dropdown with:
    - Centered text links
    - Large touch targets
    - Auto-close on selection
    - Smooth animations
    """
    if lcontents is None:
        lcontents = Div()

    if menu_id is None:
        menu_id = f"menu-{uuid4().hex[:8]}"

    sticky_cls = "sticky top-0 eidos-navbar-sticky z-50" if sticky else ""

    # Mobile toggle button with hamburger/close icon
    mobile_icon = A(
        I(data_lucide="menu", class_="w-6 h-6", x_show="!open"),
        I(data_lucide="x", class_="w-6 h-6", x_show="open", x_cloak=True),
        class_="md:hidden cursor-pointer p-2 eidos-navbar-toggle rounded-lg transition-colors",
        role="button",
        aria_label="Toggle navigation",
        x_on_click="open = !open",
        **{":aria-expanded": "open"},
    )

    # Desktop navigation
    desktop_nav = Div(
        *c,
        class_=stringify(right_cls, "hidden md:flex"),
        data_scrollspy="true" if scrollspy else None,
    )

    # Mobile navigation
    mobile_nav = Div(
        *c,
        class_=stringify(
            mobile_cls,
            "md:hidden absolute top-full left-0 right-0 eidos-navbar-mobile shadow-lg border-t",
            "flex flex-col eidos-navbar-mobile-divider" if not mobile_cls else "",
            scrollspy_cls,
        ),
        id=menu_id,
        data_scrollspy="true" if scrollspy else None,
        x_show="open",
        x_cloak=True,
        x_on_click_away="open = false",
    )

    return Div(
        # Main navbar container with relative positioning for mobile dropdown
        Div(
            Div(
                lcontents,
                mobile_icon,
                desktop_nav,
                class_="flex items-center justify-between",
            ),
            mobile_nav,
            class_=stringify("eidos-navbar relative", cls, scrollspy_cls),
            x_data="{ open: false }",
        ),
        class_=sticky_cls,
    )
