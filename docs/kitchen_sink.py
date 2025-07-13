"""Visual component showcase for EidosUI documentation - adapted from kitchen_sink.py"""

import air
from air.tags import *

import eidos.styles as styles
from eidos.components import DataTable
from eidos.tags import *


def Divider():
    return air.Hr(class_="border-4")


def ComponentSection(title: str, id_=None, *content):
    return Div(Section(H2(title), *content, id=id_, class_="space-y-4 py-20"), Divider())


def components_page():
    """Returns the complete components showcase"""
    return Div(
        ComponentSection(
            "Headings",
            "headings",
            H1("H1"),
            H2("H2"),
            H3("H3"),
            H4("H4"),
            H5("H5"),
            H6("H6"),
        ),
        ComponentSection(
            "Buttons",
            "buttons",
            Div(
                Button("Default"),
                Button("Primary", class_=styles.buttons.primary),
                Button("Secondary", class_=styles.buttons.secondary),
                Button("Ghost", class_=styles.buttons.ghost),
                Button("Outline", class_=styles.buttons.outline),
                Button("Success", class_=styles.buttons.success),
                Button("Error", class_=styles.buttons.error),
                Button("CTA", class_=styles.buttons.cta),
                class_="space-x-4",
            ),
        ),
        ComponentSection(
            "Semantic Typography",
            "semantic-typography",
            air.P(
                "EidosUI provides ",
                Strong("strong emphasis"),
                " for important text, ",
                I("italic styling"),
                " for emphasis, and ",
                Small("small text"),
                " for fine print. You can also use ",
                Mark("highlighted text"),
                " to draw attention to specific words.",
            ),
            air.P(
                "When working with technical content, you might reference ",
                Var("variables"),
                " or show ",
                Code("inline code"),
                ". For keyboard shortcuts, use ",
                Kbd("Ctrl"),
                " + ",
                Kbd("C"),
                " styling. Sample output looks like ",
                Samp("Hello, World!"),
                ".",
            ),
            Blockquote(
                "Design is not just what it looks like and feels like. Design is how it works.",
                Cite("— Steve Jobs"),
            ),
            air.P(
                "Sometimes you need to show ",
                Del("deleted text"),
                " or use abbreviations like ",
                Abbr("HTML", title="HyperText Markup Language"),
                ". Meeting scheduled for ",
                Time("2024-01-15", datetime="2024-01-15"),
                ".",
            ),
            Details(
                Summary("Click to expand more examples"),
                air.Div(
                    H3("Code Examples"),
                    Pre("def hello_world():\n    print('Hello from EidosUI!')\n    return True"),
                    H3("Definition List"),
                    Dl(
                        Dt("EidosUI"),
                        Dd("A beautiful, themeable UI component library"),
                        Dt("Semantic HTML"),
                        Dd("HTML elements that clearly describe their meaning"),
                        Dt("CSS Variables"),
                        Dd("Dynamic styling system for easy theming"),
                    ),
                    H3("Contact Information"),
                    Address(
                        "EidosUI Project",
                        air.Br(),
                        "123 Component Street",
                        air.Br(),
                        "Framework City, UI 12345",
                    ),
                    class_=styles.semantic.details_content,
                ),
            ),
            Figure(
                Div("🎨", class_="text-6xl"),
                Figcaption("The EidosUI logo represents beauty and flexibility"),
            ),
        ),
        ComponentSection(
            "Tables",
            "tables",
            H3("Table Tags"),
            Table(
                Thead(Tr(Th("Name"), Th("Age"), Th("Role"))),
                Tbody(
                    Tr(Td("Alice"), Td("28"), Td("Engineer")),
                    Tr(Td("Bob"), Td("32"), Td("Designer")),
                ),
            ),
            H3("DataTable from Lists"),
            DataTable.from_lists(
                [
                    ["Alice", "28", "Engineer"],
                    ["Bob", "32", "Designer"],
                    ["Charlie", "25", "Product Manager"],
                    ["Diana", "30", "Data Scientist"],
                ],
                headers=["Name", "Age", "Role"],
            ),
            H3("DataTable from Dictionaries", class_="mt-8"),
            DataTable.from_dicts(
                [
                    {
                        "Product": "EidosUI",
                        "Version": "1.0.0",
                        "Status": "Released",
                        "Downloads": "1,234",
                    },
                    {
                        "Product": "Air Framework",
                        "Version": "2.3.1",
                        "Status": "Beta",
                        "Downloads": "567",
                    },
                    {
                        "Product": "Theme Builder",
                        "Version": "0.9.5",
                        "Status": "Alpha",
                        "Downloads": "89",
                    },
                    {
                        "Product": "Component CLI",
                        "Version": "1.2.0",
                        "Status": "Released",
                        "Downloads": "2,456",
                    },
                ],
                headers=["Product", "Version", "Status", "Downloads"],
            ),
        ),
        ComponentSection(
            "Lucide Icons",
            "lucide-icons",
            Div(
                I(data_lucide="sun", class_="w-2 h-2"),
                I(data_lucide="moon", class_="w-3 h-3"),
                I(data_lucide="menu", class_="w-4 h-4"),
                I(data_lucide="arrow-right", class_="w-8 h-8"),
                I(data_lucide="rocket", class_="w-12 h-12"),
                class_="flex space-x-4",
            ),
        ),
    )
