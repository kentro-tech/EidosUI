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
class TypographyStyles:
    """Typography style variations using CSS variables"""
    
    # Heading styles (mobile-first responsive)
    h1: str = "text-2xl sm:text-3xl lg:text-4xl font-bold text-[var(--color-text)] leading-tight"
    h2: str = "text-xl sm:text-2xl lg:text-3xl font-semibold text-[var(--color-text)] leading-tight"
    h3: str = "text-lg sm:text-xl lg:text-2xl font-semibold text-[var(--color-text)] leading-tight"
    h4: str = "text-base sm:text-lg lg:text-xl font-semibold text-[var(--color-text)] leading-tight"
    h5: str = "text-sm sm:text-base lg:text-lg font-medium text-[var(--color-text)] leading-tight"
    h6: str = "text-xs sm:text-sm lg:text-base font-medium text-[var(--color-text)] leading-tight"
    
    # Body text styles
    body: str = "text-base text-[var(--color-text)] leading-relaxed"
    
    # Semantic emphasis
    em: str = "italic"
    strong: str = "font-semibold"
    small: str = "text-sm text-[var(--color-text-muted)]"
    
    # Links
    link: str = "text-[var(--color-primary)] hover:text-[var(--color-primary-hover)] underline underline-offset-2 transition-colors duration-200"
    
    # Text decorations
    code: str = "font-mono bg-[var(--color-surface)] px-1.5 py-0.5 rounded text-sm"
    pre: str = "bg-[var(--color-surface)] border border-[var(--color-border)] rounded-lg p-4 overflow-x-auto text-sm font-mono"
    mark: str = "bg-[var(--color-warning-light)] px-1 rounded"
    blockquote: str = "border-l-4 border-[var(--color-primary)] pl-6 py-2 italic text-[var(--color-text-muted)]"


@dataclass(frozen=True)
class FormStyles:
    """Form component styles using CSS variables"""
    
    # Input styles
    input: str = "w-full px-3 py-2 bg-[var(--color-input)] border border-[var(--color-border)] rounded-lg text-[var(--color-text)] placeholder:text-[var(--color-text-muted)] focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:border-transparent transition-colors duration-200"
    
    # Textarea
    textarea: str = "w-full px-3 py-2 bg-[var(--color-input)] border border-[var(--color-border)] rounded-lg text-[var(--color-text)] placeholder:text-[var(--color-text-muted)] focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:border-transparent transition-colors duration-200 resize-y min-h-[80px]"
    
    # Select
    select: str = "w-full px-3 py-2 bg-[var(--color-input)] border border-[var(--color-border)] rounded-lg text-[var(--color-text)] focus:outline-none focus:ring-2 focus:ring-[var(--color-primary)] focus:border-transparent transition-colors duration-200 appearance-none"
    
    # Labels
    label: str = "block text-sm font-medium text-[var(--color-text)] mb-1"
    
    # Form groups
    form_group: str = "space-y-2"


# Global style instances for easy access
button_styles = ButtonStyles()
typography_styles = TypographyStyles()
form_styles = FormStyles() 