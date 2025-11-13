"""
Example of adding a custom extension to EidosUI's markdown renderer.

This shows how to extend the built-in markdown functionality with
custom syntax and rendering.
"""

import air
from markdown.extensions import Extension
from markdown.inlinepatterns import InlineProcessor, SimpleTagInlineProcessor
from markdown.util import AtomicString
import xml.etree.ElementTree as etree

from eidos import *
from eidos.plugins.markdown import MarkdownRenderer, MarkdownCSS
from eidos.utils import get_eidos_static_files


###
### MENTION EXTENSION
###

class MentionPattern(SimpleTagInlineProcessor):
    """Converts @username to a styled mention link."""
    
    def handleMatch(self, m, data):
        """Handle the pattern match."""
        username = m.group(1)
        
        # Create a link element
        link = etree.Element('a')
        link.set('href', f'/user/{username}')
        link.set('class', 'mention-link')
        
        # Create the span inside the link
        span = etree.Element('span')
        span.set('class', 'mention')
        span.text = AtomicString(f'@{username}')
        
        link.append(span)
        
        return link, m.start(0), m.end(0)


class MentionExtension(Extension):
    """Extension that adds @mention support."""
    
    def extendMarkdown(self, md):
        # Add the mention pattern: @username
        mention_pattern = MentionPattern(r'@(\w+)', md)
        md.inlinePatterns.register(mention_pattern, 'mention', 160)

###
### EMOJI EXTENSION
###

class EmojiPattern(InlineProcessor):
    """Converts :emoji: shortcuts to actual emojis."""
    
    EMOJI_MAP = {
        'smile': '😊',
        'heart': '❤️',
        'star': '⭐',
        'fire': '🔥',
        'rocket': '🚀',
        'check': '✅',
        'x': '❌',
        'warning': '⚠️',
        'info': 'ℹ️',
        'bulb': '💡',
    }
    
    def handleMatch(self, m, data):
        """Handle the pattern match."""
        emoji_name = m.group(1)
        
        if emoji_name in self.EMOJI_MAP:
            el = etree.Element('span')
            el.set('class', 'emoji')
            el.text = self.EMOJI_MAP[emoji_name]
            return el, m.start(0), m.end(0)
        
        # If emoji not found, return the original text
        return None, None, None


class EmojiExtension(Extension):
    """Extension that adds :emoji: support."""
    
    def extendMarkdown(self, md):
        emoji_pattern = EmojiPattern(r':(\w+):', md)
        md.inlinePatterns.register(emoji_pattern, 'emoji', 170)


###
### AIR APP
###

app = air.Air()

# Mount static files (include markdown CSS)
for mount_path, directory in get_eidos_static_files(markdown=True).items():
    app.mount(mount_path, air.StaticFiles(directory=directory), name=mount_path.strip("/"))

# Define a function to create a renderer with our custom extensions
def create_renderer():
    return MarkdownRenderer(
        extensions=[
            MentionExtension(),  # Our custom mention extension
            EmojiExtension(),    # Our custom emoji extension
        ]
    )

# Load external files
with open("custom_styles.css", "r") as f:
    CUSTOM_STYLES = f.read()

with open("sample_content.md", "r") as f:
    SAMPLE_MARKDOWN = f.read()

###
### ROUTES
###

@app.get("/")
def home():
    """Homepage demonstrating custom markdown extensions by rendering a markdown file."""
    return Html(
        Head(
            Title("Markdown Extension Example"),
            *EidosHeaders(),
            MarkdownCSS(),
            Style(CUSTOM_STYLES),
        ),
        Body(
            Div(
                H1("Markdown Extension Example"),
                P("This example shows how to add custom extensions to the markdown renderer."),
                
                # Render the markdown with our extensions
                Div(
                    air.Raw(create_renderer().render(SAMPLE_MARKDOWN)),
                    class_="eidos-md mt-8"
                ),
                class_="container mx-auto p-8 max-w-4xl"
            )
        )
    )

@app.get("/user/{username}")
def user_profile(username: str):
    """Display user profile pages that the mentions extension links to."""
    return Html(
        Head(
            Title(f"User: {username}"),
            *EidosHeaders(),
        ),
        Body(
            Main(
                A("← Back to home", href="/", style="color: var(--color-primary);"),
                H1(f"@{username}"),
                P(f"This is the profile page for {username}."),
                class_="max-w-xl mx-auto p-8"
            )
        )
    )