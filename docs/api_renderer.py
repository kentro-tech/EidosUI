"""Render API documentation using EidosUI components"""

from air.tags import A, Code, Div, H1, H2, H3, H4, Li, P, Pre, Section, Span, Table, Tbody, Td, Th, Thead, Tr, Ul
from eidos.tags import *
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

def render_source_link(func_info: Dict[str, Any], module_name: str) -> Any:
    """Render source code link"""
    # Only show for local functions
    if not func_info.get('is_local', True):
        return None
    
    # Construct GitHub-style link (you can customize this)
    file_path = module_name.replace('.', '/') + '.py'
    
    return A(
        "View source",
        href=f"#source:{file_path}:{func_info['name']}",
        style="color: var(--color-primary); font-size: 0.875rem; float: right; text-decoration: none;"
    )

def render_parameters(params: List[Dict[str, Any]]) -> Any:
    """Render function parameters"""
    if not params:
        return None
    
    param_rows = []
    for param in params:
        # Build parameter description
        param_name = Code(
            param['name'], 
            style="font-family: monospace; font-size: 0.875rem; background-color: var(--color-surface); padding: 0.125rem 0.25rem; border-radius: 0.25rem;"
        )
        
        type_info = []
        if param['annotation']:
            type_info.append(Span(param['annotation'], style="color: var(--color-text-muted); font-style: italic; font-size: 0.875rem;"))
        
        default_info = []
        if param['default'] is not None:
            default_info.append(Span(f"default: {param['default']}", style="color: var(--color-text-subtle); font-size: 0.875rem;"))
        
        param_rows.append(
            Tr(
                Td(param_name, style="padding: 0.5rem 1rem; vertical-align: top;"),
                Td(
                    Div(*type_info) if type_info else "",
                    style="padding: 0.5rem 1rem;"
                ),
                Td(
                    Div(*default_info) if default_info else "",
                    style="padding: 0.5rem 1rem;"
                ),
                style="border-bottom: 1px solid var(--color-border);"
            )
        )
    
    return Div(
        H4("Parameters", style="font-weight: 600; font-size: 1.125rem; margin-top: 1.5rem; margin-bottom: 0.75rem;"),
        Table(
            Thead(
                Tr(
                    Th("Name", style="padding: 0.5rem 1rem; text-align: left; font-weight: 500; color: var(--color-text-muted);"),
                    Th("Type", style="padding: 0.5rem 1rem; text-align: left; font-weight: 500; color: var(--color-text-muted);"),
                    Th("Default", style="padding: 0.5rem 1rem; text-align: left; font-weight: 500; color: var(--color-text-muted);"),
                    style="border-bottom: 2px solid var(--color-border);"
                )
            ),
            Tbody(*param_rows),
            style="width: 100%; border-collapse: collapse;"
        ),
        style="margin-bottom: 1.5rem;"
    )

def render_docstring_section(title: str, content: str) -> Any:
    """Render a docstring section"""
    # Parse parameter lists in docstring sections
    if title in ['Args', 'Arguments', 'Parameters'] and '\n' in content:
        items = []
        for line in content.split('\n'):
            line = line.strip()
            if line and ':' in line:
                param, desc = line.split(':', 1)
                items.append(
                    Li(
                        Code(param.strip(), style="font-family: monospace; font-size: 0.875rem; background-color: var(--color-surface); padding: 0.125rem 0.25rem; border-radius: 0.25rem;"),
                        Span(f": {desc.strip()}", style="margin-left: 0.5rem;")
                    )
                )
            elif line:
                items.append(Li(line))
        
        return Div(
            H4(title, style="font-weight: 600; font-size: 1.125rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
            Ul(*items, style="list-style: disc; list-style-position: inside; space-y: 0.25rem;"),
            style="margin-bottom: 1rem;"
        )
    
    # Format code examples
    if title in ['Example', 'Examples']:
        # Try to extract code blocks
        code_match = re.search(r'```(\w*)\n(.*?)\n```', content, re.DOTALL)
        if code_match:
            code = code_match.group(2)
            return Div(
                H4(title, style="font-weight: 600; font-size: 1.125rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                Pre(Code(code, class_="language-python"), style="background-color: var(--color-surface-elevated); color: var(--color-text); padding: 1rem; border-radius: 0.25rem; overflow-x: auto;"),
                style="margin-bottom: 1rem;"
            )
        else:
            # Check if the content looks like code
            if any(keyword in content for keyword in ['>>>', 'def ', 'class ', 'import ', 'from ']):
                return Div(
                    H4(title, style="font-weight: 600; font-size: 1.125rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                    Pre(Code(content, class_="language-python"), style="background-color: var(--color-surface-elevated); color: var(--color-text); padding: 1rem; border-radius: 0.25rem; overflow-x: auto;"),
                    style="margin-bottom: 1rem;"
                )
    
    # Default rendering
    return Div(
        H4(title, style="font-weight: 600; font-size: 1.125rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
        P(content, style="color: var(--color-text); line-height: 1.5;"),
        style="margin-bottom: 1rem;"
    )

def render_function(func_info: Dict[str, Any], module_name: str = "") -> Any:
    """Render a function documentation"""
    elements = []
    
    # Function header with source link
    header_elements = [
        H3(
            *format_signature(func_info['name'], func_info['signature']),
            id=f"func-{func_info['name']}",
            style="font-size: 1.25rem; font-family: monospace; margin-bottom: 0.5rem;"
        )
    ]
    
    source_link = render_source_link(func_info, module_name)
    if source_link:
        header_elements.append(source_link)
    
    elements.append(
        Div(*header_elements, style="margin-bottom: 1rem; overflow: hidden;")
    )
    
    # Parse and render docstring
    if func_info['doc']:
        parsed_doc = parse_docstring(func_info['doc'])
        
        # Main description
        if parsed_doc['description']:
            elements.append(
                P(parsed_doc['description'], style="color: var(--color-text); line-height: 1.5; margin-bottom: 1rem;")
            )
        
        # Render docstring sections
        for section_title, section_content in parsed_doc['sections'].items():
            if section_title not in ['Args', 'Arguments', 'Parameters']:  # We handle params separately
                elements.append(render_docstring_section(section_title, section_content))
    
    # Parameters (from signature, not docstring)
    if func_info['params']:
        elements.append(render_parameters(func_info['params']))
    
    # Return type
    if func_info.get('return_annotation'):
        elements.append(
            Div(
                H4("Returns", style="font-weight: 600; font-size: 1.125rem; margin-top: 1rem; margin-bottom: 0.5rem;"),
                P(
                    Code(func_info['return_annotation'], style="font-family: monospace; font-size: 0.875rem; background-color: var(--color-surface); padding: 0.25rem 0.5rem; border-radius: 0.25rem;"),
                    style="color: var(--color-text);"
                ),
                style="margin-bottom: 1rem;"
            )
        )
    
    return Div(
        *elements,
        style="border-left: 4px solid var(--color-primary); padding-left: 1.5rem; margin-bottom: 2rem;"
    )

def render_class(class_info: Dict[str, Any], module_name: str = "") -> Any:
    """Render a class documentation"""
    elements = []
    
    # Class header
    class_title = [
        Span("class ", style="color: var(--color-text-muted);"),
        Span(class_info['name'], style="color: var(--color-primary); font-weight: 600;")
    ]
    
    if class_info.get('bases'):
        class_title.extend([
            Span("(", style="color: var(--color-text);"),
            Span(', '.join(class_info['bases']), style="color: var(--color-text-muted); font-style: italic;"),
            Span(")", style="color: var(--color-text);")
        ])
    
    elements.append(
        H3(*class_title, id=f"class-{class_info['name']}", style="font-size: 1.25rem; font-family: monospace; margin-bottom: 0.5rem;")
    )
    
    # Class docstring
    if class_info['doc']:
        parsed_doc = parse_docstring(class_info['doc'])
        if parsed_doc['description']:
            elements.append(
                P(parsed_doc['description'], style="color: var(--color-text); line-height: 1.5; margin-bottom: 1rem;")
            )
        
        for section_title, section_content in parsed_doc['sections'].items():
            elements.append(render_docstring_section(section_title, section_content))
    
    # Methods
    if class_info['methods']:
        elements.append(H4("Methods", style="font-weight: 600; font-size: 1.125rem; margin-top: 1.5rem; margin-bottom: 1rem;"))
        
        method_elements = []
        for method in class_info['methods']:
            method_name = method['name']
            decorators = []
            
            if method.get('is_classmethod'):
                decorators.append(Span("@classmethod", style="color: var(--color-success); font-size: 0.875rem; display: block;"))
            
            # Method signature
            method_header = Div(
                *decorators,
                Div(
                    *format_signature(method_name, method['signature']),
                    style="font-family: monospace;"
                ),
                style="margin-bottom: 0.5rem;"
            )
            
            method_content = [method_header]
            
            # Method docstring
            if method['doc']:
                parsed_doc = parse_docstring(method['doc'])
                if parsed_doc['description']:
                    method_content.append(
                        Div(
                            P(parsed_doc['description'], style="color: var(--color-text-muted); font-size: 0.875rem; margin-bottom: 0.5rem; margin-left: 1rem;")
                        )
                    )
            
            method_elements.append(
                Div(*method_content, style="margin-bottom: 1.5rem; background-color: var(--color-surface); padding: 1rem; border-radius: 0.25rem;")
            )
        
        elements.extend(method_elements)
    
    return Div(
        *elements,
        style="border-left: 4px solid var(--color-accent); padding-left: 1.5rem; margin-bottom: 2rem;"
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
                style="margin-bottom: 2rem; padding: 1.5rem; background-color: var(--color-primary-light); border-radius: 0.5rem; border: 1px solid var(--color-border);"
            )
        )
    
    # Table of contents
    toc_items = []
    if api_data['constants']:
        toc_items.append(
            Li(
                A("Constants", href="#constants", style="color: var(--color-primary); text-decoration: none;"),
                Span(f" ({len(api_data['constants'])})", style="color: var(--color-text-subtle); font-size: 0.875rem; margin-left: 0.25rem;")
            )
        )
    if api_data['functions']:
        toc_items.append(
            Li(
                A("Functions", href="#functions", style="color: var(--color-primary); text-decoration: none;"),
                Span(f" ({len(api_data['functions'])})", style="color: var(--color-text-subtle); font-size: 0.875rem; margin-left: 0.25rem;")
            )
        )
    if api_data['classes']:
        toc_items.append(
            Li(
                A("Classes", href="#classes", style="color: var(--color-primary); text-decoration: none;"),
                Span(f" ({len(api_data['classes'])})", style="color: var(--color-text-subtle); font-size: 0.875rem; margin-left: 0.25rem;")
            )
        )
    
    if toc_items:
        elements.append(
            Div(
                H2("Contents", style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.75rem;"),
                Ul(*toc_items, style="list-style: disc; list-style-position: inside; space-y: 0.5rem;"),
                style="margin-bottom: 2rem; padding: 1rem; background-color: var(--color-surface); border-radius: 0.5rem;"
            )
        )
    
    # Constants section
    if api_data['constants']:
        const_elements = []
        for const in api_data['constants']:
            const_elements.append(
                Div(
                    Code(const['name'], style="font-family: monospace; color: var(--color-primary); font-weight: 600;"),
                    Span(" = ", style="color: var(--color-text);"),
                    Code(const['value'], style="font-family: monospace; color: var(--color-success);"),
                    Span(f"  # {const['type']}", style="color: var(--color-text-subtle); font-style: italic; font-size: 0.875rem; margin-left: 0.5rem;"),
                    style="margin-bottom: 0.5rem;"
                )
            )
        
        elements.append(
            Section(
                H2("Constants", id="constants", style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--color-border);"),
                Div(*const_elements, style="space-y: 0.5rem;"),
                style="margin-bottom: 3rem;"
            )
        )
    
    # Functions section
    if api_data['functions']:
        elements.append(
            Section(
                H2("Functions", id="functions", style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--color-border);"),
                *[render_function(func, module_name) for func in api_data['functions']],
                style="margin-bottom: 3rem;"
            )
        )
    
    # Classes section
    if api_data['classes']:
        elements.append(
            Section(
                H2("Classes", id="classes", style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; padding-bottom: 0.5rem; border-bottom: 1px solid var(--color-border);"),
                *[render_class(cls, module_name) for cls in api_data['classes']],
                style="margin-bottom: 3rem;"
            )
        )
    
    return Div(*elements, style="max-width: 80rem; margin: 0 auto;")

def render_api_index(modules: List[str]) -> Any:
    """Render API index page"""
    module_groups = {}
    
    # Group modules by parent
    for module in modules:
        parts = module.split('.')
        if len(parts) > 2:
            parent = '.'.join(parts[:2])
        else:
            parent = parts[0]
        
        if parent not in module_groups:
            module_groups[parent] = []
        module_groups[parent].append(module)
    
    group_elements = []
    for parent, mods in sorted(module_groups.items()):
        module_links = []
        
        for module in sorted(mods):
            parts = module.split('.')
            display_name = '.'.join(parts[2:]) if len(parts) > 2 else parts[-1]
            
            module_links.append(
                Li(
                    A(
                        Code(display_name, style="font-family: monospace;"),
                        href=f"/api/{module}",
                        style="color: var(--color-primary); text-decoration: none;"
                    ),
                    style="margin-bottom: 0.5rem;"
                )
            )
        
        group_elements.append(
            Div(
                H3(parent, style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.5rem;"),
                Ul(*module_links, style="list-style: disc; list-style-position: inside; margin-left: 1rem;"),
                style="margin-bottom: 1.5rem;"
            )
        )
    
    return Div(
        H1("API Reference", style="font-size: 1.875rem; font-weight: bold; margin-bottom: 0.5rem;"),
        P("Complete API documentation for EidosUI modules", style="font-size: 1.25rem; color: var(--color-text-muted); margin-bottom: 2rem;"),
        
        Div(
            *group_elements,
            style="space-y: 1.5rem;"
        ),
        style="max-width: 64rem; margin: 0 auto;"
    )