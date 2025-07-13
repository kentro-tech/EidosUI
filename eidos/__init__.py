"""EidosUI - A modern, flexible Tailwind CSS-based UI library for Python web frameworks.

Quick start:
    >>> from eidos import *
    >>> Table.from_lists([["A", "B"], ["C", "D"]], headers=["Col1", "Col2"])

Or use explicit imports:
    >>> from eidos import Table, Button, H1
    >>> from eidos import styles
"""

# Import all styled HTML tags
from .tags import (
    # Headings
    H1, H2, H3, H4, H5, H6,
    # Body
    Body,
    # Buttons
    Button,
    # Semantic typography
    Strong, I, Small, Del, Abbr, Var, Mark, Time,
    Code, Pre, Kbd, Samp, Blockquote, Cite, Address,
    Hr, Details, Summary, Dl, Dt, Dd, Figure, Figcaption,
    # Table elements
    Table, Thead, Tbody, Tfoot, Tr, Th, Td,
    # Pass-through HTML tags
    A, Area, Article, Aside, Audio, B, Base, Bdi, Bdo, Br,
    Canvas, Caption, Col, Colgroup, Data, Datalist, Dfn, Dialog, Div,
    Em, Embed, Fieldset, Footer, Form, Head, Header, Hgroup, Html,
    Iframe, Img, Input, Ins, Label, Legend, Li, Link,
    Main, Map, Menu, Meta, Meter, Nav, Noscript, Object, Ol, Optgroup, Option, Output,
    P, Param, Picture, Progress, Q, Rp, Rt, Ruby,
    S, Script, Search, Section, Select, Source, Span, Style, Sub, Sup,
    Template, Textarea, Title, Track,
    U, Ul, Video, Wbr
)

# Import style namespaces
from . import styles
from .styles import buttons, typography, semantic, tables

# Import components
from .components import Table, NavBar, EidosHeaders

# Version info
__version__ = "0.4.0"

# Define what's available with "from eidos import *"
__all__ = [
    # Version
    "__version__",
    # Style namespaces
    "styles", "buttons", "typography", "semantic", "tables",
    # Components
    "Table", "NavBar", "EidosHeaders",
    # HTML Tags
    "H1", "H2", "H3", "H4", "H5", "H6", "Body", "Button",
    "Strong", "I", "Small", "Del", "Abbr", "Var", "Mark", "Time",
    "Code", "Pre", "Kbd", "Samp", "Blockquote", "Cite", "Address",
    "Hr", "Details", "Summary", "Dl", "Dt", "Dd", "Figure", "Figcaption",
    "Thead", "Tbody", "Tfoot", "Tr", "Th", "Td",
    "A", "Area", "Article", "Aside", "Audio", "B", "Base", "Bdi", "Bdo", "Br",
    "Canvas", "Caption", "Col", "Colgroup", "Data", "Datalist", "Dfn", "Dialog", "Div",
    "Em", "Embed", "Fieldset", "Footer", "Form", "Head", "Header", "Hgroup", "Html",
    "Iframe", "Img", "Input", "Ins", "Label", "Legend", "Li", "Link",
    "Main", "Map", "Menu", "Meta", "Meter", "Nav", "Noscript", "Object", "Ol", "Optgroup", "Option", "Output",
    "P", "Param", "Picture", "Progress", "Q", "Rp", "Rt", "Ruby",
    "S", "Script", "Search", "Section", "Select", "Source", "Span", "Style", "Sub", "Sup",
    "Template", "Textarea", "Title", "Track",
    "U", "Ul", "Video", "Wbr"
]