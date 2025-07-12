"""Core markdown rendering with theme integration"""

import markdown
from typing import Optional, List, Union
from .extensions.alerts import AlertExtension


class MarkdownRenderer:
    """Core markdown rendering with theme integration"""
    
    def __init__(self, extensions: Optional[List[Union[str, markdown.Extension]]] = None):
        """Initialize the renderer with optional extensions.
        
        Args:
            extensions: List of markdown extension names or instances to enable
        """
        self.extensions = extensions or []
        # Add some useful default extensions
        default_extensions = [
            'fenced_code', 
            'tables', 
            'nl2br', 
            'sane_lists',
            AlertExtension()  # Add GitHub-style alerts
        ]
        self.extensions.extend(default_extensions)
        
        # Initialize the markdown processor
        self.md = markdown.Markdown(extensions=self.extensions)
    
    def render(self, markdown_text: str) -> str:
        """Convert markdown to themed HTML.
        
        Args:
            markdown_text: Raw markdown text to render
            
        Returns:
            HTML string wrapped with eidos-md class for styling
        """
        # Reset the markdown processor to clear any state
        self.md.reset()
        
        # Convert markdown to HTML
        html_content = self.md.convert(markdown_text)
        
        # Wrap in a div with our markdown class for styling
        return f'<div class="eidos-md">{html_content}</div>'
    
    def add_extension(self, extension: str) -> None:
        """Add a markdown extension.
        
        Args:
            extension: Name of the markdown extension to add
        """
        if extension not in self.extensions:
            self.extensions.append(extension)
            # Recreate the markdown processor with new extensions
            self.md = markdown.Markdown(extensions=self.extensions)