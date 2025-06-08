"""Theme management system for EidosUI using CSS variables"""

from typing import Optional
import os
import pathlib


class ThemeManager:
    """Manages CSS variable-based themes with Python interface for DX"""
    
    def __init__(self):
        self._current_theme = "light"
        self._theme_dir = pathlib.Path(__file__).parent.parent / "themes"
        
    def get_css_var(self, var_name: str) -> str:
        """Get CSS variable value for Python DX"""
        return f"var(--{var_name})"
    
    def get_theme_css_path(self, theme_name: str = "light") -> pathlib.Path:
        """Get path to theme CSS file"""
        return self._theme_dir / f"{theme_name}.css"
    
    def get_theme_css_content(self, theme_name: str = "light") -> str:
        """Get CSS content for a theme"""
        css_path = self.get_theme_css_path(theme_name)
        if css_path.exists():
            return css_path.read_text()
        return ""
    



def set_theme_js(theme_name: str = "light") -> str:
    """Generate JavaScript to set theme via data attribute"""
    return f'document.documentElement.setAttribute("data-theme", "{theme_name}");'


def get_theme_css_link(theme_name: str = "light", href_prefix: str = "/static/eidos/themes/") -> str:
    """Get HTML link tag for theme CSS"""
    return f'<link rel="stylesheet" href="{href_prefix}{theme_name}.css">'


def theme_switcher_script() -> str:
    """JavaScript for theme switching functionality"""
    return """
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('eidos-theme', theme);
        document.dispatchEvent(new CustomEvent('eidos:theme-changed', {
            detail: { theme: theme }
        }));
    }
    
    function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme') || 'light';
        const next = current === 'light' ? 'dark' : 'light';
        setTheme(next);
    }
    
    function initTheme() {
        const savedTheme = localStorage.getItem('eidos-theme');
        const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
        setTheme(savedTheme || systemTheme);
    }
    
    // Auto-initialize
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }
    """


# Global theme manager instance
theme_manager = ThemeManager() 