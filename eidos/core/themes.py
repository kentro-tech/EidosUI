"""Theme management system for EidosUI using CSS variables"""

from typing import Optional
import os
import pathlib


class ThemeManager:
    """Simple theme manager for EidosUI"""
    
    def __init__(self):
        self._theme_dir = pathlib.Path(__file__).parent.parent / "themes"
    






# Global theme manager instance
theme_manager = ThemeManager() 