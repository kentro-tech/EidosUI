# Agent Instructions

- Use mgrep for most things instead of grep, glob, blob and other searches.  It's a semantic search that works much better.

## Core Behavior

- **Always**: Explain what you're going to do to let me review it prior to implementing.  If you have to read multiple files to understand what needs to change, explain it to me and give me time to process and understand before implementing.
- **Iteration**: Work in small steps.  Lean startup style where tiny steps slowly progress toward the goal, letting me be involved and manually test after each small steps.
- **Learning**: My number 1 goal is to learn, so interact with me in a way that encourages learning.  While that may mean going slower in the short term, that lets me maximize my impact and speed in the long term.
- **Config**: There are very few things on this earth that I hate more than config.  Use it only when neccessary or when there is a massive massive benefit to doing so.

## Web Dev

Stack:
- Air: Web Development library
- Styling: Tailwind
- JS: Alpine.js via Airpine

### Air

- **Air Tags**: Use Air Tags, which bring HTML into python syntax and render to html.  Syntax is children come first as positional argumenets, and then named arguments after.  For example:

```python
import air

air.Div(
    air.H1("Syntax Example"),
    air.P("Hello"),
    air.Strong("World", class_='p-8'),
    class_='p-6',
    )
```

> [!IMPORTANT]
> Notice that that there is no `children=[...]` argument for child tags.  `children` is not a valid argument for air tags.

### Airpine for Alpine.js

#### Core Concept

Airpine maps Alpine.js directives to Python with full autocomplete. Two namespaces:
- `Alpine.at.*` → `@event` (shorthand)
- `Alpine.x.*` → `x-directive`

For reserved words (`if`, `class`, `for`) use trailing underscore (like `x.for_` or `x.bind.class_`)

#### Quick Examples

```python
from airpine import Alpine, RawJS
from air import Div, Button, Input

**Alpine.x.data({"count": 0, "message": ""})
# → x-data="{ count: 0, message: '' }"

**Alpine.at.click("count++")
# → @click="count++"

**Alpine.at.keydown.ctrl.enter("save()")
# → @keydown.ctrl.enter="save()"

**Alpine.x.model("email")
# → x-model="email"

**Alpine.x.show("open")
# → x-show="open"

**Alpine.x.if_("visible")
# → x-if="visible"

# Binding attributes
**Alpine.x.bind.class_("{ 'active': isActive }")
# → x-bind:class="{ 'active': isActive }"

**Alpine.x.bind.disabled("!valid")
# → x-bind:disabled="!valid"

# Loops
**Alpine.x.for_("item in items")
# → x-for="item in items"

**Alpine.x.key("item.id")
# → x-key="item.id"
```

#### Merging Attributes

Use `|` to combine:

```python
Button(
    "Submit",
    **(
        Alpine.x.data({"loading": False}) |
        Alpine.at.click.prevent("submit()") |
        Alpine.x.bind.disabled("loading")
    )
)
```

#### JavaScript Functions

Use `RawJS` for functions in x-data:

```python
**Alpine.x.data({
    "count": 0,
    "increment": RawJS("function() { this.count++; }"),
    "reset": RawJS("() => { this.count = 0; }")
})
# → x-data="{ count: 0, increment: function() { this.count++; }, reset: () => { this.count = 0; } }"
```