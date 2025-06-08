#!/usr/bin/env python3
"""Basic test to verify EidosUI functionality"""

from eidos import (
    H1, H2, H3, Text, Button, Card, Container, Grid, Input, Label, FormGroup,
    button_styles, card_styles, layout_styles, typography_styles, theme_manager
)


def test_components():
    """Test basic component creation"""
    
    # Test typography components
    h1 = H1("Hello World")
    h2 = H2("Subtitle", cls=typography_styles.h2)
    text = Text("This is some body text", cls=typography_styles.body)
    
    print("✅ Typography components created successfully")
    
    # Test button with different styles
    primary_btn = Button("Primary", cls=button_styles.primary)
    secondary_btn = Button("Secondary", cls=button_styles.secondary)
    ghost_btn = Button("Ghost", cls=button_styles.ghost)
    
    print("✅ Button components created successfully")
    
    # Test layout components
    card = Card(
        H2("Card Title"),
        Text("Card content goes here"),
        cls=card_styles.default,
        padding_cls=card_styles.comfortable
    )
    
    grid = Grid(
        card,
        Card("Card 2", cls=card_styles.elevated),
        Card("Card 3", cls=card_styles.flat),
        cls=layout_styles.grid_responsive
    )
    
    container = Container(
        grid,
        size_cls=layout_styles.container_lg,
        cls=layout_styles.stack_md
    )
    
    print("✅ Layout components created successfully")
    
    # Test form components
    form = FormGroup(
        Label("Email"),
        Input(type="email", placeholder="Enter email"),
        Button("Submit", cls=button_styles.primary)
    )
    
    print("✅ Form components created successfully")
    
    # Test theme manager
    css_var = theme_manager.get_css_var("color-primary")
    assert css_var == "var(--color-primary)"
    
    print("✅ Theme manager working correctly")


def test_page_creation():
    """Test creating a complete page"""
    
    page = Container(
        H1("EidosUI Test Page"),
        
        # Hero section
        Card(
            H2("Welcome to EidosUI"),
            Text("A modern, flexible UI library for Python"),
            Button("Get Started", cls=button_styles.primary),
            cls=card_styles.elevated,
            padding_cls="p-8 text-center"
        ),
        
        # Feature grid
        Grid(
            Card(
                H3("🎨 Themeable"),
                Text("Built-in light/dark themes"),
                cls=card_styles.default
            ),
            Card(
                H3("📱 Responsive"),
                Text("Mobile-first design"),
                cls=card_styles.default
            ),
            Card(
                H3("🔧 Flexible"),
                Text("Use our styles or custom classes"),
                cls=card_styles.default
            ),
            cls=layout_styles.grid_responsive
        ),
        
        # Contact form
        Card(
            H2("Contact Form"),
            FormGroup(
                Label("Name"),
                Input(placeholder="Your name", required=True)
            ),
            FormGroup(
                Label("Message"),
                Input(placeholder="Your message", required=True)
            ),
            Button("Send", cls=button_styles.primary),
            cls=card_styles.default,
            padding_cls="p-6 max-w-md mx-auto"
        ),
        
        cls=layout_styles.stack_xl,
        size_cls=layout_styles.container_lg
    )
    
    print("✅ Complete page created successfully")
    return page


if __name__ == "__main__":
    print("🚀 Testing EidosUI...")
    
    test_components()
    test_page_creation()
    
    print("\n🎉 All tests passed! EidosUI is working correctly.")
    print("\n📖 Key features tested:")
    print("   • Typography components (H1, H2, Text)")
    print("   • Button variations (primary, secondary, ghost)")
    print("   • Layout components (Card, Container, Grid)")
    print("   • Form components (Input, Label, FormGroup)")
    print("   • Style dataclasses integration")
    print("   • Theme manager functionality")
    print("   • Complete page composition")
    print("\n✨ Ready for development!") 