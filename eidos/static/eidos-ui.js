/**
 * EidosUI Theme Switcher
 * Client-side utilities for theme management
 */

(function() {
    'use strict';
    
    // Theme management functions
    window.EidosUI = {
        /**
         * Set the current theme
         * @param {string} theme - Theme name ('light' or 'dark')
         */
        setTheme: function(theme) {
            document.documentElement.setAttribute('data-theme', theme);
            localStorage.setItem('eidos-theme', theme);
            
            // Dispatch custom event
            document.dispatchEvent(new CustomEvent('eidos:theme-changed', {
                detail: { theme: theme }
            }));
        },
        
        /**
         * Get the current theme
         * @returns {string} Current theme name
         */
        getTheme: function() {
            return document.documentElement.getAttribute('data-theme') || 'light';
        },
        
        /**
         * Toggle between light and dark themes
         */
        toggleTheme: function() {
            const current = this.getTheme();
            const next = current === 'light' ? 'dark' : 'light';
            this.setTheme(next);
        },
        
        /**
         * Initialize theme from localStorage or system preference
         */
        initTheme: function() {
            const savedTheme = localStorage.getItem('eidos-theme');
            const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
            const theme = savedTheme || systemTheme;
            this.setTheme(theme);
        }
    };
    
    // Auto-initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            window.EidosUI.initTheme();
        });
    } else {
        window.EidosUI.initTheme();
    }
    
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
        // Only auto-switch if user hasn't set a preference
        if (!localStorage.getItem('eidos-theme')) {
            window.EidosUI.setTheme(e.matches ? 'dark' : 'light');
        }
    });
    
    // Global functions for convenience
    window.setTheme = window.EidosUI.setTheme.bind(window.EidosUI);
    window.toggleTheme = window.EidosUI.toggleTheme.bind(window.EidosUI);
    
})(); 