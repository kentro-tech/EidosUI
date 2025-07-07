"""Core utility functions for EidosUI."""

from typing import Optional, Union, List
import os
import sys


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


def get_eidos_static_directory() -> str:
    """
    Get the path to eidos static files for mounting in FastAPI/Air apps.
    
    This function returns the directory containing the eidos package files,
    which includes the CSS directory. Use this when mounting static files
    in your application.
    
    Returns:
        The absolute path to the eidos package directory
        
    Example:
        >>> from fastapi.staticfiles import StaticFiles
        >>> from eidos.utils import get_eidos_static_directory
        >>> app.mount("/eidos", StaticFiles(directory=get_eidos_static_directory()), name="eidos")
    """
    try:
        from importlib.resources import files
        return str(files('eidos'))
    except (ImportError, AttributeError):
        # Fallback for development or if importlib.resources fails
        return os.path.dirname(os.path.abspath(__file__))