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
           mobile_cls='',
           sticky: bool = False,
           scrollspy: bool = False,
           cls='p-4',
           scrollspy_cls=ScrollspyT.underline,
           menu_id=None,
           ) -> Tag:
    """Pure Tailwind responsive navigation bar with optional scrollspy.
    
    Mobile menu uses best practice dropdown with:
    - Centered text links
    - Large touch targets
    - Auto-close on selection
    - Smooth animations
    """
    if menu_id is None: menu_id = f"menu-{uuid4().hex[:8]}"
    
    sticky_cls = 'sticky top-0 bg-base-100 shadow-sm z-50' if sticky else ''
    
    # Mobile toggle button with hamburger/close icon
    mobile_icon = A(
        I(data_lucide="menu", class_="w-6 h-6", data_menu_icon="open"),
        I(data_lucide="x", class_="w-6 h-6 hidden", data_menu_icon="close"),
        class_="md:hidden cursor-pointer p-2 hover:bg-base-200 rounded-lg transition-colors",
        data_toggle=f"#{menu_id}",
        role="button",
        aria_label="Toggle navigation",
        aria_expanded="false"
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
        class_=stringify(
            mobile_cls, 
            'hidden md:hidden absolute top-full left-0 right-0 bg-white dark:bg-gray-900 shadow-lg border-t border-base-200',
            'flex flex-col divide-y divide-base-200' if not mobile_cls else '',
            scrollspy_cls
        ),
        id=menu_id,
        data_scrollspy="true" if scrollspy else None,
        data_mobile_menu="true"
    )
    
    return Div(
        # Main navbar container with relative positioning for mobile dropdown
        Div(
            Div(
                lcontents,
                mobile_icon,
                desktop_nav,
                class_='flex items-center justify-between'
            ),
            mobile_nav,
            class_=stringify('eidos-navbar relative', cls, scrollspy_cls)
        ),
        class_=sticky_cls
    )