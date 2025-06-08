"""Utility functions for EidosUI"""

from typing import Union, Optional, List


def merge_classes(*classes: Optional[Union[str, List[str]]]) -> str:
    """
    Merge multiple class strings, handling None values and lists
    
    Args:
        *classes: Variable number of class strings, lists of strings, or None values
        
    Returns:
        A single merged class string with duplicates removed and proper spacing
        
    Examples:
        >>> merge_classes("text-base", "font-bold", None, "text-center")
        "text-base font-bold text-center"
        
        >>> merge_classes(["bg-blue-500", "hover:bg-blue-600"], "rounded-lg")
        "bg-blue-500 hover:bg-blue-600 rounded-lg"
    """
    result = []
    
    for cls in classes:
        if cls is None:
            continue
        
        if isinstance(cls, (list, tuple)):
            # Handle lists/tuples of classes
            for item in cls:
                if item and isinstance(item, str):
                    result.extend(item.split())
        elif isinstance(cls, str) and cls.strip():
            # Handle string classes
            result.extend(cls.split())
    
    # Remove duplicates while preserving order
    seen = set()
    unique_classes = []
    for class_name in result:
        if class_name not in seen:
            seen.add(class_name)
            unique_classes.append(class_name)
    
    return ' '.join(unique_classes)


def conditional_classes(base_classes: str, condition: bool, true_classes: str, false_classes: str = "") -> str:
    """
    Apply conditional classes based on a condition
    
    Args:
        base_classes: Base classes that are always applied
        condition: Boolean condition to evaluate
        true_classes: Classes to apply if condition is True
        false_classes: Classes to apply if condition is False
        
    Returns:
        Merged class string
        
    Examples:
        >>> conditional_classes("btn", True, "btn-primary", "btn-secondary")
        "btn btn-primary"
        
        >>> conditional_classes("text-base", False, "text-green-600", "text-red-600")
        "text-base text-red-600"
    """
    classes_to_merge = [base_classes]
    
    if condition:
        classes_to_merge.append(true_classes)
    else:
        classes_to_merge.append(false_classes)
    
    return merge_classes(*classes_to_merge)


def theme_switcher_button(
    light_icon: str = "☀️", 
    dark_icon: str = "🌙",
    cls: str = "p-2 rounded-lg bg-surface hover:bg-surface-elevated transition-colors duration-base border border-border"
) -> str:
    """
    Generate HTML for a theme switcher button
    
    Args:
        light_icon: Icon to show in light mode
        dark_icon: Icon to show in dark mode  
        cls: CSS classes for the button
        
    Returns:
        HTML string for theme switcher button
    """
    return f"""
    <button 
        onclick="toggleTheme()" 
        class="{cls}"
        aria-label="Toggle theme"
    >
        <span class="block [data-theme='dark']_&:hidden">{light_icon}</span>
        <span class="hidden [data-theme='dark']_&:block">{dark_icon}</span>
    </button>
    """


def get_responsive_classes(
    base: str,
    sm: Optional[str] = None,
    md: Optional[str] = None,
    lg: Optional[str] = None,
    xl: Optional[str] = None
) -> str:
    """
    Generate responsive class string with mobile-first approach
    
    Args:
        base: Base classes (mobile)
        sm: Small screen classes (640px+)
        md: Medium screen classes (768px+)
        lg: Large screen classes (1024px+)
        xl: Extra large screen classes (1280px+)
        
    Returns:
        Merged responsive class string
        
    Examples:
        >>> get_responsive_classes("text-sm", sm="text-base", lg="text-lg")
        "text-sm sm:text-base lg:text-lg"
    """
    classes = [base]
    
    if sm:
        classes.append(f"sm:{sm}")
    if md:
        classes.append(f"md:{md}")
    if lg:
        classes.append(f"lg:{lg}")
    if xl:
        classes.append(f"xl:{xl}")
        
    return merge_classes(*classes)


def create_size_variants(base_classes: str, size_map: dict) -> dict:
    """
    Create size variants by combining base classes with size-specific classes
    
    Args:
        base_classes: Base classes that apply to all sizes
        size_map: Dictionary mapping size names to size-specific classes
        
    Returns:
        Dictionary mapping size names to complete class strings
        
    Examples:
        >>> base = "bg-primary text-white rounded-lg"
        >>> sizes = {"sm": "px-2 py-1 text-sm", "lg": "px-6 py-3 text-lg"}
        >>> create_size_variants(base, sizes)
        {"sm": "bg-primary text-white rounded-lg px-2 py-1 text-sm", 
         "lg": "bg-primary text-white rounded-lg px-6 py-3 text-lg"}
    """
    return {
        size: merge_classes(base_classes, size_classes)
        for size, size_classes in size_map.items()
    } 