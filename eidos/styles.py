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

# Create singleton instance for easy access
buttons = Buttons()
typography = Typography()