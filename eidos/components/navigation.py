from air import Div, A, I, Tag
from ..tags import *
from ..utils import stringify
from typing import Final
from uuid import uuid4

class ScrollspyT:
    underline: Final[str] = 'navbar-underline'
    bold: Final[str] = 'navbar-bold'

def NavBar(*c,
           lcontents=H3("Title"),
           right_cls='items-center space-x-4',
           mobile_cls='space-y-4',
           sticky: bool = False,
           scrollspy: bool = False,
           cls='p-4',
           scrollspy_cls=ScrollspyT.underline,
           menu_id=None,
           ) -> Tag:
    """Pure Tailwind responsive navigation bar with optional scrollspy."""
    if menu_id is None: menu_id = f"menu-{uuid4().hex[:8]}"
    
    sticky_cls = 'sticky top-0 bg-base-100/80 backdrop-blur-sm z-50' if sticky else ''
    
    # Mobile toggle button with data attribute for JS
    mobile_icon = A(
        I(data_lucide="menu", class_="w-6 h-6"),
        class_="md:hidden cursor-pointer p-2 hover:bg-base-200 rounded-lg transition-colors",
        data_toggle=f"#{menu_id}",
        role="button",
        aria_label="Toggle navigation"
    )
    
    # Desktop navigation
    desktop_nav = Div(
        *c,
        class_=stringify(right_cls, 'hidden md:flex'),
        data_scrollspy="true" if scrollspy else None
    )
    
    # Mobile navigation
    mobile_nav = Div(
        *c,
        class_=stringify(mobile_cls, 'hidden md:hidden flex flex-col', scrollspy_cls),
        id=menu_id,
        data_scrollspy="true" if scrollspy else None
    )
    
    return Div(
        # Main navbar container
        Div(
            Div(
                lcontents,
                mobile_icon,
                desktop_nav,
                class_='flex items-center justify-between'
            ),
            class_=stringify('eidos-navbar', cls, scrollspy_cls)
        ),
        mobile_nav,
        class_=sticky_cls
    )