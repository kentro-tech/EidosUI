# Theming

EidosUI uses CSS variables for theming. Change variables to customize appearance.

## Built-in Themes

### Light Theme
Default theme. Defined in `/eidos/css/themes/light.css`.

### Dark Theme  
Dark mode. Defined in `/eidos/css/themes/dark.css`.

## Theme Structure

### Colors

```css
/* Primary */
--color-primary: #3b82f6;
--color-primary-hover: #2563eb;
--color-primary-light: #dbeafe;
--color-primary-dark: #1d4ed8;
--color-primary-foreground: #ffffff;

/* Semantic */
--color-success: #10b981;
--color-warning: #eab308;
--color-error: #dc2626;
--color-info: #0ea5e9;
```

### Typography

```css
/* Font Sizes */
--font-size-xs: 0.75rem;
--font-size-sm: 0.875rem;
--font-size-base: 1rem;
--font-size-lg: 1.125rem;
--font-size-xl: 1.25rem;

/* Font Weights */
--font-weight-normal: 400;
--font-weight-medium: 500;
--font-weight-semibold: 600;
--font-weight-bold: 700;
```

### Spacing

```css
--space-xs: 0.25rem;
--space-sm: 0.5rem;
--space-md: 1rem;
--space-lg: 1.5rem;
--space-xl: 2rem;
```

## Creating a Theme

1. Copy `/eidos/css/themes/light.css`
2. Modify CSS variables
3. Include in your app:

```python
Head(
    *EidosHeaders(),
    Link(rel="stylesheet", href="/static/my-theme.css")
)
```

## Switching Themes

EidosUI includes a built-in theme switcher that handles light/dark mode automatically.

### Using the Theme Switch

Simply include `ThemeSwitch()` in your navigation:

```python
from eidos import EidosHeaders, NavBar, ThemeSwitch

Head(*EidosHeaders())  # Theme switching included by default

Body(
    NavBar(
        A("Home", href="/"),
        ThemeSwitch(),  # Adds theme toggle button
        lcontents=H3("My App")
    )
)
```

The theme switcher:
- Respects system preferences by default
- Persists user choice in localStorage  
- Updates instantly without page reload
- Works with multiple buttons on the same page

### Customizing the Theme Switch

```python
# Text variant
ThemeSwitch(variant="text")

# Custom icons
ThemeSwitch(light_icon="☀️", dark_icon="🌙")

# Custom styling
ThemeSwitch(class_="p-3 rounded-lg")
```

### Manual Theme Control

You can also set theme programmatically:

```javascript
// Set theme manually
document.documentElement.setAttribute('data-theme', 'dark')
localStorage.setItem('eidos-theme-preference', 'dark')
```