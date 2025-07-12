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
    
    for class_ in classes:
        if class_ is None:
            continue
        elif isinstance(class_, list):
            # Recursively handle lists
            result.extend(c for c in class_ if c)
        elif isinstance(class_, str) and class_.strip():
            result.append(class_.strip())
    
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
        import pathlib
        # Convert MultiplexedPath to actual filesystem path
        eidos_path = files('eidos')
        if hasattr(eidos_path, '_paths'):
            # MultiplexedPath - get the first valid path
            for path in eidos_path._paths:
                if isinstance(path, pathlib.Path) and path.exists():
                    return str(path)
        # Try to get the path directly
        return str(eidos_path)
    except (ImportError, AttributeError):
        # Fallback for development or if importlib.resources fails
        return os.path.dirname(os.path.abspath(__file__))