# Styled Tags

EidosUI provides pre-styled versions of HTML tags. Import and use like regular Air tags.

## Usage

```python
from eidos import H1, P, Button, Table

H1("Page Title")
P("Paragraph text")
Button("Click me", type="submit")
```

## Available Tags

### Typography

- `H1` to `H6` - Headings
- `P` - Paragraphs  
- `Strong` - Bold text
- `Em`, `I` - Italic text
- `Small` - Small text
- `Mark` - Highlighted text
- `Code` - Inline code
- `Pre` - Code blocks
- `Blockquote` - Quotes

### Semantic

- `Abbr` - Abbreviations
- `Cite` - Citations
- `Var` - Variables
- `Kbd` - Keyboard input
- `Samp` - Sample output
- `Time` - Time/dates
- `Address` - Addresses

### Structure

- `Table`, `Thead`, `Tbody`, `Tr`, `Th`, `Td` - Tables
- `Dl`, `Dt`, `Dd` - Definition lists
- `Details`, `Summary` - Collapsible content
- `Figure`, `Figcaption` - Figures
- `Hr` - Horizontal rules

### Form Elements

- `Button` - Styled buttons
- `Input`, `Textarea`, `Select` - Form inputs
- `Label` - Form labels
- `Fieldset`, `Legend` - Field groups

## Customizing

Add classes to override defaults:

```python
H1("Title", class_="text-red-500")  # Adds Tailwind class
Button("Submit", class_="custom-btn")  # Your custom class
```

## Pass-through Tags

Some tags have no default styling:

```python
Div, Span, A, Img, Ul, Ol, Li, Nav, Main, Section, Article, Aside, Header, Footer
```

Use these for layout and structure.