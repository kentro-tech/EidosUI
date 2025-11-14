// EidosUI Theme Switcher using Alpine.js
document.addEventListener('alpine:init', () => {
    Alpine.store('theme', {
        current: 'light',
        
        init() {
            const saved = localStorage.getItem('eidos-theme-preference');
            this.current = (saved === 'light' || saved === 'dark')
                ? saved
                : (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
            this.apply();
        },
        
        toggle() {
            this.current = this.current === 'dark' ? 'light' : 'dark';
            this.apply();
        },
        
        apply() {
            document.documentElement.setAttribute('data-theme', this.current);
            localStorage.setItem('eidos-theme-preference', this.current);
        },
        
        getIcon(lightIcon = '☀️', darkIcon = '🌙') {
            return this.current === 'dark' ? lightIcon : darkIcon;
        },
        
        getLabel() {
            return this.current === 'dark' ? 'Switch to light mode' : 'Switch to dark mode';
        },
        
        getText() {
            return this.current === 'dark' ? 'Light Mode' : 'Dark Mode';
        }
    });
});

// Initialize theme store
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        if (window.Alpine && Alpine.store('theme')) {
            Alpine.store('theme').init();
        }
    });
} else {
    if (window.Alpine && Alpine.store('theme')) {
        Alpine.store('theme').init();
    }
}
