"""Render API documentation using EidosUI components"""

from air.tags import A, Code, Div, H1, H3, H4, Li, P, Pre, Span, Ul
from typing import Dict, Any, List
import re

def parse_docstring(docstring: str) -> Dict[str, Any]:
    """Parse docstring into sections"""
    if not docstring:
        return {'description': '', 'sections': {}}
    
    lines = docstring.strip().split('\n')
    description = []
    sections = {}
    current_section = None
    current_content = []
    
    for line in lines:
        # Check for section headers (Args:, Returns:, etc.)
        if line.strip() and line.strip().endswith(':') and line.strip()[:-1] in ['Args', 'Arguments', 'Parameters', 'Returns', 'Return', 'Yields', 'Raises', 'Note', 'Notes', 'Example', 'Examples']:
            if current_section:
                sections[current_section] = '\n'.join(current_content).strip()
            current_section = line.strip()[:-1]
            current_content = []
        elif current_section:
            current_content.append(line)
        else:
            description.append(line)
    
    if current_section:
        sections[current_section] = '\n'.join(current_content).strip()
    
    return {
        'description': '\n'.join(description).strip(),
        'sections': sections
    }

def format_signature(name: str, signature: str) -> List[Any]:
    """Format function signature with proper syntax highlighting"""
    # Parse the signature to identify components
    sig_match = re.match(r'\((.*?)\)\s*(?:->\s*(.+))?', signature)
    
    if not sig_match:
        return [Span(name, style="color: var(--color-primary); font-weight: 600;"), Span(signature, style="color: var(--color-text);")]
    
    params_str = sig_match.group(1)
    return_type = sig_match.group(2)
    
    # Build formatted signature
    elements = [
        Span(name, style="color: var(--color-primary); font-weight: 600;"),
        Span("(", style="color: var(--color-text);")
    ]
    
    if params_str:
        # Split parameters
        params = []
        depth = 0
        current = []
        for char in params_str:
            if char in '([{':
                depth += 1
            elif char in ')]}':
                depth -= 1
            elif char == ',' and depth == 0:
                params.append(''.join(current).strip())
                current = []
                continue
            current.append(char)
        if current:
            params.append(''.join(current).strip())
        
        # Format each parameter
        for i, param in enumerate(params):
            if ':' in param:
                name_part, type_part = param.split(':', 1)
                elements.extend([
                    Span(name_part.strip(), style="color: var(--color-accent);"),
                    Span(": ", style="color: var(--color-text);"),
                    Span(type_part.strip(), style="color: var(--color-text-muted); font-style: italic;")
                ])
            else:
                elements.append(Span(param, style="color: var(--color-accent);"))
            
            if i < len(params) - 1:
                elements.append(Span(", ", style="color: var(--color-text);"))
    
    elements.append(Span(")", style="color: var(--color-text);"))
    
    if return_type:
        elements.extend([
            Span(" → ", style="color: var(--color-text);"),
            Span(return_type, style="color: var(--color-text-muted); font-style: italic;")
        ])
    
    return elements

def render_item(item: Dict[str, Any], item_type: str, module_name: str) -> Any:
    """Render a single API item (function, class, or constant)"""
    elements = []
    
    # Constants
    if item_type == 'constant':
        return Div(
            Code(item['name'], style="font-family: monospace; color: var(--color-primary); font-weight: 600;"),
            Span(" = ", style="color: var(--color-text);"),
            Code(item['value'], style="font-family: monospace; color: var(--color-success);"),
            Span(f"  # {item['type']}", style="color: var(--color-text-subtle); font-style: italic; font-size: 0.875rem; margin-left: 0.5rem;"),
            style="margin-bottom: 1.5rem;"
        )
    
    # Functions and Classes
    if item_type == 'function':
        # Function header with GitHub link
        header = H3(
            *format_signature(item['name'], item['signature']),
            id=f"func-{item['name']}",
            style="font-size: 1.25rem; font-family: monospace; margin-bottom: 0.5rem;"
        )
        
        if item.get('is_local', True):
            # GitHub link
            file_path = module_name.replace('.', '/') + '.py'
            github_link = A(
                "View on GitHub",
                href=f"https://github.com/kentro-tech/eidosui/blob/main/{file_path}",
                target="_blank",
                style="color: var(--color-primary); font-size: 0.875rem; float: right; text-decoration: none;"
            )
            elements.append(Div(header, github_link, style="overflow: hidden; margin-bottom: 1rem;"))
        else:
            elements.append(header)
        
        border_color = "var(--color-primary)"
    
    elif item_type == 'class':
        # Class header
        class_title = [
            Span("class ", style="color: var(--color-text-muted);"),
            Span(item['name'], style="color: var(--color-primary); font-weight: 600;")
        ]
        
        if item.get('bases'):
            class_title.extend([
                Span("(", style="color: var(--color-text);"),
                Span(', '.join(item['bases']), style="color: var(--color-text-muted); font-style: italic;"),
                Span(")", style="color: var(--color-text);")
            ])
        
        header = H3(*class_title, id=f"class-{item['name']}", style="font-size: 1.25rem; font-family: monospace; margin-bottom: 0.5rem;")
        
        if item.get('is_local', True):
            # GitHub link
            file_path = module_name.replace('.', '/') + '.py'
            github_link = A(
                "View on GitHub",
                href=f"https://github.com/kentro-tech/eidosui/blob/main/{file_path}",
                target="_blank",
                style="color: var(--color-primary); font-size: 0.875rem; float: right; text-decoration: none;"
            )
            elements.append(Div(header, github_link, style="overflow: hidden; margin-bottom: 1rem;"))
        else:
            elements.append(header)
        
        border_color = "var(--color-accent)"
    
    # Docstring
    if item.get('doc'):
        parsed_doc = parse_docstring(item['doc'])
        
        # Main description
        if parsed_doc['description']:
            elements.append(
                P(parsed_doc['description'], style="color: var(--color-text); line-height: 1.5; margin-bottom: 1rem;")
            )
        
        # Docstring sections
        for section_title, section_content in parsed_doc['sections'].items():
            # Format code examples
            if section_title in ['Example', 'Examples']:
                elements.append(
                    Div(
                        H4(section_title, style="font-weight: 600; font-size: 1rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                        Pre(Code(section_content, class_="language-python"), 
                            style="background-color: var(--color-surface-elevated); color: var(--color-text); padding: 1rem; border-radius: 0.25rem; overflow-x: auto;"),
                        style="margin-bottom: 1rem;"
                    )
                )
            else:
                elements.append(
                    Div(
                        H4(section_title, style="font-weight: 600; font-size: 1rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                        P(section_content, style="color: var(--color-text); line-height: 1.5;"),
                        style="margin-bottom: 1rem;"
                    )
                )
    
    # Parameters (for functions)
    if item_type == 'function' and item.get('params'):
        param_items = []
        for param in item['params']:
            param_elements = [Code(param['name'], style="font-family: monospace; background-color: var(--color-surface); padding: 0.125rem 0.25rem; border-radius: 0.25rem;")]
            
            if param['annotation']:
                param_elements.append(Span(f": {param['annotation']}", style="color: var(--color-text-muted); font-style: italic; font-size: 0.875rem; margin-left: 0.25rem;"))
            
            if param['default'] is not None:
                param_elements.append(Span(f" = {param['default']}", style="color: var(--color-text-subtle); font-size: 0.875rem;"))
            
            param_items.append(Li(*param_elements))
        
        if param_items:
            elements.append(
                Div(
                    H4("Parameters", style="font-weight: 600; font-size: 1rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                    Ul(*param_items, style="list-style: none; padding-left: 1rem;"),
                    style="margin-bottom: 1rem;"
                )
            )
    
    # Return type (for functions)
    if item_type == 'function' and item.get('return_annotation'):
        elements.append(
            Div(
                H4("Returns", style="font-weight: 600; font-size: 1rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                P(
                    Code(item['return_annotation'], style="font-family: monospace; font-size: 0.875rem; background-color: var(--color-surface); padding: 0.25rem 0.5rem; border-radius: 0.25rem;"),
                    style="color: var(--color-text);"
                ),
                style="margin-bottom: 1rem;"
            )
        )
    
    # Methods (for classes)
    if item_type == 'class' and item.get('methods'):
        elements.append(H4("Methods", style="font-weight: 600; font-size: 1.125rem; margin-top: 1.5rem; margin-bottom: 1rem;"))
        
        for method in item['methods']:
            method_elements = []
            
            # Method signature
            if method.get('is_classmethod'):
                method_elements.append(Span("@classmethod", style="color: var(--color-success); font-size: 0.875rem; display: block;"))
            
            method_elements.append(
                Div(
                    *format_signature(method['name'], method['signature']),
                    style="font-family: monospace; margin-bottom: 0.5rem;"
                )
            )
            
            # Method docstring
            if method['doc']:
                method_elements.append(
                    P(method['doc'].split('\n')[0], style="color: var(--color-text-muted); font-size: 0.875rem; margin-left: 1rem;")
                )
            
            elements.append(
                Div(*method_elements, style="margin-bottom: 1rem; background-color: var(--color-surface); padding: 1rem; border-radius: 0.25rem;")
            )
    
    return Div(
        *elements,
        style=f"border-left: 4px solid {border_color}; padding-left: 1.5rem; margin-bottom: 2rem;"
    )

def render_api_page(api_data: Dict[str, Any]) -> Any:
    """Render complete API documentation page"""
    if 'error' in api_data:
        return Div(
            H1("API Reference Error", style="font-size: 1.875rem; font-weight: bold; margin-bottom: 1rem;"),
            P(api_data['error'], style="color: var(--color-error);")
        )
    
    elements = []
    
    # Module title and description
    module_name = api_data['module']
    elements.append(
        Div(
            H1(f"{module_name}", style="font-size: 1.875rem; font-weight: bold; margin-bottom: 0.5rem;"),
            P("API Reference", style="font-size: 1.25rem; color: var(--color-text-muted); margin-bottom: 1.5rem;")
        )
    )
    
    if api_data['doc']:
        elements.append(
            Div(
                P(api_data['doc'], style="font-size: 1.125rem; line-height: 1.5;"),
                style="margin-bottom: 2rem; padding: 1.5rem; background-color: var(--color-surface); border-radius: 0.5rem; border: 1px solid var(--color-border);"
            )
        )
    
    # Combine all items and sort by source order (would need line numbers from extractor)
    # For now, show in order: constants, functions, classes
    all_items = []
    
    for const in api_data.get('constants', []):
        all_items.append(('constant', const))
    
    for func in api_data.get('functions', []):
        all_items.append(('function', func))
    
    for cls in api_data.get('classes', []):
        all_items.append(('class', cls))
    
    # Render all items
    for item_type, item in all_items:
        elements.append(render_item(item, item_type, module_name))
    
    return Div(*elements, style="max-width: 80rem; margin: 0 auto; padding: 2rem;")

def render_api_index(modules: List[str]) -> Any:
    """Render API index page"""
    module_links = []
    
    for module in sorted(modules):
        module_links.append(
            Li(
                A(
                    Code(module, style="font-family: monospace;"),
                    href=f"/api/{module}",
                    style="color: var(--color-primary); text-decoration: none;"
                ),
                style="margin-bottom: 0.5rem;"
            )
        )
    
    return Div(
        H1("API Reference", style="font-size: 1.875rem; font-weight: bold; margin-bottom: 0.5rem;"),
        P("Complete API documentation for EidosUI modules", style="font-size: 1.25rem; color: var(--color-text-muted); margin-bottom: 2rem;"),
        
        Ul(*module_links, style="list-style: none; padding: 0;"),
        style="max-width: 64rem; margin: 0 auto; padding: 2rem;"
    )