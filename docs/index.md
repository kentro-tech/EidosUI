# EidosUI

I build `EidosUI` to fill a need that I had when building apps.  I wanted a framework that was python first and mostly "just worked" with defaults out of the box.  But I wanted one where I could hack and customize it extremely easily and deeply.  EidosUI is designed to give the best of both worlds.

See the [kitchen-sink](/kitchen-sink) to scroll through all of our components.

## Installation

1. `uv pip install eidosui`
2. Optionally add a [plugin](/plugins) with `uv pip install "eidosui[markdown]"`
3. See our [quick start](/quick-start) to make an app

## Inspiration

As I have begun I find myself drawing inspiration from

- `FastHTML` / `MonsterUI`: `FastHTML` and `MonsterUI` brought a level of simplicity and iteration speed to python web development that did not exist before.  I have and will draw inspiration and adopt many innovative ideas from both of those open source project.
- `NextJS`: I spent time studying and learning NextJS because it is one of the most popular ways to build web apps.  While I found the ecosystem overly complex, there were a lot of really useful things I enjoyed about it.  I plan to use many patterns from my experiences building with NextJS.

And builds on top of (and also helped inspired the project):

- `FastAPI` / `air`:  FastAPI is my favorite framework for making JSON apis.  So when I found out my friends Danny and Audrey were going to work on building a framework to make htmx based web apps with FastAPI I was extremely excited.  And it's been going even better than I could have imagined.
- `tailwind`:  Tailwind is a css framework that is a standard for a reason.  While it's not the most concise or easiest it gives a ton of flexibility.  I find UI development painful, and so I end up writing UI frameworks to alleviate that pain 🤦

## The Design

Check out the [Concepts](/concepts) section for more detail on particular topics, but here's a brief overview.

### The Stylistic Base

#### CSS Variables

Themes are defined as a bunch of css variables in a css file (like `color-primary` and `color-primary-hover`)

```css
[data-theme="light"] {
    /* Core Colors */
    --color-primary: #3b82f6;
    --color-primary-hover: #2563eb;
    ...
}
```

#### CSS Classes

Those css variables are used in a style sheet to define classes (like `eidos-h1`)

```css
.eidos-h1 {
    font-size: var(--font-size-3xl);
    font-weight: var(--font-weight-bold);
    line-height: var(--line-height-tight);
    margin-bottom: var(--space-md);
}
```

### The Python Exposure

#### Style Classes

CSS classes are exposed in python classes like so:

```python
class Typography:
    h1: Final[str] = "eidos-h1"
    h2: Final[str] = "eidos-h2"
    ...
```

#### Tags

Which are the used to create `AirTag` components.

```python
def H1(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H1(*content, class_=stringify(styles.typography.h1, class_), **kwargs)
```

### Components

On top of those tags, we can build more complicated components.  For example `NavBar`'s which combine many Tags, flexbox styling, icons, and some javascript.

### Plugins

Things that do not fit well into any of the above but are still useful are optional plugins to install (like the `markdown` plugin)