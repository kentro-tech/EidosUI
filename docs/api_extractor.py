"""Extract API documentation from Python modules"""

import importlib
import inspect
from typing import Any


def extract_module_api(module_name: str) -> dict[str, Any]:
    """Extract API info from a module"""
    try:
        module = importlib.import_module(module_name)
    except ImportError as e:
        return {
            "error": f"Could not import module {module_name}: {e}",
            "module": module_name,
        }

    items = []

    # Get all members in order of definition
    for name, obj in inspect.getmembers(module):
        # Skip private members
        if name.startswith("_"):
            continue

        # Skip imported members
        if hasattr(obj, "__module__") and obj.__module__ != module_name:
            if not hasattr(module, "__all__") or name not in module.__all__:
                continue

        item = {"name": name}

        if inspect.isfunction(obj):
            item["type"] = "function"
            item["signature"] = str(inspect.signature(obj))
            item["doc"] = inspect.getdoc(obj) or ""

            # Get parameters
            sig = inspect.signature(obj)
            item["params"] = []
            for param_name, param in sig.parameters.items():
                param_info = {
                    "name": param_name,
                    "annotation": str(param.annotation)
                    if param.annotation != inspect.Parameter.empty
                    else "",
                    "default": str(param.default)
                    if param.default != inspect.Parameter.empty
                    else "",
                }
                item["params"].append(param_info)

            # Return type
            if sig.return_annotation != inspect.Signature.empty:
                item["return_type"] = str(sig.return_annotation)

        elif inspect.isclass(obj):
            item["type"] = "class"
            item["doc"] = inspect.getdoc(obj) or ""
            item["bases"] = [
                base.__name__ for base in obj.__bases__ if base.__name__ != "object"
            ]

            # Get methods
            item["methods"] = []
            for method_name, method in inspect.getmembers(obj, inspect.isfunction):
                if not method_name.startswith("_") or method_name == "__init__":
                    method_info = {
                        "name": method_name,
                        "signature": str(inspect.signature(method)),
                        "doc": (inspect.getdoc(method) or "").split("\n")[
                            0
                        ],  # First line only
                    }
                    item["methods"].append(method_info)

        elif isinstance(obj, (str, int, float, bool, type(None))):
            item["type"] = "constant"
            item["value"] = repr(obj)
            item["value_type"] = type(obj).__name__
        else:
            continue

        items.append(item)

    return {"module": module_name, "doc": inspect.getdoc(module) or "", "items": items}


def get_available_modules() -> list[str]:
    """Get list of available EidosUI modules"""
    # Auto-discover modules by scanning the eidos package
    base_modules = ["eidos.tags", "eidos.styles", "eidos.utils"]

    # Try to discover component modules
    try:
        import pkgutil

        import eidos.components

        for importer, modname, ispkg in pkgutil.iter_modules(eidos.components.__path__):
            base_modules.append(f"eidos.components.{modname}")
    except ImportError:
        pass

    # Try to discover plugin modules
    try:
        import pkgutil

        import eidos.plugins

        for importer, modname, ispkg in pkgutil.iter_modules(eidos.plugins.__path__):
            base_modules.append(f"eidos.plugins.{modname}")
    except ImportError:
        pass

    # Return only modules that actually exist
    return [mod for mod in base_modules if can_import(mod)]


def can_import(module_name: str) -> bool:
    """Check if a module can be imported"""
    try:
        importlib.import_module(module_name)
        return True
    except ImportError:
        return False
