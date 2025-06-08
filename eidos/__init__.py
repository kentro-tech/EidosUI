"""
EidosUI - A modern, flexible Tailwind CSS-based UI library for Python web frameworks

Key Features:
- CSS variable-based theming (light/dark) 
- Class-based components for maximum flexibility
- Mobile-first responsive design patterns
- Comprehensive style dataclasses with sensible defaults
- Built on fastapi-tags for modern Python web development
"""

from .core import (
    ThemeManager,
    theme_manager,
    button_styles,
    typography_styles,
    form_styles,
    merge_classes,
    serve_eidos_static,
    create_eidos_head_tag,
)

from .components import (
    # Typography
    H1, H2, H3, H4, H5, H6,
    P, Text, Em, Strong, A, Code, Pre, Mark, Small,
    
    # Forms
    Button, Input, Textarea, Select, Label, FormGroup,
)

# Version info
__version__ = "0.1.0"
__author__ = "Isaac Flath"

__all__ = [
    # Core
    "ThemeManager",
    "theme_manager",
    "button_styles", 
    "typography_styles",
    "form_styles",
    "merge_classes",
    "serve_eidos_static",
    "create_eidos_head_tag",
    
    # Typography components
    "H1", "H2", "H3", "H4", "H5", "H6",
    "P", "Text", "Em", "Strong", "A", "Code", "Pre", "Blockquote", "Mark", "Small",
    
    # Form components
    "Button", "Input", "Textarea", "Select", "Label", "FormGroup",
    
    # Metadata
    "__version__",
    "__author__",
] 