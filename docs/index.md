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

## MonsterUI

### Background Context

I previously built MonsterUI.  80% of people that have seen this have asked a question like:

- How is this different from `MonsterUI`?
- Is this `MonsterUI` version 2?
- Will I still use/support/maintain `MonsterUI`?

This section is designed to answer those, and other related questions.

### Why I build MonsterUI

I built MonsterUI because I tried `fasthtml` and loved it, but found UI challenging in python.  Its origins were as a wrapper for `frankenui`, originally called `fh-frankenui`.  But really, the goal of the library was to make any UI thing very simple and it quickly grew way beyond a wrapper.  While `frankenui` remained a big part of the library it grew to include many things that were not part of the `frankenui` project.

- Lots of custom typography styling using tailwind
- Custom component for navbar
- Server side markdown rendering using Mistletoe, and class injection
- Code Syntax Highlighting
- Latex Rendering
- DaisyUI components
- Small bits of custom JS and CSS for toasts, scrollspy, etc.
- Theme syncing between frankenui, highlightjs, katex, daisyui,
- And more

Because of this prior to release I changed the name to `MonsterUI`, because it grew beyond a wrapper but wanted the keep a monster themed name as a nod to the original inspiration from `frankenui`.  As you can see, all of those extra things are incredibly useful and practical.  MonsterUI is the best UI framework for fast iteration speed because of those features being all inclusive.

I still use MonsterUI and still support it, and I have no plans of that changing.  Eidos UI serves a different purpose for me.

### Why I'm building Eidos UI

All those features made for fast iteration speed, but it also made the library difficult to understand and customize.  Even the top users and contributors of `MonsterUI` typically describe it as mostly a `FrankenUI` wrapper because the core concept is difficult to understand and that simplifies it.  This means customization is difficult.  When I have a specific look I want to create I find myself using tailwind instead and abandoning MonsterUI (and I kinda hate tailwind TBH).  The number 1 source of confusion for MonsterUI from users is around extending it (themes, frankenui vs daisyui vs uikit vs tailwind deps, highlightjs languages, navbar css, etc.)

So I decided to build Eidos UI.  I have a great library (MonsterUI) when I want to maximize iteration speed and convenience to create a decent looking page, and that's most of what I do.  But now want a great library (EidosUI) to help me make great looking pages that I can customize at the different layers of abstraction easily.  This will give me 2 libraries that between the two can cover 100% of my use cases.

So Eidos UI is designed to be less magical, a bit more verbose, and more modular.  It will probably take more lines of code and more knowledge to build with Eidos UI, but it will be more flexible.

