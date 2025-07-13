"""Extract API documentation from Python modules"""

import inspect
import importlib
from typing import List, Dict, Any, Optional
import re

def clean_docstring(doc: Optional[str]) -> Optional[str]:
    """Clean and format docstring"""
    if not doc:
        return None
    # Remove extra whitespace while preserving structure
    lines = doc.strip().split('\n')
    if not lines:
        return None
    
    # Find minimum indentation
    min_indent = float('inf')
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = len(line) - len(stripped)
            min_indent = min(min_indent, indent)
    
    # Remove common indentation
    if min_indent < float('inf'):
        lines = [lines[0]] + [line[min_indent:] if line.strip() else line for line in lines[1:]]
    
    return '\n'.join(lines)

def extract_function_info(func, module_name: str = None) -> Dict[str, Any]:
    """Extract information from a function"""
    sig = inspect.signature(func)
    doc = inspect.getdoc(func)
    
    # Get parameter info
    params = []
    for name, param in sig.parameters.items():
        param_info = {
            'name': name,
            'default': param.default if param.default != inspect.Parameter.empty else None,
            'annotation': str(param.annotation) if param.annotation != inspect.Parameter.empty else None,
            'kind': str(param.kind)
        }
        params.append(param_info)
    
    # Get return type
    return_annotation = None
    if sig.return_annotation != inspect.Signature.empty:
        return_annotation = str(sig.return_annotation)
    
    # Check if it's from the module we're documenting
    is_local = True
    if module_name and hasattr(func, '__module__'):
        is_local = func.__module__ == module_name
    
    return {
        'name': func.__name__,
        'signature': str(sig),
        'doc': clean_docstring(doc),
        'params': params,
        'return_annotation': return_annotation,
        'is_local': is_local
    }

def extract_class_info(cls, module_name: str = None) -> Dict[str, Any]:
    """Extract information from a class"""
    doc = inspect.getdoc(cls)
    
    # Get methods
    methods = []
    for name, method in inspect.getmembers(cls, inspect.isfunction):
        if not name.startswith('_') or name == '__init__':
            method_info = extract_function_info(method, module_name)
            method_info['is_method'] = True
            methods.append(method_info)
    
    # Get class methods
    for name, method in inspect.getmembers(cls, inspect.ismethod):
        if not name.startswith('_'):
            method_info = extract_function_info(method, module_name)
            method_info['is_classmethod'] = True
            methods.append(method_info)
    
    # Check if it's from the module we're documenting
    is_local = True
    if module_name and hasattr(cls, '__module__'):
        is_local = cls.__module__ == module_name
    
    return {
        'name': cls.__name__,
        'doc': clean_docstring(doc),
        'methods': methods,
        'is_local': is_local,
        'bases': [base.__name__ for base in cls.__bases__ if base.__name__ != 'object']
    }

def extract_module_api(module_name: str) -> Dict[str, Any]:
    """Extract API info from a module"""
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        return {
            'error': f"Could not import module {module_name}: {e}",
            'module': module_name
        }
    
    functions = []
    classes = []
    constants = []
    
    # Get all members
    for name, obj in inspect.getmembers(module):
        # Skip private members
        if name.startswith('_'):
            continue
            
        # Skip imported members (focus on what's defined in this module)
        if hasattr(obj, '__module__') and obj.__module__ != module_name:
            # Exception: include if it's re-exported (common pattern)
            if not hasattr(module, '__all__') or name not in module.__all__:
                continue
        
        if inspect.isfunction(obj):
            functions.append(extract_function_info(obj, module_name))
        elif inspect.isclass(obj):
            classes.append(extract_class_info(obj, module_name))
        elif isinstance(obj, (str, int, float, bool, type(None))):
            # Simple constants
            constants.append({
                'name': name,
                'value': repr(obj),
                'type': type(obj).__name__
            })
    
    # Sort alphabetically
    functions.sort(key=lambda x: x['name'])
    classes.sort(key=lambda x: x['name'])
    constants.sort(key=lambda x: x['name'])
    
    return {
        'module': module_name,
        'doc': clean_docstring(inspect.getdoc(module)),
        'functions': functions,
        'classes': classes,
        'constants': constants
    }

def get_available_modules() -> List[str]:
    """Get list of available EidosUI modules"""
    modules = [
        'eidos.tags',
        'eidos.styles',
        'eidos.components.navigation',
        'eidos.components.headers',
        'eidos.utils'
    ]
    
    # Add markdown plugin if available
    try:
        import eidos.plugins.markdown
        modules.append('eidos.plugins.markdown')
    except ImportError:
        pass
    
    # Filter out modules that don't exist
    available = []
    for mod in modules:
        try:
            importlib.import_module(mod)
            available.append(mod)
        except ImportError:
            pass
    
    return available