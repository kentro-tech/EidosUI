"""Core utility functions for EidosUI."""

from typing import Optional, Union, List


def stringify(*classes: Optional[Union[str, List[str]]]) -> str:
    """
    Concatenate CSS classes, filtering out None values and flattening lists.
    
    Args:
        *classes: Variable number of class strings, lists of strings, or None values
        
    Returns:
        A single space-separated string of CSS classes
        
    Examples:
        >>> stringify("btn", "btn-primary")
        "btn btn-primary"
        
        >>> stringify("btn", None, "btn-lg")
        "btn btn-lg"
        
        >>> stringify(["btn", "btn-primary"], "mt-4")
        "btn btn-primary mt-4"
    """
    result = []
    
    for cls in classes:
        if cls is None:
            continue
        elif isinstance(cls, list):
            # Recursively handle lists
            result.extend(c for c in cls if c)
        elif isinstance(cls, str) and cls.strip():
            result.append(cls.strip())
    
    return " ".join(result)