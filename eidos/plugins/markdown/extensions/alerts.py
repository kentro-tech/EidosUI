"""GitHub-style alerts extension for markdown"""

import re
import xml.etree.ElementTree as etree
from re import Pattern
from xml.etree.ElementTree import Element, SubElement

from markdown import Markdown
from markdown.blockprocessors import BlockProcessor
from markdown.extensions import Extension


class AlertBlockProcessor(BlockProcessor):
    """Process GitHub-style alert blocks"""

    # Pattern to match > [!TYPE] at the start of a blockquote
    RE_ALERT: Pattern[str] = re.compile(r"^> \[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]", re.MULTILINE)

    # Alert type configurations
    ALERT_TYPES: dict[str, dict[str, str]] = {
        "NOTE": {"class": "eidos-alert eidos-alert-info", "icon": "ℹ️", "title": "Note"},
        "TIP": {
            "class": "eidos-alert eidos-alert-success",
            "icon": "💡",
            "title": "Tip",
        },
        "IMPORTANT": {
            "class": "eidos-alert eidos-alert-warning",
            "icon": "❗",
            "title": "Important",
        },
        "WARNING": {
            "class": "eidos-alert eidos-alert-warning",
            "icon": "⚠️",
            "title": "Warning",
        },
        "CAUTION": {
            "class": "eidos-alert eidos-alert-error",
            "icon": "🔴",
            "title": "Caution",
        },
    }

    def test(self, parent: Element, block: str) -> bool:
        """Test if the block is a GitHub-style alert"""
        return bool(self.RE_ALERT.match(block))

    def run(self, parent: Element, blocks: list[str]) -> bool:
        """Process the alert block"""
        block = blocks.pop(0)

        # Extract alert type
        match = self.RE_ALERT.match(block)
        if not match:
            return False

        alert_type = match.group(1)
        alert_config = self.ALERT_TYPES.get(alert_type, self.ALERT_TYPES["NOTE"])

        # Create the alert container
        alert_div = SubElement(parent, "div")
        alert_div.set("class", alert_config["class"])

        # Add the header with icon and title
        header = SubElement(alert_div, "div")
        header.set("class", "eidos-alert-header")

        icon_span = SubElement(header, "span")
        icon_span.set("class", "eidos-alert-icon")
        icon_span.text = alert_config["icon"]

        title_span = SubElement(header, "span")
        title_span.set("class", "eidos-alert-title")
        title_span.text = alert_config["title"]

        content_div = SubElement(alert_div, "div")
        content_div.set("class", "eidos-alert-content")

        # Remove the alert marker and process the remaining content
        content = self.RE_ALERT.sub("", block)

        lines = content.split("\n")
        processed_lines = []

        for line in lines:
            # Remove leading '>' from each line
            if line.startswith(">"):
                line = line[1:].lstrip()
            processed_lines.append(line)

        content_text = "\n".join(processed_lines).strip()

        # Parse the content as markdown
        if content_text:
            temp_element = etree.Element("div")
            self.parser.parseBlocks(temp_element, [content_text])

            for child in temp_element:
                content_div.append(child)

            if len(content_div) == 0:
                p = SubElement(content_div, "p")
                p.text = content_text

        # Continue processing subsequent blocks that might be part of the alert
        while blocks and blocks[0].startswith(">"):
            continuation = blocks.pop(0)
            continuation_text = continuation[1:].lstrip() if continuation.startswith(">") else continuation

            if continuation_text:
                p = SubElement(content_div, "p")
                p.text = continuation_text

        return True


class AlertExtension(Extension):
    """Add GitHub-style alerts to markdown"""

    def extendMarkdown(self, md: Markdown) -> None:
        """Add the alert processor to the markdown instance"""
        md.parser.blockprocessors.register(
            AlertBlockProcessor(md.parser),
            "github_alerts",
            175,  # Priority - process before blockquote
        )
