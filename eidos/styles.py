"""CSS class constants for EidosUI components.

This module provides Python constants for CSS classes that exist in styles.css.
Only includes classes that are actually defined in the CSS file.
"""

from typing import Final


class Theme:
    """Theme-related CSS classes from styles.css."""

    body: Final[str] = "eidos-body"


class Buttons:
    """Button-related CSS classes from styles.css."""

    # Base button class (required for all buttons)
    base: Final[str] = "eidos-btn"

    # Button variants
    primary: Final[str] = "eidos-btn-primary"
    secondary: Final[str] = "eidos-btn-secondary"
    ghost: Final[str] = "eidos-btn-ghost"
    outline: Final[str] = "eidos-btn-outline"
    success: Final[str] = "eidos-btn-success"
    error: Final[str] = "eidos-btn-error"
    cta: Final[str] = "eidos-btn-cta"


class Typography:
    """Typography-related CSS classes from styles.css."""

    h1: Final[str] = "eidos-h1"
    h2: Final[str] = "eidos-h2"
    h3: Final[str] = "eidos-h3"
    h4: Final[str] = "eidos-h4"
    h5: Final[str] = "eidos-h5"
    h6: Final[str] = "eidos-h6"


class Semantic:
    """Semantic HTML element CSS classes from styles.css."""

    # Text formatting
    strong: Final[str] = "eidos-strong"
    i: Final[str] = "eidos-i"
    small: Final[str] = "eidos-small"
    del_: Final[str] = "eidos-del"  # del is reserved keyword
    abbr: Final[str] = "eidos-abbr"
    var: Final[str] = "eidos-var"
    mark: Final[str] = "eidos-mark"
    time: Final[str] = "eidos-time"

    # Code elements
    code: Final[str] = "eidos-code"
    pre: Final[str] = "eidos-pre"
    kbd: Final[str] = "eidos-kbd"
    samp: Final[str] = "eidos-samp"

    # Structural elements
    blockquote: Final[str] = "eidos-blockquote"
    cite: Final[str] = "eidos-cite"
    address: Final[str] = "eidos-address"
    hr: Final[str] = "eidos-hr"

    # Interactive elements
    details: Final[str] = "eidos-details"
    summary: Final[str] = "eidos-summary"
    details_content: Final[str] = "eidos-details-content"

    # Definition list
    dl: Final[str] = "eidos-dl"
    dt: Final[str] = "eidos-dt"
    dd: Final[str] = "eidos-dd"

    # Figure
    figure: Final[str] = "eidos-figure"
    figcaption: Final[str] = "eidos-figcaption"


class Tables:
    """Table-related CSS classes from styles.css."""

    # Base table class
    table: Final[str] = "eidos-table"

    # Table sections
    thead: Final[str] = "eidos-thead"
    tbody: Final[str] = "eidos-tbody"
    tfoot: Final[str] = "eidos-tfoot"

    # Table elements
    tr: Final[str] = "eidos-tr"
    th: Final[str] = "eidos-th"
    td: Final[str] = "eidos-td"


# Create singleton instance for easy access
buttons = Buttons()
typography = Typography()
semantic = Semantic()
tables = Tables()
