"""Visual component showcase for EidosUI documentation - adapted from kitchen_sink.py"""

import air

import eidos.styles as styles
from eidos.components import DataTable
from eidos.components.feedback import Feedback
from eidos.components.tabs import AlpineTabs, HTMXTabs
from eidos.tags import *


# Example feedback save function for demo
async def save_feedback_demo(user_id: int, text: str, route: str | None):
    """Demo save function - replace with actual DB logic in production."""
    print(f"💬 Feedback from user {user_id} on route '{route}': {text}")
    return None  # Success


# Initialize feedback component
feedback = Feedback(on_save=save_feedback_demo)


# Route handler for feedback submission
async def handle_feedback(request: air.Request):
    """Handle feedback form submission."""
    # Mock user - replace with actual user from session/auth
    mock_user_id = 1
    return await feedback._submit_handler(request, mock_user_id)


def Divider():
    return air.Hr(class_="border-4")


def ComponentSection(title: str, id_=None, *content):
    return Div(Section(H2(title), *content, id=id_, class_="space-y-4 py-20"), Divider())


def components_page():
    """Returns the complete components showcase"""
    return Div(
        H1("EidosUI Kitchen Sink"),
        P("This is a kitchen sink of all the components in EidosUI to see what's available."),
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
                    class_=styles.typography.details_content,
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
            "Tabs",
            "tabs",
            H3("Alpine.js Tabs (Client-Side)"),
            P("Client-side tabs with Alpine.js - all content loads at once, switches instantly:"),
            AlpineTabs(
                ("Typography", Div(H4("Typography Tab"), P("Content about typography with instant switching."))),
                ("Buttons", Div(H4("Buttons Tab"), P("Button components and styles here."))),
                ("Forms", Div(H4("Forms Tab"), P("Form inputs and validation examples."))),
                selected=0,
            ),
            H3("HTMX-Based Tabs (Server-Side)", class_="mt-8"),
            P("Server-fetched tabs with HTMX for dynamic/heavy content:"),
            HTMXTabs(
                ("Typography", "/tab/typography"),
                ("Lists", "/tab/lists"),
                ("Code", "/tab/code"),
                selected=0,
            ),
        ),
        ComponentSection(
            "Forms",
            "forms",
            H3("Text Inputs"),
            Div(
                Div(
                    Label("Text Input:", for_="text_example"),
                    Input(id="text_example", name="text_example", placeholder="Enter some text"),
                    FormHelp("Basic text input field"),
                ),
                Div(
                    Label("Email Input:", for_="email_example"),
                    EmailInput(id="email_example", name="email_example", placeholder="name@example.com"),
                    FormHelp("Email input with validation"),
                ),
                Div(
                    Label("Password Input:", for_="password_example"),
                    PasswordInput(id="password_example", name="password_example", placeholder="Enter password"),
                    FormHelp("Password input with hidden text"),
                ),
                Div(
                    Label("Search Input:", for_="search_example"),
                    SearchInput(id="search_example", name="search_example", placeholder="Search..."),
                    FormHelp("Search input with clear button"),
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            H3("Numeric and Date Inputs", class_="mt-8"),
            Div(
                Div(
                    Label("Number Input:", for_="number_example"),
                    NumberInput(
                        id="number_example", name="number_example", placeholder="0", min="0", max="100", step="5"
                    ),
                    FormHelp("Number input with min, max, and step"),
                ),
                Div(
                    Label("Date Input:", for_="date_example"),
                    DatePicker(id="date_example", name="date_example"),
                    FormHelp("Date picker input"),
                ),
                Div(
                    Label("Time Input:", for_="time_example"),
                    TimePicker(id="time_example", name="time_example"),
                    FormHelp("Time picker input"),
                ),
                Div(
                    Label("DateTime Input:", for_="datetime_example"),
                    Input(id="datetime_example", name="datetime_example", type="datetime-local"),
                    FormHelp("Combined date and time picker"),
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            H3("Contact Inputs", class_="mt-8"),
            Div(
                Div(
                    Label("Phone Input:", for_="phone_example"),
                    TelInput(id="phone_example", name="phone_example", placeholder="+1 (555) 123-4567"),
                    FormHelp("Telephone number input"),
                ),
                Div(
                    Label("URL Input:", for_="url_example"),
                    UrlInput(id="url_example", name="url_example", placeholder="https://example.com"),
                    FormHelp("URL input with validation"),
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            H3("Text Areas", class_="mt-8"),
            Div(
                Label("Message:", for_="message_example"),
                Textarea(
                    "Enter your message here...",
                    id="message_example",
                    name="message_example",
                    placeholder="Enter your message here...",
                    rows=4,
                ),
                FormHelp("Resizable text area for longer content"),
            ),
            Div(
                Label("Description (Read-only):", for_="readonly_example"),
                Textarea(
                    "This is a read-only text area. You cannot edit this content.",
                    id="readonly_example",
                    name="readonly_example",
                    rows=3,
                    readonly=True,
                ),
                FormHelp("Read-only text area"),
            ),
            H3("Select Dropdowns", class_="mt-8"),
            Div(
                Div(
                    Label("Simple Select:", for_="simple_select"),
                    Select(
                        Option("Choose an option", value="", disabled=True, selected=True),
                        Option("Option 1"),
                        Option("Option 2"),
                        Option("Option 3"),
                        id="simple_select",
                        name="simple_select",
                    ),
                    FormHelp("Basic select dropdown"),
                ),
                Div(
                    Label("Country Select:", for_="country_select"),
                    Select(
                        Option("Select your country", value="", disabled=True),
                        Option("United States", value="us", selected=True),
                        Option("United Kingdom", value="uk"),
                        Option("Canada", value="ca"),
                        Option("Australia", value="au"),
                        Option("Germany", value="de"),
                        Option("France", value="fr"),
                        Option("Japan", value="jp"),
                        Option("Other", value="other"),
                        id="country_select",
                        name="country_select",
                    ),
                    FormHelp("Select with value/label pairs"),
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            Div(
                Div(
                    H3("Checkboxes", class_="mt-8"),
                    P("Select your interests:", class_="font-medium mb-2"),
                    Div(
                        Checkbox(name="interests", label="Technology", value="tech", checked=True),
                        Checkbox(name="interests", label="Design", value="design"),
                        Checkbox(name="interests", label="Business", value="business"),
                        Checkbox(name="interests", label="Science", value="science", checked=True),
                        Checkbox(name="interests", label="Arts", value="arts"),
                        class_="space-y-2 flex flex-col",
                    ),
                    P("Multiple selections allowed", class_=styles.typography.details_content),
                ),
                Div(
                    H3("Radio Buttons", class_="mt-8"),
                    P("Choose your subscription plan:", class_="font-medium mb-2"),
                    Div(
                        Radio(name="plan", label="Free - $0/month", value="free"),
                        Radio(name="plan", label="Basic - $9/month", value="basic", checked=True),
                        Radio(name="plan", label="Pro - $29/month", value="pro"),
                        Radio(name="plan", label="Enterprise - Contact us", value="enterprise"),
                        class_="space-y-2 flex flex-col",
                    ),
                    P("Only one selection allowed", class_="text-sm text-gray-600 mt-2"),
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            H3("File Upload", class_="mt-8"),
            Div(
                Label("Upload Document:", for_="document"),
                FileInput(id="document", name="document", accept=".pdf,.doc,.docx"),
                FormHelp("PDF, DOC, or DOCX files only"),
            ),
            Div(
                Label("Upload Images:", for_="images"),
                FileInput(id="images", name="images", accept="image/*", multiple=True),
                FormHelp("Multiple image files allowed"),
            ),
            H3("Input States", class_="mt-8"),
            Div(
                Div(
                    Label("Required Field:", Span(" *", class_="text-red-500"), for_="required_example"),
                    Input(
                        id="required_example",
                        name="required_example",
                        placeholder="This field is required",
                        required=True,
                    ),
                    FormHelp("This field must be filled out"),
                ),
                Div(
                    Label("Disabled Field:", for_="disabled_example"),
                    Input(id="disabled_example", name="disabled_example", value="Cannot edit this", disabled=True),
                    FormHelp("This field is disabled"),
                ),
                Div(
                    Label("Field with Error:", for_="error_example"),
                    EmailInput(
                        id="error_example",
                        name="error_example",
                        value="invalid@email",
                        aria_invalid="true",
                        aria_describedby="error_example-error",
                    ),
                    FormError("Please enter a valid email address", id="error_example-error"),
                    FormHelp("This field has a validation error"),
                ),
                Div(
                    Label("Read-only Field:", for_="readonly_input"),
                    Input(id="readonly_input", name="readonly_input", value="Read-only value", readonly=True),
                    FormHelp("This field is read-only"),
                ),
                class_="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            H3("Special Inputs", class_="mt-8"),
            Div(
                Label("Color Picker:", for_="color_example"),
                ColorPicker(id="color_example", name="color_example", value="#3b82f6"),
                FormHelp("Click to choose a color"),
            ),
            H3("Form Layout Example", class_="mt-8"),
            Fieldset(
                Legend("Personal Information", class_="text-lg font-semibold mb-4"),
                Div(
                    Div(
                        Label("First Name:", Span(" *", class_="text-red-500"), for_="first_name"),
                        Input(id="first_name", name="first_name", required=True),
                        class_="eidos-form-col",
                    ),
                    Div(
                        Label("Last Name:", Span(" *", class_="text-red-500"), for_="last_name"),
                        Input(id="last_name", name="last_name", required=True),
                        class_="eidos-form-col",
                    ),
                    class_="eidos-form-row",
                ),
                Div(
                    Label("Email:", Span(" *", class_="text-red-500"), for_="email"),
                    EmailInput(id="email", name="email", required=True),
                ),
                Div(
                    Div(Label("City:", for_="city"), Input(id="city", name="city"), class_="eidos-form-col"),
                    Div(
                        Label("State:", for_="state"),
                        Select(
                            Option("Select state", value="", disabled=True, selected=True),
                            Option("CA"),
                            Option("NY"),
                            Option("TX"),
                            Option("FL"),
                            Option("WA"),
                            id="state",
                            name="state",
                        ),
                        class_="eidos-form-col",
                    ),
                    Div(
                        Label("ZIP Code:", for_="zip"),
                        Input(id="zip", name="zip", placeholder="00000"),
                        class_="eidos-form-col",
                    ),
                    class_="eidos-form-row",
                ),
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
        ComponentSection(
            "Feedback",
            "feedback",
            P("Interactive feedback widget with Alpine.js modal and HTMX form submission."),
            H3("Basic Usage"),
            Div(
                feedback.widget(),
                P("Click the feedback button to see the modal in action.", class_="text-sm text-gray-600 mt-2"),
                class_="mb-4",
            ),
        ),
    )
