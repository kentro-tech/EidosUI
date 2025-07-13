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

Use `data-theme` attribute:

```python
Html(data_theme="dark")  # or "light"
```

Or with JavaScript:

```javascript
document.documentElement.setAttribute('data-theme', 'dark')