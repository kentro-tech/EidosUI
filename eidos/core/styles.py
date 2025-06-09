"""Style dataclasses for EidosUI components using CSS classes"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ButtonStyles:
    """Button style variations using CSS classes"""
    
    # Primary styles (most commonly used)
    primary: str = "eidos-btn-primary"
    secondary: str = "eidos-btn-secondary"
    ghost: str = "eidos-btn-ghost"
    
    # Semantic styles
    success: str = "eidos-btn-success"
    cta: str = "eidos-btn-cta"
    warning: str = "eidos-btn-warning"
    error: str = "eidos-btn-error"
    info: str = "eidos-btn-info"
    
    # Size variations
    sm: str = "eidos-btn-sm"
    md: str = "eidos-btn-md"  # Default size
    lg: str = "eidos-btn-lg"
    xl: str = "eidos-btn-xl"
    
    # Icon styles
    icon_sm: str = "eidos-btn-icon-sm"
    icon_md: str = "eidos-btn-icon-md"
    icon_lg: str = "eidos-btn-icon-lg"
    
    # Special styles
    outline_primary: str = "eidos-btn-outline-primary"
    outline_secondary: str = "eidos-btn-outline-secondary"
    link: str = "eidos-btn-link"


@dataclass(frozen=True) 
class TypographyStyles:
    """Typography style variations using CSS classes"""
    
    # Heading styles (mobile-first responsive)
    h1: str = "eidos-h1"
    h2: str = "eidos-h2"
    h3: str = "eidos-h3"
    h4: str = "eidos-h4"
    h5: str = "eidos-h5"
    h6: str = "eidos-h6"
    
    # Body text styles
    body: str = "eidos-body"
    
    # Semantic emphasis
    em: str = "eidos-em"
    strong: str = "eidos-strong"
    small: str = "eidos-small"
    
    # Links
    link: str = "eidos-link"
    
    # Text decorations
    code: str = "eidos-code"
    pre: str = "eidos-pre"
    mark: str = "eidos-mark"
    blockquote: str = "eidos-blockquote"


@dataclass(frozen=True)
class FormStyles:
    """Form component styles using CSS classes"""
    
    # Input styles
    input: str = "eidos-input"
    
    # Textarea
    textarea: str = "eidos-textarea"
    
    # Select
    select: str = "eidos-select"
    
    # Labels
    label: str = "eidos-label"
    
    # Form groups
    form_group: str = "eidos-form-group"


# Global style instances for easy access
button_styles = ButtonStyles()
typography_styles = TypographyStyles()
form_styles = FormStyles() 