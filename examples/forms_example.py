"""Example demonstrating EidosUI form components and Air form integration."""

from pydantic import BaseModel, EmailStr, Field, validator

import air
from eidos import *
from eidos.utils import get_eidos_static_files

# Create Air app
app = air.Air()

# Mount static files
for mount_path, directory in get_eidos_static_files().items():
    app.mount(mount_path, air.StaticFiles(directory=directory), name=mount_path.strip("/"))


# Example 1: Basic form components
@app.page
def basic_form():
    """Demonstrate basic form components."""
    return Html(
        Head(
            Title("EidosUI Forms - Basic Components"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("EidosUI Form Components"),
                
                # Basic text inputs
                Div(
                    Label("Full Name:", for_="fullname"),
                    Span(" *", class_="text-red-500"),
                    Input(
                        id="fullname",
                        name="fullname",
                        placeholder="Enter your full name",
                        required=True
                    ),
                    FormHelp("Please enter your first and last name")
                ),
                
                # Email input
                Div(
                    Label("Email Address:", for_="email"),
                    Span(" *", class_="text-red-500"),
                    EmailInput(
                        id="email",
                        name="email",
                        placeholder="name@example.com",
                        required=True
                    ),
                    FormHelp("We'll never share your email with anyone else")
                ),
                
                # Password input
                Div(
                    Label("Password:", for_="password"),
                    Span(" *", class_="text-red-500"),
                    PasswordInput(
                        id="password",
                        name="password",
                        placeholder="Enter a secure password",
                        required=True
                    ),
                    FormHelp("Must be at least 8 characters long")
                ),
                
                # Textarea
                Div(
                    Label("Message:", for_="message"),
                    Textarea(
                        "Tell us what you think...",
                        id="message",
                        name="message",
                        placeholder="Tell us what you think...",
                        rows=5
                    ),
                    FormHelp("Maximum 500 characters")
                ),
                
                # Select dropdown
                Div(
                    Label("Country:", for_="country"),
                    Span(" *", class_="text-red-500"),
                    Select(
                        Option("Select your country", value="", disabled=True, selected=True),
                        Option("United States", value="us"),
                        Option("United Kingdom", value="uk"),
                        Option("Canada", value="ca"),
                        Option("Australia", value="au"),
                        Option("Other", value="other"),
                        id="country",
                        name="country",
                        required=True
                    ),
                    FormHelp("Please select your country")
                ),
                
                # Checkboxes
                H3("Interests", class_="mt-6 mb-3"),
                Div(
                    Checkbox(name="interests", label="Technology", value="tech"),
                    Checkbox(name="interests", label="Design", value="design"),
                    Checkbox(name="interests", label="Business", value="business"),
                    Checkbox(name="interests", label="Science", value="science"),
                    class_="space-y-2"
                ),
                
                # Radio buttons
                H3("Preferred Contact Method", class_="mt-6 mb-3"),
                Div(
                    Radio(name="contact_method", label="Email", value="email", checked=True),
                    Radio(name="contact_method", label="Phone", value="phone"),
                    Radio(name="contact_method", label="SMS", value="sms"),
                    class_="space-y-2"
                ),
                
                # File upload
                Div(
                    Label("Upload Resume:", for_="resume"),
                    FileInput(
                        id="resume",
                        name="resume",
                        accept=".pdf,.doc,.docx",
                        required=False
                    ),
                    FormHelp("PDF, DOC, or DOCX files only (max 5MB)"),
                    class_="mt-6"
                ),
                
                # Submit button
                Button("Submit Form", type="submit",class_=(styles.buttons.primary,"mt-4")),
                
                class_="max-w-2xl mx-auto p-8"
            )
        )
    ).render()


# Example 2: Form with validation errors
@app.page
def form_with_errors():
    """Demonstrate form with validation errors."""
    return Html(
        Head(
            Title("EidosUI Forms - Validation Errors"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Form with Validation Errors"),
                P("This example shows how form fields look with validation errors.", class_="mb-6"),
                
                # Input with error
                Div(
                    Label("Username:", for_="username"),
                    Span(" *", class_="text-red-500"),
                    Input(
                        id="username",
                        name="username",
                        value="ab",  # Too short
                        aria_invalid="true",
                        aria_describedby="username-error"
                    ),
                    FormError("Username must be at least 3 characters long", id="username-error")
                ),
                
                # Email with error
                Div(
                    Label("Email:", for_="email"),
                    Span(" *", class_="text-red-500"),
                    EmailInput(
                        id="email",
                        name="email",
                        value="invalid-email",
                        aria_invalid="true",
                        aria_describedby="email-error"
                    ),
                    FormError("Please enter a valid email address", id="email-error")
                ),
                
                # Select with error
                Div(
                    Label("Age Group:", for_="age_group"),
                    Span(" *", class_="text-red-500"),
                    Select(
                        Option("Select your age group", value="", disabled=True, selected=True),
                        Option("18-25"),
                        Option("26-35"),
                        Option("36-45"),
                        Option("46+"),
                        id="age_group",
                        name="age_group",
                        aria_invalid="true",
                        aria_describedby="age_group-error"
                    ),
                    FormError("Please select your age group", id="age_group-error")
                ),
                
                class_="max-w-2xl mx-auto p-8"
            )
        )
    ).render()


# Example 3: Air Form Integration
class ContactModel(BaseModel):
    """Contact form model using Pydantic."""
    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    phone: str = Field(default="", pattern=r"^(\+\d{1,3}[- ]?)?\d{10}$|^$")
    subject: str = Field(..., min_length=5, max_length=200)
    message: str = Field(..., min_length=10, max_length=1000)
    newsletter: bool = Field(default=False)
    
    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "phone": "+1234567890",
                "subject": "Question about EidosUI",
                "message": "I would like to know more about form handling...",
                "newsletter": True
            }
        }


class ContactForm(air.AirForm):
    """Contact form using Air."""
    model = ContactModel


@app.page
def air_form_example():
    """Demonstrate Air form integration with EidosUI styling."""
    # Create form instance
    contact_form = ContactForm()
    
    # Wrap with EidosUI styling
    eidos_form = EidosForm(contact_form)
    
    return Html(
        Head(
            Title("EidosUI Forms - Air Integration"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Contact Form - Air Integration"),
                P(
                    "This form uses Air's form handling with EidosUI styling. ",
                    "The form is powered by Pydantic for validation.",
                    class_="mb-6"
                ),
                
                # Render the styled Air form
                eidos_form.render(),
                
                # Submit button
                Button("Send Message", type="submit", class_=(styles.buttons.primary,"mt-4")),
                
                class_="max-w-2xl mx-auto p-8"
            )
        )
    ).render()


@app.post("/air-form")
async def handle_air_form(request: dict):
    """Handle Air form submission."""
    # Create form instance
    contact_form = ContactForm()
    
    # Validate the form data
    is_valid = contact_form.validate(request)
    
    # Wrap with EidosUI styling
    eidos_form = EidosForm(contact_form)
    
    return Html(
        Head(
            Title("EidosUI Forms - Air Integration"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Contact Form - Air Integration"),
                
                # Show success or render form with errors
                (
                    Div(
                        H2("Success!", class_="text-green-600"),
                        P("Your message has been sent successfully."),
                        Pre(str(request), class_="mt-4 p-4 bg-gray-100 rounded"),
                        A("Submit another form", href="/air-form", class_="text-blue-600 underline"),
                        class_="p-4 bg-green-50 rounded-lg"
                    )
                    if is_valid
                    else Div(
                        P(
                            "Please correct the errors below:",
                            class_="mb-4 text-red-600"
                        ),
                        eidos_form.render(),
                        Button("Send Message", type="submit", class_=(styles.buttons.primary,"mt-4"))
                    )
                ),
                
                class_="max-w-2xl mx-auto p-8"
            )
        )
    ).render()


# Example 4: Complex form layouts
@app.page
def form_layouts():
    """Demonstrate complex form layouts."""
    return Html(
        Head(
            Title("EidosUI Forms - Layouts"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Complex Form Layouts"),
                
                # Two-column layout
                H2("Billing Information", class_="mt-8 mb-4"),
                Div(
                    Div(
                        Label("First Name:", for_="first_name"),
                        Span(" *", class_="text-red-500"),
                        Input(id="first_name", name="first_name", required=True),
                        class_="eidos-form-col"
                    ),
                    Div(
                        Label("Last Name:", for_="last_name"),
                        Span(" *", class_="text-red-500"),
                        Input(id="last_name", name="last_name", required=True),
                        class_="eidos-form-col"
                    ),
                    class_="eidos-form-row"
                ),
                
                # Three-column layout
                Div(
                    Div(
                        Label("City:", for_="city"),
                        Span(" *", class_="text-red-500"),
                        Input(id="city", name="city", required=True),
                        class_="eidos-form-col"
                    ),
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
                            name="state"
                        ),
                        class_="eidos-form-col"
                    ),
                    Div(
                        Label("ZIP Code:", for_="zip"),
                        Span(" *", class_="text-red-500"),
                        Input(id="zip", name="zip", required=True),
                        class_="eidos-form-col"
                    ),
                    class_="eidos-form-row"
                ),
                
                # Input groups
                H2("Input Groups", class_="mt-8 mb-4"),
                Div(
                    Label("Price:", for_="price"),
                    Div(
                        Span("$", class_="eidos-input-addon"),
                        NumberInput(id="price", name="price", placeholder="0.00"),
                        Span(".00", class_="eidos-input-addon"),
                        class_="eidos-input-group"
                    )
                ),
                
                Div(
                    Label("Website:", for_="website"),
                    Div(
                        Span("https://", class_="eidos-input-addon"),
                        Input(id="website", name="website", placeholder="example.com"),
                        class_="eidos-input-group"
                    )
                ),
                
                Button("Save Information", type="submit", class_=(styles.buttons.primary,"mt-4")),
                
                class_="max-w-4xl mx-auto p-8"
            )
        )
    ).render()


@app.page
def index():
    """Forms example index page."""
    return Html(
        Head(
            Title("EidosUI Forms Examples"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("EidosUI Forms Examples"),
                P("Explore different form component examples:", class_="mb-6"),
                
                Div(
                    A(
                        "Basic Form Components",
                        href=basic_form.url(),
                        class_="block p-4 mb-4 bg-blue-50 hover:bg-blue-100 rounded-lg"
                    ),
                    A(
                        "Form with Validation Errors",
                        href=form_with_errors.url(),
                        class_="block p-4 mb-4 bg-red-50 hover:bg-red-100 rounded-lg"
                    ),
                    A(
                        "Air Form Integration",
                        href=air_form_example.url(),
                        class_="block p-4 mb-4 bg-green-50 hover:bg-green-100 rounded-lg"
                    ),
                    A(
                        "Complex Form Layouts",
                        href=form_layouts.url(),
                        class_="block p-4 mb-4 bg-purple-50 hover:bg-purple-100 rounded-lg"
                    ),
                ),
                
                class_="max-w-2xl mx-auto p-8"
            )
        )
    ).render()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)