# Styling System

EidosUI's styling system provides flexible, themeable components through a layered approach using CSS variables, Tailwind utilities, and custom classes.

## Overview

The styling system consists of:

1. **CSS Variables** - Dynamic values for colors, spacing, typography
2. **Base Styles** - Component definitions using variables
3. **Theme Files** - Variable definitions for different themes
4. **Style Enums** - Python access to CSS classes
5. **Tailwind Utilities** - Additional styling flexibility

## CSS Variable System

### Core Variables

EidosUI uses CSS variables for all themeable properties:

```css
/* Colors */
--eidos-primary: #3182ce;
--eidos-primary-hover: #2563eb;
--eidos-primary-text: #ffffff;

/* Typography */
--eidos-font-family: system-ui, -apple-system, sans-serif;
--eidos-text-base: 1rem;
--eidos-text-lg: 1.125rem;

/* Spacing */
--eidos-spacing-4: 1rem;
--eidos-spacing-8: 2rem;

/* Borders */
--eidos-border-radius: 0.375rem;
--eidos-border-width: 1px;
```

### Color System

EidosUI uses a semantic color system:

```css
/* Semantic colors */
--eidos-text-primary: var(--eidos-gray-900);
--eidos-text-secondary: var(--eidos-gray-600);
--eidos-bg-primary: var(--eidos-white);
--eidos-bg-secondary: var(--eidos-gray-50);

/* State colors */
--eidos-success: var(--eidos-green-600);
--eidos-error: var(--eidos-red-600);
--eidos-warning: var(--eidos-yellow-600);
--eidos-info: var(--eidos-blue-600);
```

### Using Variables in Components

```python
# Components automatically use the variables
H1("Styled Heading")  # Uses --eidos-text-4xl, --eidos-font-bold

# Custom styling with variables
Div(
    "Custom styled content",
    style="color: var(--eidos-primary); padding: var(--eidos-spacing-4);"
)
```

## Theme System

### Built-in Themes

EidosUI includes light and dark themes:

```python
# Theme is controlled by data-theme attribute
Html(data_theme="light")  # or "dark"

# Toggle theme with JavaScript
Script("""
function toggleTheme() {
    const html = document.documentElement;
    const current = html.getAttribute('data-theme');
    html.setAttribute('data-theme', current === 'dark' ? 'light' : 'dark');
}
""")
```

### Creating Custom Themes

1. Create a CSS file with your variable overrides:

```css
/* my-theme.css */
:root[data-theme="my-brand"] {
    /* Colors */
    --eidos-primary: #ff6b35;
    --eidos-primary-hover: #ff5722;
    --eidos-primary-text: #ffffff;
    
    /* Typography */
    --eidos-font-family: 'Inter', sans-serif;
    --eidos-heading-font: 'Poppins', sans-serif;
    
    /* Customize any variable */
    --eidos-border-radius: 0.5rem;
    --eidos-shadow-lg: 0 20px 25px -5px rgb(0 0 0 / 0.1);
}
```

2. Include your theme CSS:

```python
Head(
    *EidosHeaders(),
    Link(rel="stylesheet", href="/static/my-theme.css")
)
```

3. Apply the theme:

```python
Html(data_theme="my-brand")
```

## Style Enums

Access CSS classes through Python enums:

```python
import eidos.styles as styles

# Button styles
Button("Primary", class_=styles.buttons.primary)
Button("Secondary", class_=styles.buttons.secondary)
Button("Ghost", class_=styles.buttons.ghost)

# Typography styles  
H1("Title", class_=styles.typography.h1)
P("Body text", class_=styles.typography.body)
Small("Caption", class_=styles.typography.caption)

# Semantic styles
Mark("Highlighted", class_=styles.semantic.mark)
Code("code", class_=styles.semantic.code)
```

## Component Styling

### Base Component Styles

Each component has base styles defined with CSS variables:

```css
.eidos-button {
    /* Structure */
    display: inline-flex;
    align-items: center;
    padding: var(--eidos-spacing-2) var(--eidos-spacing-4);
    
    /* Typography */
    font-family: var(--eidos-font-family);
    font-size: var(--eidos-text-base);
    font-weight: var(--eidos-font-medium);
    
    /* Appearance */
    border-radius: var(--eidos-border-radius);
    transition: all 150ms ease;
}

.eidos-button-primary {
    background: var(--eidos-primary);
    color: var(--eidos-primary-text);
}

.eidos-button-primary:hover {
    background: var(--eidos-primary-hover);
}
```

### Extending Component Styles

Combine EidosUI classes with Tailwind utilities:

```python
Button(
    "Custom Button",
    class_=f"{styles.buttons.primary} shadow-xl transform hover:scale-105"
)
```

## Tailwind Integration

### Using Tailwind Utilities

EidosUI works seamlessly with Tailwind:

```python
# Layout utilities
Div(
    content,
    class_="flex items-center justify-between p-4"
)

# Responsive design
Card(
    content,
    class_="w-full md:w-1/2 lg:w-1/3"
)

# Combining with EidosUI styles
Button(
    "Action",
    class_=f"{styles.buttons.primary} md:text-lg lg:px-8"
)
```

### Common Patterns

```python
# Container
Div(content, class_="container mx-auto px-4")

# Grid layout
Div(
    *cards,
    class_="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
)

# Flexbox
Div(
    *items,
    class_="flex flex-wrap items-center gap-4"
)

# Spacing
Section(
    content,
    class_="py-12 md:py-16 lg:py-20"
)
```

## Custom Styling

### Inline Styles

For one-off styling needs:

```python
Div(
    "Special content",
    style="background: linear-gradient(to right, var(--eidos-primary), var(--eidos-secondary));"
)
```

### Custom CSS Classes

Add your own CSS classes:

```css
/* custom.css */
.my-special-card {
    background: var(--eidos-bg-secondary);
    border: 2px dashed var(--eidos-primary);
    padding: var(--eidos-spacing-6);
}
```

```python
Div(content, class_="my-special-card")
```

### Scoped Styles

For component-specific styles:

```python
def FeatureCard(icon, title, description):
    return Div(
        Style("""
            .feature-card {
                transition: transform 200ms;
            }
            .feature-card:hover {
                transform: translateY(-4px);
            }
        """),
        Div(
            icon,
            H3(title),
            P(description),
            class_="feature-card p-6 rounded-lg shadow-md"
        )
    )
```

## Responsive Design

### Mobile-First Approach

```python
Button(
    "Responsive Button",
    class_="text-sm md:text-base lg:text-lg px-4 md:px-6 lg:px-8"
)
```

### Responsive Utilities

```python
# Hide/show at breakpoints
Div(
    Span("Mobile menu", class_="md:hidden"),
    Nav("Desktop menu", class_="hidden md:block")
)

# Responsive grid
Div(
    *items,
    class_="grid grid-cols-2 md:grid-cols-4 lg:grid-cols-6 gap-4"
)
```

## Animation & Transitions

### CSS Transitions

```python
Button(
    "Hover me",
    class_="transition-all duration-300 hover:scale-105 hover:shadow-lg"
)
```

### CSS Animations

```python
# Spinner
Div(
    class_="animate-spin h-5 w-5 border-2 border-primary border-t-transparent rounded-full"
)

# Pulse
Div(
    "New!",
    class_="animate-pulse bg-primary text-white px-2 py-1 rounded"
)
```

### Custom Animations

```css
@keyframes slide-up {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.slide-up {
    animation: slide-up 300ms ease-out;
}
```

## Best Practices

### 1. Use Semantic Classes First

```python
# Prefer semantic components
Strong("Important")  # Not: Span("Important", class_="font-bold")
```

### 2. Leverage CSS Variables

```python
# Use variables for consistency
style="color: var(--eidos-primary);"  # Not: style="color: #3182ce;"
```

### 3. Combine Thoughtfully

```python
# Good: EidosUI + utility classes
Button(
    "Action",
    class_=f"{styles.buttons.primary} shadow-md"
)

# Avoid: Overriding core styles
Button(
    "Action",
    class_="bg-red-500"  # This fights with button styles
)
```

### 4. Theme-Aware Styling

```python
# Colors that adapt to theme
Div(
    content,
    class_="bg-gray-100 dark:bg-gray-800"
)
```

### 5. Performance

- Use CSS classes over inline styles
- Prefer CSS animations over JavaScript
- Minimize custom CSS specificity

## Debugging Styles

### Browser DevTools

```python
# Add debug classes
Div(
    content,
    class_="debug-border",
    data_component="my-component"  # Easy to find in DevTools
)
```

### CSS Variable Inspector

```javascript
// Log all EidosUI variables
const styles = getComputedStyle(document.documentElement);
const eidosVars = Array.from(document.styleSheets)
    .flatMap(sheet => Array.from(sheet.cssRules))
    .filter(rule => rule.style && rule.selectorText === ':root')
    .flatMap(rule => Array.from(rule.style))
    .filter(prop => prop.startsWith('--eidos'));

eidosVars.forEach(varName => {
    console.log(`${varName}: ${styles.getPropertyValue(varName)}`);
});
```

## Advanced Techniques

### Dynamic Themes

```python
def ThemePicker():
    themes = ["light", "dark", "brand", "high-contrast"]
    return Select(
        *[Option(theme.title(), value=theme) for theme in themes],
        onchange="document.documentElement.setAttribute('data-theme', this.value)"
    )
```

### CSS Variable Calculations

```css
.custom-spacing {
    /* Calculate based on variables */
    padding: calc(var(--eidos-spacing-4) * 1.5);
    margin-top: calc(var(--eidos-spacing-base) + 2rem);
}
```

### Context-Aware Styling

```python
def Card(content, context="default"):
    context_styles = {
        "default": "bg-white dark:bg-gray-800",
        "highlight": "bg-primary-50 dark:bg-primary-900",
        "warning": "bg-yellow-50 dark:bg-yellow-900"
    }
    
    return Div(
        content,
        class_=f"p-6 rounded-lg {context_styles.get(context, context_styles['default'])}"
    )
```