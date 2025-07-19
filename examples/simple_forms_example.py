"""Simple EidosUI form example using styled tags."""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from eidos import *
from eidos.utils import get_eidos_static_files

# Create FastAPI app
app = FastAPI()

# Mount static files
for mount_path, directory in get_eidos_static_files().items():
    app.mount(mount_path, StaticFiles(directory=directory), name=mount_path.strip("/"))


@app.get("/", response_class=HTMLResponse)
def index():
    """Simple form example using EidosUI styled tags."""
    return Html(
        Head(
            Title("EidosUI Simple Forms"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Simple EidosUI Forms"),
                P("Using styled form tags directly without complex components:"),
                
                # Simple form
                air.Form(
                    Fieldset(
                        air.Legend("User Information"),
                        
                        # Text input with label
                        Label("Name:", for_="name"),
                        Input(id="name", name="name", placeholder="Enter your name"),
                        
                        # Email input
                        Label("Email:", for_="email", class_="mt-4"),
                        EmailInput(id="email", name="email", placeholder="name@example.com"),
                        
                        # Password input
                        Label("Password:", for_="password", class_="mt-4"),
                        PasswordInput(id="password", name="password"),
                        FormHelp("Must be at least 8 characters"),
                        
                        # Number input
                        Label("Age:", for_="age", class_="mt-4"),
                        NumberInput(id="age", name="age", min="18", max="120"),
                        
                        # Date picker
                        Label("Birth Date:", for_="birthdate", class_="mt-4"),
                        DatePicker(id="birthdate", name="birthdate"),
                        
                        # Time picker
                        Label("Preferred Time:", for_="time", class_="mt-4"),
                        TimePicker(id="time", name="time"),
                        
                        # Color picker
                        Label("Favorite Color:", for_="color", class_="mt-4"),
                        ColorPicker(id="color", name="color", value="#3b82f6"),
                        
                        # URL input
                        Label("Website:", for_="website", class_="mt-4"),
                        UrlInput(id="website", name="website", placeholder="https://example.com"),
                        
                        # Phone input
                        Label("Phone:", for_="phone", class_="mt-4"),
                        TelInput(id="phone", name="phone", placeholder="+1 (555) 123-4567"),
                        
                        # Search input
                        Label("Search:", for_="search", class_="mt-4"),
                        SearchInput(id="search", name="search", placeholder="Search..."),
                        
                        # Textarea
                        Label("Comments:", for_="comments", class_="mt-4"),
                        Textarea("", id="comments", name="comments", rows="4", placeholder="Tell us what you think..."),
                        
                        # Select dropdown
                        Label("Country:", for_="country", class_="mt-4"),
                        Select(
                            Option("Select a country", value="", disabled=True, selected=True),
                            Option("United States", value="us"),
                            Option("United Kingdom", value="uk"),
                            Option("Canada", value="ca"),
                            Option("Australia", value="au"),
                            id="country",
                            name="country"
                        ),
                        
                        # Checkboxes
                        H3("Interests", class_="mt-6 mb-3"),
                        Label(
                            Checkbox(id="tech", name="interests", value="tech"),
                            " Technology",
                            class_="eidos-label-inline"
                        ),
                        Label(
                            Checkbox(id="design", name="interests", value="design", checked=True),
                            " Design",
                            class_="eidos-label-inline"
                        ),
                        Label(
                            Checkbox(id="business", name="interests", value="business"),
                            " Business",
                            class_="eidos-label-inline"
                        ),
                        
                        # Radio buttons
                        H3("Subscription", class_="mt-6 mb-3"),
                        Label(
                            Radio(id="free", name="subscription", value="free", checked=True),
                            " Free",
                            class_="eidos-label-inline"
                        ),
                        Label(
                            Radio(id="basic", name="subscription", value="basic"),
                            " Basic ($9/mo)",
                            class_="eidos-label-inline"
                        ),
                        Label(
                            Radio(id="pro", name="subscription", value="pro"),
                            " Pro ($29/mo)",
                            class_="eidos-label-inline"
                        ),
                        
                        # File upload
                        Label("Upload Resume:", for_="resume", class_="mt-6"),
                        FileInput(id="resume", name="resume", accept=".pdf,.doc,.docx"),
                        FormHelp("PDF, DOC, or DOCX files only"),
                    ),
                    
                    # Form with errors example
                    Fieldset(
                        air.Legend("Example with Errors", class_="mt-8"),
                        
                        Label("Username:", for_="username"),
                        Input(id="username", name="username", value="ab", aria_invalid="true"),
                        FormError("Username must be at least 3 characters"),
                        
                        Label("Email:", for_="email2", class_="mt-4"),
                        EmailInput(id="email2", name="email2", value="invalid-email", aria_invalid="true"),
                        FormError("Please enter a valid email address"),
                    ),
                    
                    # Submit button
                    Button("Submit Form", type="submit", class_="mt-6"),
                    
                    method="post",
                    action="/submit",
                    class_="space-y-2"
                ),
                
                class_="max-w-2xl mx-auto p-8"
            )
        )
    ).render()


@app.post("/submit", response_class=HTMLResponse)
def submit_form():
    """Handle form submission."""
    return Html(
        Head(
            Title("Form Submitted"),
            *EidosHeaders(),
        ),
        Body(
            Div(
                H1("Form Submitted Successfully!"),
                P("Thank you for your submission."),
                A("Go back", href="/", class_="text-blue-600 underline"),
                class_="max-w-2xl mx-auto p-8 text-center"
            )
        )
    ).render()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)