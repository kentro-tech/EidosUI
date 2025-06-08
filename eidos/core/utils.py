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