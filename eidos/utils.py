"""Core utility functions for EidosUI."""

from pathlib import Path


def stringify(*classes: str | list[str] | None) -> str:
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
    result: list[str] = []

    for class_ in classes:
        if class_ is None:
            continue
        elif isinstance(class_, (list | tuple)):
            result.extend(c for c in class_ if c)
        elif isinstance(class_, str) and class_.strip():
            result.append(class_.strip())

    return " ".join(result)


def get_eidos_static_files(markdown: bool = False) -> dict[str, str]:
    """
    Get a dictionary mapping URL paths to static file directories.

    This provides a safe way to mount only specific static assets
    without exposing Python source files.

    Args:
        markdown: Whether to include markdown plugin CSS (default: False)

    Returns:
        Dict mapping mount paths to directory paths

    Example:
        >>> from fastapi.staticfiles import StaticFiles
        >>> from eidos.utils import get_eidos_static_files
        >>> # Basic usage - just core CSS and JS
        >>> for mount_path, directory in get_eidos_static_files().items():
        ...     app.mount(mount_path, StaticFiles(directory=directory), name=mount_path.strip('/'))
        >>>
        >>> # Include markdown CSS
        >>> for mount_path, directory in get_eidos_static_files(markdown=True).items():
        ...     app.mount(mount_path, StaticFiles(directory=directory), name=mount_path.strip('/'))
    """
    # Use pathlib for cleaner path handling
    base_path = Path(__file__).parent.absolute()

    static_files = {
        "/eidos/css": str(base_path / "css"),
        "/eidos/js": str(base_path / "js"),
    }

    # Only include markdown CSS if requested
    if markdown:
        static_files["/eidos/plugins/markdown/css"] = str(base_path / "plugins" / "markdown" / "css")

    return static_files
