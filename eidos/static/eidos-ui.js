/**
 * EidosUI - Minimal Theme Switcher
 */
(function() {
    const themes = window.EIDOS_THEMES || { light: '/eidos/themes/light.css', dark: '/eidos/themes/dark.css' };
    let current = localStorage.getItem('eidos-theme') || Object.keys(themes)[0];
    
    function setTheme(name) {
        if (!themes[name]) return;
        document.querySelectorAll('link[data-eidos-theme]').forEach(l => l.remove());
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = themes[name];
        link.setAttribute('data-eidos-theme', name);
        document.head.appendChild(link);
        document.documentElement.setAttribute('data-theme', name);
        localStorage.setItem('eidos-theme', current = name);
    }
    
    window.setTheme = setTheme;
    window.registerTheme = (name, path) => themes[name] = path;
    window.toggleTheme = () => {
        const names = Object.keys(themes);
        setTheme(names[(names.indexOf(current) + 1) % names.length]);
    };
    
    if (Object.keys(themes).length && !window.EIDOS_NO_AUTO_THEME) setTheme(current);
})(); 