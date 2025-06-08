"""Style dataclasses for EidosUI components using CSS variables"""

from dataclasses import dataclass


@dataclass(frozen=True)
class ButtonStyles:
    """Button style variations using CSS variables"""
    
    # Primary styles (most commonly used)
    primary: str = "bg-[var(--color-primary)] hover:bg-[var(--color-primary-hover)] text-[var(--color-primary-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:ring-offset-2 shadow-sm hover:shadow-md active:scale-95"
    secondary: str = "bg-[var(--color-secondary)] hover:bg-[var(--color-secondary-hover)] text-[var(--color-secondary-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-secondary)] focus:ring-offset-2 shadow-sm hover:shadow-md active:scale-95"
    ghost: str = "text-[var(--color-primary)] hover:bg-[var(--color-primary-light)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:ring-offset-2 active:scale-95"
    
    # Semantic styles
    success: str = "bg-[var(--color-success)] hover:bg-[var(--color-success-hover)] text-[var(--color-success-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-success)] focus:ring-offset-2 shadow-sm hover:shadow-md active:scale-95"
    cta: str = "bg-[var(--color-cta)] hover:bg-[var(--color-cta-hover)] text-[var(--color-cta-foreground)] font-semibold rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-cta)] focus:ring-offset-2 shadow-md hover:shadow-lg active:scale-95 transform"
    warning: str = "bg-[var(--color-warning)] hover:bg-[var(--color-warning-hover)] text-[var(--color-warning-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-warning)] focus:ring-offset-2 shadow-sm hover:shadow-md active:scale-95"
    error: str = "bg-[var(--color-error)] hover:bg-[var(--color-error-hover)] text-[var(--color-error-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-error)] focus:ring-offset-2 shadow-sm hover:shadow-md active:scale-95"
    info: str = "bg-[var(--color-info)] hover:bg-[var(--color-info-hover)] text-[var(--color-info-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-info)] focus:ring-offset-2 shadow-sm hover:shadow-md active:scale-95"
    
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
    outline_primary: str = "border-2 border-[var(--color-primary)] text-[var(--color-primary)] hover:bg-[var(--color-primary)] hover:text-[var(--color-primary-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:ring-offset-2 active:scale-95"
    outline_secondary: str = "border-2 border-[var(--color-secondary)] text-[var(--color-secondary)] hover:bg-[var(--color-secondary)] hover:text-[var(--color-secondary-foreground)] font-medium rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-secondary)] focus:ring-offset-2 active:scale-95"
    link: str = "text-[var(--color-primary)] hover:text-[var(--color-primary-hover)] underline-offset-4 hover:underline font-medium transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:ring-offset-2 rounded active:scale-95"


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