/**
 * EidosUI Theme Switcher
 * Handles light/dark theme toggling with localStorage persistence
 */

(function() {
    const THEME_KEY = 'eidos-theme-preference';
    
    function getTheme() {
        const saved = localStorage.getItem(THEME_KEY);
        if (saved === 'light' || saved === 'dark') return saved;
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    
    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(THEME_KEY, theme);
        updateButtons(theme);
    }
    
    function updateButtons(theme) {
        const buttons = document.querySelectorAll('.eidos-theme-switch');
        buttons.forEach(btn => {
            const lightIcon = btn.dataset.lightIcon || '☀️';
            const darkIcon = btn.dataset.darkIcon || '🌙';
            const variant = btn.dataset.variant || 'icon';
            
            if (variant === 'icon') {
                btn.textContent = theme === 'dark' ? lightIcon : darkIcon;
            } else {
                btn.textContent = theme === 'dark' ? 'Light Mode' : 'Dark Mode';
            }
            
            btn.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
        });
    }
    
    function toggleTheme() {
        const current = document.documentElement.getAttribute('data-theme');
        setTheme(current === 'dark' ? 'light' : 'dark');
    }
    
    function init() {
        const theme = getTheme();
        setTheme(theme);
        
        const buttons = document.querySelectorAll('.eidos-theme-switch');
        buttons.forEach(btn => {
            btn.onclick = toggleTheme;
        });
    }
    
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
