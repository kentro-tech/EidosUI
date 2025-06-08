# EidosUI Development Plan

## Project Overview
EidosUI is a modern, Tailwind CSS-based UI library for Python web frameworks, designed to work seamlessly with the fastapi-tag-exploration pattern. It provides a clean, theme-aware component system with excellent developer experience.

## Core Design Principles
1. **Tailwind-First**: All styles use Tailwind CSS classes, compatible with CDN
2. **Theme-Aware**: Built-in light/dark themes with easy customization.  These themes should be defined in the exact way a user could define their own custom theme.
3. **Type-Safe**: Leverages Python dataclasses and enums for better DX
4. **Modular**: Components are self-contained and composable
5. **Modern Aesthetic**: Clean, minimal design with excellent UX patterns
6. **FastApi Compatible**: Works seamlessly with fastapi-tag-exploration patterns

## Project Structure

```
EidosUI/
├── README.md
├── pyproject.toml
├── eidos/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── themes.py          # Python theme interface and utilities
│   │   ├── styles.py          # Style dataclasses using CSS variables
│   │   └── utils.py           # Helper functions for class manipulation
│   ├── themes/
│   │   ├── light.css          # Light theme CSS variables
│   │   ├── dark.css           # Dark theme CSS variables
│   │   └── custom.css.example # Example custom theme
│   ├── components/
│   │   ├── __init__.py
│   │   ├── base.py            # Base component utilities
│   │   ├── typography.py      # Text, headings, etc.
│   │   ├── layout.py          # Containers, grids, flex utilities
│   │   ├── forms.py           # Inputs, buttons, form controls
│   │   ├── navigation.py      # Nav, breadcrumbs, pagination
│   │   ├── feedback.py        # Alerts, toasts, modals
│   │   ├── display.py         # Cards, tables, lists
│   │   └── media.py           # Images, avatars, icons
│   ├── templates/
│   │   ├── __init__.py
│   │   ├── pages.py           # Full page layouts with theme support
│   │   └── sections.py        # Reusable page sections
│   └── static/
│       └── eidos-ui.js        # Client-side theme switching utilities
├── examples/
│   ├── basic_usage.py
│   ├── custom_theme.py
│   └── full_app.py
└── tests/
    ├── test_themes.py
    ├── test_components.py
    └── test_integration.py
```

## Theme System Architecture

### CSS Variable-Based Theme Definition
```css
/* eidos/themes/light.css */
:root {
  /* Core Colors */
  --color-primary: #2563eb;
  --color-primary-hover: #1d4ed8;
  --color-primary-light: #eff6ff;
  --color-primary-dark: #1e3a8a;
  --color-primary-foreground: #ffffff;
  
  --color-secondary: #64748b;
  --color-secondary-hover: #475569;
  --color-secondary-light: #f8fafc;
  --color-secondary-dark: #334155;
  --color-secondary-foreground: #ffffff;
  
  --color-accent: #7c3aed;
  --color-accent-hover: #6d28d9;
  --color-accent-light: #f3e8ff;
  --color-accent-foreground: #ffffff;
  
  /* Semantic Colors */
  --color-success: #16a34a;
  --color-success-hover: #15803d;
  --color-success-light: #f0fdf4;
  --color-success-foreground: #ffffff;
  
  --color-warning: #eab308;
  --color-warning-hover: #ca8a04;
  --color-warning-light: #fefce8;
  --color-warning-foreground: #000000;
  
  --color-error: #dc2626;
  --color-error-hover: #b91c1c;
  --color-error-light: #fef2f2;
  --color-error-foreground: #ffffff;
  
  --color-info: #0ea5e9;
  --color-info-hover: #0284c7;
  --color-info-light: #f0f9ff;
  --color-info-foreground: #ffffff;
  
  /* Surface Colors */
  --color-background: #ffffff;
  --color-surface: #f8fafc;
  --color-surface-elevated: #ffffff;
  --color-border: #e2e8f0;
  --color-border-hover: #cbd5e1;
  --color-input: #ffffff;
  --color-card: #ffffff;
  
  /* Text Colors */
  --color-text: #0f172a;
  --color-text-muted: #64748b;
  --color-text-subtle: #94a3b8;
  --color-text-inverse: #ffffff;
  
  /* Spacing Scale */
  --space-xs: 0.25rem;   /* 4px */
  --space-sm: 0.5rem;    /* 8px */
  --space-md: 1rem;      /* 16px */
  --space-lg: 1.5rem;    /* 24px */
  --space-xl: 2rem;      /* 32px */
  --space-2xl: 3rem;     /* 48px */
  --space-3xl: 4rem;     /* 64px */
  
  /* Typography Scale */
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;
  
  /* Border Radius */
  --radius-none: 0;
  --radius-sm: 0.125rem;   /* 2px */
  --radius-base: 0.375rem; /* 6px */
  --radius-md: 0.5rem;     /* 8px */
  --radius-lg: 0.75rem;    /* 12px */
  --radius-xl: 1rem;       /* 16px */
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-base: 0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1);
  --shadow-xl: 0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1);
  
  /* Animation */
  --transition-fast: 150ms ease;
  --transition-base: 200ms ease;
  --transition-slow: 300ms ease;
}

/* Dark theme */
[data-theme="dark"] {
  --color-background: #0f172a;
  --color-surface: #1e293b;
  --color-surface-elevated: #334155;
  --color-border: #334155;
  --color-border-hover: #475569;
  --color-input: #1e293b;
  --color-card: #1e293b;
  
  --color-text: #f8fafc;
  --color-text-muted: #94a3b8;
  --color-text-subtle: #64748b;
  --color-text-inverse: #0f172a;
  
  --color-primary-light: #1e3a8a;
  --color-secondary-light: #334155;
  --color-accent-light: #581c87;
  --color-success-light: #14532d;
  --color-warning-light: #713f12;
  --color-error-light: #7f1d1d;
  --color-info-light: #0c4a6e;
}
```

### Python Theme Interface
```python
# eidos/core/themes.py
from typing import Dict, Any
import os

class ThemeManager:
    """Manages CSS variable-based themes with Python interface for DX"""
    
    def __init__(self):
        self._current_theme = "light"
        self._css_vars_cache: Dict[str, str] = {}
        
    def get_css_var(self, var_name: str) -> str:
        """Get CSS variable value for Python DX"""
        return f"var(--{var_name})"
    
    def generate_tailwind_config(self) -> Dict[str, Any]:
        """Generate Tailwind config that uses our CSS variables"""
        return {
            "theme": {
                "extend": {
                    "colors": {
                        "primary": {
                            "DEFAULT": "var(--color-primary)",
                            "hover": "var(--color-primary-hover)",
                            "light": "var(--color-primary-light)",
                            "dark": "var(--color-primary-dark)",
                            "foreground": "var(--color-primary-foreground)",
                        },
                        "secondary": {
                            "DEFAULT": "var(--color-secondary)",
                            "hover": "var(--color-secondary-hover)",
                            "light": "var(--color-secondary-light)",
                            "dark": "var(--color-secondary-dark)",
                            "foreground": "var(--color-secondary-foreground)",
                        },
                        "accent": {
                            "DEFAULT": "var(--color-accent)",
                            "hover": "var(--color-accent-hover)",
                            "light": "var(--color-accent-light)",
                            "foreground": "var(--color-accent-foreground)",
                        },
                        "success": {
                            "DEFAULT": "var(--color-success)",
                            "hover": "var(--color-success-hover)",
                            "light": "var(--color-success-light)",
                            "foreground": "var(--color-success-foreground)",
                        },
                        "warning": {
                            "DEFAULT": "var(--color-warning)",
                            "hover": "var(--color-warning-hover)",
                            "light": "var(--color-warning-light)",
                            "foreground": "var(--color-warning-foreground)",
                        },
                        "error": {
                            "DEFAULT": "var(--color-error)",
                            "hover": "var(--color-error-hover)",
                            "light": "var(--color-error-light)",
                            "foreground": "var(--color-error-foreground)",
                        },
                        "info": {
                            "DEFAULT": "var(--color-info)",
                            "hover": "var(--color-info-hover)",
                            "light": "var(--color-info-light)",
                            "foreground": "var(--color-info-foreground)",
                        },
                        "surface": {
                            "DEFAULT": "var(--color-surface)",
                            "elevated": "var(--color-surface-elevated)",
                        },
                        "border": {
                            "DEFAULT": "var(--color-border)",
                            "hover": "var(--color-border-hover)",
                        },
                    },
                    "spacing": {
                        "xs": "var(--space-xs)",
                        "sm": "var(--space-sm)",
                        "md": "var(--space-md)",
                        "lg": "var(--space-lg)",
                        "xl": "var(--space-xl)",
                        "2xl": "var(--space-2xl)",
                        "3xl": "var(--space-3xl)",
                    },
                    "borderRadius": {
                        "base": "var(--radius-base)",
                        "md": "var(--radius-md)",
                        "lg": "var(--radius-lg)",
                        "xl": "var(--radius-xl)",
                    },
                    "boxShadow": {
                        "sm": "var(--shadow-sm)",
                        "base": "var(--shadow-base)",
                        "md": "var(--shadow-md)",
                        "lg": "var(--shadow-lg)",
                        "xl": "var(--shadow-xl)",
                    },
                    "transitionDuration": {
                        "fast": "150ms",
                        "base": "200ms",
                        "slow": "300ms",
                    }
                }
            }
        }

# Global theme manager instance
theme_manager = ThemeManager()
```

### Theme Switching & Management
```python
# eidos/core/themes.py (continued)

def set_theme(theme_name: str = "light"):
    """Set theme via data attribute on document element"""
    return f'document.documentElement.setAttribute("data-theme", "{theme_name}");'

def get_theme_css_link(theme_name: str = "light") -> str:
    """Get CSS link tag for theme"""
    return f'<link rel="stylesheet" href="/static/themes/{theme_name}.css">'

def theme_switcher_script() -> str:
    """JavaScript for theme switching"""
    return """
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('eidos-theme', theme);
    }
    
    function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme') || 'light';
        const next = current === 'light' ? 'dark' : 'light';
        setTheme(next);
    }
    
    // Initialize theme from localStorage or system preference
    const savedTheme = localStorage.getItem('eidos-theme');
    const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    setTheme(savedTheme || systemTheme);
    """
```

## Style System Architecture

### Component Style Dataclasses
```python
# eidos/core/styles.py
from dataclasses import dataclass

@dataclass(frozen=True)
class ButtonStyles:
    """Button style variations using CSS variables"""
    
    # Primary styles (most commonly used)
    primary: str = "bg-primary hover:bg-primary-hover text-primary-foreground font-medium rounded-lg transition-colors duration-base focus:outline-none focus:ring-2 focus:ring-primary focus:ring-opacity-50"
    secondary: str = "bg-secondary hover:bg-secondary-hover text-secondary-foreground font-medium rounded-lg transition-colors duration-base border border-secondary"
    ghost: str = "text-primary hover:bg-primary-light font-medium rounded-lg transition-colors duration-base"
    
    # Semantic styles
    success: str = "bg-success hover:bg-success-hover text-success-foreground font-medium rounded-lg transition-colors duration-base"
    warning: str = "bg-warning hover:bg-warning-hover text-warning-foreground font-medium rounded-lg transition-colors duration-base"
    error: str = "bg-error hover:bg-error-hover text-error-foreground font-medium rounded-lg transition-colors duration-base"
    info: str = "bg-info hover:bg-info-hover text-info-foreground font-medium rounded-lg transition-colors duration-base"
    
    # Size variations
    sm: str = "px-3 py-1.5 text-sm"
    md: str = "px-4 py-2 text-base"  # Default size
    lg: str = "px-6 py-3 text-lg"
    xl: str = "px-8 py-4 text-xl"
    
    # Icon styles
    icon_sm: str = "p-1.5"
    icon_md: str = "p-2"
    icon_lg: str = "p-3"
    
    # Special styles
    outline_primary: str = "border border-primary text-primary hover:bg-primary hover:text-primary-foreground font-medium rounded-lg transition-colors duration-base"
    outline_secondary: str = "border border-secondary text-secondary hover:bg-secondary hover:text-secondary-foreground font-medium rounded-lg transition-colors duration-base"
    link: str = "text-primary hover:text-primary-hover underline-offset-4 hover:underline font-medium transition-colors duration-base"

@dataclass(frozen=True)
class CardStyles:
    """Card style variations using CSS variables"""
    
    # Primary card styles
    default: str = "bg-card border border-border rounded-lg shadow-sm"
    elevated: str = "bg-card border border-border rounded-lg shadow-md hover:shadow-lg transition-shadow duration-base"
    flat: str = "bg-surface rounded-lg"
    
    # Interactive cards
    interactive: str = "bg-card border border-border rounded-lg shadow-sm hover:shadow-md hover:border-border-hover transition-all duration-base cursor-pointer"
    
    # Padding variations
    compact: str = "p-4"
    comfortable: str = "p-6"  # Default
    spacious: str = "p-8"
    
    # Special variations
    glass: str = "bg-card/80 backdrop-blur-sm border border-border rounded-lg shadow-sm"
    outline: str = "border border-border rounded-lg bg-transparent"

@dataclass(frozen=True) 
class TypographyStyles:
    """Typography style variations using CSS variables"""
    
    # Heading styles (mobile-first responsive)
    h1: str = "text-2xl sm:text-3xl lg:text-4xl font-bold text-text leading-tight"
    h2: str = "text-xl sm:text-2xl lg:text-3xl font-semibold text-text leading-tight"
    h3: str = "text-lg sm:text-xl lg:text-2xl font-semibold text-text leading-tight"
    h4: str = "text-base sm:text-lg lg:text-xl font-semibold text-text leading-tight"
    h5: str = "text-sm sm:text-base lg:text-lg font-medium text-text leading-tight"
    h6: str = "text-xs sm:text-sm lg:text-base font-medium text-text leading-tight"
    
    # Body text styles
    body: str = "text-base text-text leading-relaxed"
    body_sm: str = "text-sm text-text leading-relaxed"
    body_lg: str = "text-lg text-text leading-relaxed"
    
    # Utility text styles
    muted: str = "text-text-muted"
    subtle: str = "text-text-subtle"
    inverse: str = "text-text-inverse"
    
    # Semantic text styles
    success: str = "text-success"
    warning: str = "text-warning"
    error: str = "text-error"
    info: str = "text-info"
    
    # Text decorations
    code: str = "font-mono bg-surface px-1.5 py-0.5 rounded text-sm"
    kbd: str = "font-mono bg-surface border border-border px-1.5 py-0.5 rounded text-sm shadow-sm"
    mark: str = "bg-warning-light px-1 rounded"

@dataclass(frozen=True)
class FormStyles:
    """Form component styles using CSS variables"""
    
    # Input styles
    input: str = "w-full px-3 py-2 bg-input border border-border rounded-lg text-text placeholder:text-text-muted focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-colors duration-base"
    input_sm: str = "px-2.5 py-1.5 text-sm"
    input_lg: str = "px-4 py-3 text-lg"
    
    # Input states
    input_error: str = "border-error focus:ring-error"
    input_success: str = "border-success focus:ring-success"
    input_disabled: str = "bg-surface opacity-60 cursor-not-allowed"
    
    # Textarea
    textarea: str = "w-full px-3 py-2 bg-input border border-border rounded-lg text-text placeholder:text-text-muted focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-colors duration-base resize-y min-h-[80px]"
    
    # Select
    select: str = "w-full px-3 py-2 bg-input border border-border rounded-lg text-text focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent transition-colors duration-base appearance-none"
    
    # Checkbox & Radio
    checkbox: str = "w-4 h-4 border border-border rounded text-primary focus:ring-primary focus:ring-2 bg-input"
    radio: str = "w-4 h-4 border border-border text-primary focus:ring-primary focus:ring-2 bg-input"
    
    # Labels
    label: str = "block text-sm font-medium text-text mb-1"
    label_optional: str = "block text-sm font-medium text-text-muted mb-1"
    
    # Form groups
    form_group: str = "space-y-2"
    form_row: str = "grid grid-cols-1 sm:grid-cols-2 gap-4"

@dataclass(frozen=True)
class LayoutStyles:
    """Layout component styles using CSS variables"""
    
    # Container styles (mobile-first responsive)
    container: str = "mx-auto px-4 sm:px-6 lg:px-8"
    container_sm: str = "max-w-2xl"
    container_md: str = "max-w-4xl"  
    container_lg: str = "max-w-6xl"  # Default
    container_xl: str = "max-w-7xl"
    container_full: str = "max-w-full"
    
    # Grid styles  
    grid: str = "grid gap-4"
    grid_responsive: str = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4"
    grid_auto_fit: str = "grid grid-cols-[repeat(auto-fit,minmax(280px,1fr))] gap-4"
    
    # Flex utilities
    flex_center: str = "flex items-center justify-center"
    flex_between: str = "flex items-center justify-between"
    flex_col: str = "flex flex-col"
    flex_wrap: str = "flex flex-wrap"
    
    # Stack (vertical spacing)
    stack_sm: str = "space-y-2"
    stack_md: str = "space-y-4"  # Default
    stack_lg: str = "space-y-6"
    stack_xl: str = "space-y-8"
    
    # Page layouts
    page: str = "min-h-screen bg-background text-text"
    main: str = "flex-1"
    sidebar: str = "w-64 bg-surface border-r border-border"
    header: str = "sticky top-0 z-40 bg-background/80 backdrop-blur-sm border-b border-border"
    footer: str = "border-t border-border bg-surface"

@dataclass(frozen=True)
class NavigationStyles:
    """Navigation component styles"""
    
    # Navigation containers
    nav: str = "flex items-center space-x-4"
    nav_vertical: str = "flex flex-col space-y-1"
    
    # Navigation links
    nav_link: str = "text-text-muted hover:text-text transition-colors duration-base"
    nav_link_active: str = "text-primary font-medium"
    
    # Breadcrumbs
    breadcrumb: str = "flex items-center space-x-2 text-sm text-text-muted"
    breadcrumb_separator: str = "text-text-subtle"
    
    # Tabs
    tab_list: str = "flex border-b border-border"
    tab: str = "px-4 py-2 text-text-muted hover:text-text border-b-2 border-transparent hover:border-border transition-colors duration-base"
    tab_active: str = "text-primary border-primary"

# Global style instances for easy access
button_styles = ButtonStyles()
card_styles = CardStyles()
typography_styles = TypographyStyles()
form_styles = FormStyles()
layout_styles = LayoutStyles()
navigation_styles = NavigationStyles()
```

## Component System Architecture

### Base Component Infrastructure
```python
# eidos/components/base.py
from typing import Union, Tuple, Any
import fastapi_tags as ft
from ..core.themes import get_current_theme

def merge_classes(*classes: Union[str, Tuple[str, ...], None]) -> str:
    """Merge multiple class strings, handling None values"""
    result = []
    for cls in classes:
        if cls is None:
            continue
        if isinstance(cls, (tuple, list)):
            result.extend(str(c) for c in cls if c)
        else:
            result.append(str(cls))
    return ' '.join(filter(None, result))

class ComponentBase:
    """Base class for all EidosUI components"""
    
    def __init__(self):
        self.theme = get_current_theme()
    
    def _apply_theme_classes(self, base_classes: str, theme_variant: str = None) -> str:
        """Apply theme-specific classes to base classes"""
        # Theme application logic
        pass
```

### Typography Components - Class-Based Approach
```python
# eidos/components/typography.py
import fastapi_tags as ft
from .base import merge_classes
from ..core.styles import typography_styles

def H1(*content, cls: str = typography_styles.h1, **kwargs) -> ft.H1:
    """Flexible H1 heading with mobile-first responsive sizing"""
    return ft.H1(*content, cls=cls, **kwargs)

def H2(*content, cls: str = typography_styles.h2, **kwargs) -> ft.H2:
    """Flexible H2 heading with mobile-first responsive sizing"""
    return ft.H2(*content, cls=cls, **kwargs)

def H3(*content, cls: str = typography_styles.h3, **kwargs) -> ft.H3:
    """Flexible H3 heading with mobile-first responsive sizing"""
    return ft.H3(*content, cls=cls, **kwargs)

def H4(*content, cls: str = typography_styles.h4, **kwargs) -> ft.H4:
    """Flexible H4 heading with mobile-first responsive sizing"""
    return ft.H4(*content, cls=cls, **kwargs)

def H5(*content, cls: str = typography_styles.h5, **kwargs) -> ft.H5:
    """Flexible H5 heading with mobile-first responsive sizing"""
    return ft.H5(*content, cls=cls, **kwargs)

def H6(*content, cls: str = typography_styles.h6, **kwargs) -> ft.H6:
    """Flexible H6 heading with mobile-first responsive sizing"""
    return ft.H6(*content, cls=cls, **kwargs)

def Text(*content, cls: str = typography_styles.body, **kwargs) -> ft.P:
    """Flexible text component - defaults to body style"""
    return ft.P(*content, cls=cls, **kwargs)

def Link(*content, cls: str = "text-primary hover:text-primary-hover underline transition-colors duration-base", **kwargs) -> ft.A:
    """Flexible link component"""
    return ft.A(*content, cls=cls, **kwargs)

def Code(*content, cls: str = typography_styles.code, **kwargs) -> ft.Code:
    """Inline code component"""
    return ft.Code(*content, cls=cls, **kwargs)

def Blockquote(*content, cls: str = "border-l-4 border-primary pl-4 italic", **kwargs) -> ft.Blockquote:
    """Blockquote component"""
    return ft.Blockquote(*content, cls=cls, **kwargs)
```

### Component Architecture - Class-Based Approach
```python
# eidos/components/forms.py
import fastapi_tags as ft
from .base import merge_classes
from ..core.styles import button_styles, form_styles

def Button(*content, cls: str = button_styles.primary, size_cls: str = button_styles.md, **kwargs) -> ft.Button:
    """Highly flexible button component that takes classes directly"""
    return ft.Button(
        *content,
        cls=merge_classes(cls, size_cls),
        **kwargs
    )

def Input(cls: str = form_styles.input, size_cls: str = "", state_cls: str = "", **kwargs) -> ft.Input:
    """Flexible input component with class-based styling"""
    return ft.Input(
        cls=merge_classes(cls, size_cls, state_cls),
        **kwargs
    )

def Textarea(cls: str = form_styles.textarea, **kwargs) -> ft.Textarea:
    """Flexible textarea component"""
    return ft.Textarea(
        cls=cls,
        **kwargs
    )

def Select(*options, cls: str = form_styles.select, **kwargs) -> ft.Select:
    """Flexible select component"""
    return ft.Select(
        *options,
        cls=cls,
        **kwargs
    )

def Label(text: str, cls: str = form_styles.label, **kwargs) -> ft.Label:
    """Flexible label component"""
    return ft.Label(
        text,
        cls=cls,
        **kwargs
    )

def FormGroup(*content, cls: str = form_styles.form_group, **kwargs) -> ft.Div:
    """Form group container with default spacing"""
    return ft.Div(
        *content,
        cls=cls,
        **kwargs
    )
```

### Layout Components - Class-Based Approach  
```python
# eidos/components/layout.py
import fastapi_tags as ft
from .base import merge_classes
from ..core.styles import card_styles, layout_styles

def Container(*content, cls: str = "", size_cls: str = layout_styles.container_lg, **kwargs) -> ft.Div:
    """Flexible container component with size classes"""
    return ft.Div(
        *content,
        cls=merge_classes(layout_styles.container, size_cls, cls),
        **kwargs
    )

def Card(*content, cls: str = card_styles.default, padding_cls: str = card_styles.comfortable, **kwargs) -> ft.Div:
    """Flexible card component with class-based styling"""
    return ft.Div(
        *content,
        cls=merge_classes(cls, padding_cls),
        **kwargs
    )

def Grid(*content, cls: str = layout_styles.grid_responsive, **kwargs) -> ft.Div:
    """Flexible grid component - defaults to responsive grid"""
    return ft.Div(
        *content,
        cls=cls,
        **kwargs
    )

def Stack(*content, cls: str = layout_styles.stack_md, **kwargs) -> ft.Div:
    """Vertical stack component with spacing"""
    return ft.Div(
        *content,
        cls=cls,
        **kwargs
    )

def Flex(*content, cls: str = layout_styles.flex_center, **kwargs) -> ft.Div:
    """Flexible flex container"""
    return ft.Div(
        *content,
        cls=cls,
        **kwargs
    )

def Center(*content, cls: str = "", **kwargs) -> ft.Div:
    """Center content both horizontally and vertically"""
    return ft.Div(
        *content,
        cls=merge_classes(layout_styles.flex_center, "min-h-screen", cls),
        **kwargs
    )

def Spacer(cls: str = "flex-1") -> ft.Div:
    """Flexible spacer component"""
    return ft.Div(cls=cls)
```

## Integration with fastapi-tag-exploration Pattern

### Enhanced Layout Module
```python
# eidos/templates/pages.py
import fastapi_tags as ft
from ..components.layout import Container
from ..components.typography import H1
from ..core.themes import get_current_theme

def page(title: str, *content, theme_name: str = None, cls: str = "", **kwargs) -> ft.Html:
    """Base page layout with theme support"""
    theme = get_current_theme()
    
    return ft.Html(
        ft.Head(
            ft.Title(title),
            ft.Script(src="https://unpkg.com/htmx.org@1.9.10"),
            ft.Script(src="https://cdn.tailwindcss.com"),
            ft.Script(f"""
                // Theme initialization
                if ('{theme.name}' === 'dark') {{
                    document.documentElement.classList.add('dark');
                }}
            """),
            ft.Meta(name="viewport", content="width=device-width, initial-scale=1.0")
        ),
        ft.Body(
            *content,
            cls=merge_classes(f"min-h-screen bg-{theme.colors.background} text-{theme.colors.text}", cls),
            **kwargs
        )
    )

def app_shell(title: str, *content, nav: ft.FT = None, footer: ft.FT = None) -> ft.Html:
    """Complete app shell with navigation and footer"""
    return page(
        title,
        nav if nav else default_nav(),
        ft.Main(
            Container(*content, cls="py-8"),
            cls="flex-1"
        ),
        footer if footer else default_footer(),
        cls="flex flex-col"
    )
```

## Theme Switching Implementation

### Runtime Theme Switching
```python
# eidos/core/utils.py
def generate_theme_css(theme: Theme) -> str:
    """Generate CSS custom properties for a theme"""
    return f"""
    :root {{
        --color-primary: {theme.colors.primary};
        --color-secondary: {theme.colors.secondary};
        --color-background: {theme.colors.background};
        --color-surface: {theme.colors.surface};
        --color-text: {theme.colors.text};
        --color-border: {theme.colors.border};
    }}
    """

def theme_switcher_component() -> ft.Div:
    """Theme switcher toggle component"""
    return ft.Div(
        ft.Button(
            "🌙", 
            id="theme-toggle",
            cls="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors",
            onclick="toggleTheme()"
        ),
        ft.Script("""
            function toggleTheme() {
                const html = document.documentElement;
                const isDark = html.classList.contains('dark');
                
                if (isDark) {
                    html.classList.remove('dark');
                    localStorage.setItem('theme', 'light');
                } else {
                    html.classList.add('dark');
                    localStorage.setItem('theme', 'dark');
                }
            }
            
            // Initialize theme from localStorage
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark' || (!savedTheme && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                document.documentElement.classList.add('dark');
            }
        """)
    )
```

## Component Coverage Plan

### Phase 1: Core Components
- [x] Typography (H1-H6, Text, Link)  
- [x] Layout (Container, Grid, Card, Stack)
- [x] Forms (Button, Input, Textarea, Select, Checkbox, Radio)
- [x] Theme System

### Phase 2: Navigation & Feedback
- [ ] Navigation (Nav, Breadcrumb, Pagination, Tabs)
- [ ] Feedback (Alert, Toast, Modal, Loading)
- [ ] Display (Table, List, Badge, Avatar)

### Phase 3: Advanced Components  
- [ ] Media (Image, Icon, Gallery)
- [ ] Complex Forms (DatePicker, MultiSelect, Upload)
- [ ] Interactive (Dropdown, Tooltip, Popover, Accordion)

### Phase 4: Specialized Components
- [ ] Charts & Data Visualization integration hooks
- [ ] Layout Templates (Dashboard, Landing, Auth)
- [ ] Animation utilities

## Modern Aesthetic Improvements

### Design Principles
1. **Subtle Shadows**: More refined shadow system with multiple layers
2. **Better Spacing**: Consistent spacing scale based on 4px grid
3. **Improved Typography**: Better font weights and line heights
4. **Color Harmony**: Carefully chosen color palettes with proper contrast
5. **Micro-interactions**: Smooth transitions and hover states
6. **Accessibility**: WCAG 2.1 AA compliance built-in

### Key Visual Differences from MonsterUI/Franken
- More generous white space and padding
- Subtle gradients and glass-morphism effects
- Better focus states with rings instead of borders
- Consistent border radius (rounded-lg as default)
- More sophisticated color relationships
- Better mobile-first responsive design

## Usage Examples

### Basic Usage - Class-Based Approach
```python
from eidos import Button, Card, H1, Text, button_styles, card_styles
from eidos.templates import page

def my_page():
    return page(
        "My App",
        Card(
            H1("Welcome to EidosUI"),
            Text("A modern UI library for Python web apps", 
                 cls="text-text-muted mb-6"),
            Button("Get Started", cls=button_styles.primary),
            Button("Learn More", cls=button_styles.ghost),
            cls=card_styles.elevated,
            padding_cls=card_styles.spacious
        )
    )
```

### Flexible Component Usage
```python
from eidos import Button, button_styles, form_styles

# Using provided styles
Button("Save", cls=button_styles.success)

# Using custom Tailwind classes
Button("Delete", cls="bg-red-600 hover:bg-red-700 text-white px-4 py-2 rounded-lg")

# Combining provided styles with custom classes
Button("Submit", cls=f"{button_styles.primary} w-full mt-4")

# Input with error state
Input(cls=f"{form_styles.input} {form_styles.input_error}")
```

### Mobile-First Responsive Design
```python
from eidos import Grid, Card, H2, Text, layout_styles

def responsive_grid():
    return Grid(
        Card(H2("Feature 1"), Text("Description")),
        Card(H2("Feature 2"), Text("Description")),  
        Card(H2("Feature 3"), Text("Description")),
        # Auto-responsive: 1 col on mobile, 2 on tablet, 3 on desktop
        cls=layout_styles.grid_responsive
    )
```

### Theme Integration
```python
# Theme is handled via CSS variables and data attributes
# No Python theme context needed - just include theme CSS

from eidos.templates import page
from eidos.core.themes import theme_switcher_script

def app_with_theme_switcher():
    return page(
        "My App",
        # Theme switcher button
        ft.Button("🌙", onclick="toggleTheme()", 
                 cls="fixed top-4 right-4 p-2 rounded-lg bg-surface"),
        # App content...
        scripts=[theme_switcher_script()]
    )
```

## Implementation Timeline

### Week 1-2: Foundation
- Project structure setup
- Theme system core implementation
- Base component infrastructure  
- Typography and basic layout components

### Week 3-4: Core Components
- Form components (Button, Input, etc.)
- Card and container components
- Integration with fastapi-tag-exploration pattern

### Week 5-6: Advanced Features
- Theme switching functionality
- Navigation components
- Feedback components (alerts, modals)

### Week 7-8: Polish & Documentation
- Component documentation
- Usage examples
- Performance optimization
- Testing suite

## References and Key Code Snippets

### Tailwind CSS Integration
```html
<!-- Required in HTML head -->
<script src="https://cdn.tailwindcss.com"></script>
<script>
  tailwind.config = {
    darkMode: 'class',
    theme: {
      extend: {
        colors: {
          primary: 'var(--color-primary)',
          secondary: 'var(--color-secondary)'
        }
      }
    }
  }
</script>
```


This plan provides a comprehensive roadmap for building EidosUI as a modern, theme-aware UI library that integrates seamlessly with the fastapi-tag-exploration pattern while providing significant aesthetic and functional improvements over existing solutions. 