from typing import Optional, Literal, Any, Union
import air
from . import styles
from .utils import stringify

def Button(*content: Any, class_: Optional[Union[str, list[str]]] = styles.buttons.primary, **kwargs: Any) -> air.Tag:
    """
    Args:
        content: The content of the button.
        class_: The class of the button.
        **kwargs: Additional keyword arguments passed to the button tag.

    Returns:
        air.Tag: The button tag.

    Example:
        Button("Click me", class_=styles.buttons.primary)
    """
    return air.Button(*content, class_=stringify(styles.buttons.base, class_), **kwargs)

def H1(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    """
    Args:
        content: The content of the h1 tag.
        class_: The class of the h1 tag.
        **kwargs: Additional keyword arguments passed to the h1 tag.

    Returns:
        air.Tag: The h1 tag.

    Example:
        H1("Hello, world!")
    """
    return air.H1(*content, class_=stringify(styles.typography.h1, class_), **kwargs)

def H2(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    """
    Args:
        content: The content of the h2 tag.
        class_: The class of the h2 tag.
        **kwargs: Additional keyword arguments passed to the h2 tag.

    Returns:
        air.Tag: The h2 tag.

    Example:
        H2("Hello, world!")
    """
    return air.H2(*content, class_=stringify(styles.typography.h2, class_), **kwargs)

def H3(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    """
    Args:
        content: The content of the h3 tag.
        class_: The class of the h3 tag.
        **kwargs: Additional keyword arguments passed to the h3 tag.

    Returns:
        air.Tag: The h3 tag.

    Example:
        H3("Hello, world!")
    """
    return air.H3(*content, class_=stringify(styles.typography.h3, class_), **kwargs)

def H4(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H4(*content, class_=stringify(styles.typography.h4, class_), **kwargs)

def H5(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H5(*content, class_=stringify(styles.typography.h5, class_), **kwargs)

def H6(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H6(*content, class_=stringify(styles.typography.h6, class_), **kwargs)

def Body(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Body(*content, class_=stringify(styles.Theme.body, class_), **kwargs)

# Semantic HTML Elements

def Strong(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Strong(*content, class_=stringify(styles.semantic.strong, class_), **kwargs)

def I(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.I(*content, class_=stringify(styles.semantic.i, class_), **kwargs)

def Small(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Small(*content, class_=stringify(styles.semantic.small, class_), **kwargs)

def Del(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Del(*content, class_=stringify(styles.semantic.del_, class_), **kwargs)

def Abbr(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    """
    Args:
        content: The content of the abbr tag.
        class_: The class of the abbr tag.
        **kwargs: Additional keyword arguments passed to the abbr tag.

    Returns:
        air.Tag: The abbr tag.

    Example:
        Abbr("HTML", title="Hyper Text Markup Language")
    """
    return air.Abbr(*content, class_=stringify(styles.semantic.abbr, class_), **kwargs)

def Var(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Var(*content, class_=stringify(styles.semantic.var, class_), **kwargs)

def Mark(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Mark(*content, class_=stringify(styles.semantic.mark, class_), **kwargs)

def Time(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Time(*content, class_=stringify(styles.semantic.time, class_), **kwargs)

def Code(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Code(*content, class_=stringify(styles.semantic.code, class_), **kwargs)

def Pre(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Pre(*content, class_=stringify(styles.semantic.pre, class_), **kwargs)

def Kbd(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Kbd(*content, class_=stringify(styles.semantic.kbd, class_), **kwargs)

def Samp(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Samp(*content, class_=stringify(styles.semantic.samp, class_), **kwargs)

def Blockquote(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Blockquote(*content, class_=stringify(styles.semantic.blockquote, class_), **kwargs)

def Cite(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Cite(*content, class_=stringify(styles.semantic.cite, class_), **kwargs)

def Address(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Address(*content, class_=stringify(styles.semantic.address, class_), **kwargs)

def Hr(class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Hr(class_=stringify(styles.semantic.hr, class_), **kwargs)

def Details(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Details(*content, class_=stringify(styles.semantic.details, class_), **kwargs)

def Summary(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Summary(*content, class_=stringify(styles.semantic.summary, class_), **kwargs)

def Dl(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Dl(*content, class_=stringify(styles.semantic.dl, class_), **kwargs)

def Dt(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Dt(*content, class_=stringify(styles.semantic.dt, class_), **kwargs)

def Dd(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Dd(*content, class_=stringify(styles.semantic.dd, class_), **kwargs)

def Figure(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Figure(*content, class_=stringify(styles.semantic.figure, class_), **kwargs)

def Figcaption(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.Figcaption(*content, class_=stringify(styles.semantic.figcaption, class_), **kwargs)


# Pass-through tags (no default styling)

def A(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through anchor tag"""
    return air.A(*content, **kwargs)

def Area(**kwargs: Any) -> air.Tag:
    """Pass-through area tag"""
    return air.Area(**kwargs)

def Article(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through article tag"""
    return air.Article(*content, **kwargs)

def Aside(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through aside tag"""
    return air.Aside(*content, **kwargs)

def Audio(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through audio tag"""
    return air.Audio(*content, **kwargs)

def B(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through bold tag"""
    return air.B(*content, **kwargs)

def Base(**kwargs: Any) -> air.Tag:
    """Pass-through base tag"""
    return air.Base(**kwargs)

def Bdi(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through bi-directional isolation tag"""
    return air.Bdi(*content, **kwargs)

def Bdo(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through bi-directional override tag"""
    return air.Bdo(*content, **kwargs)

def Br(**kwargs: Any) -> air.Tag:
    """Pass-through line break tag"""
    return air.Br(**kwargs)

def Canvas(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through canvas tag"""
    return air.Canvas(*content, **kwargs)

def Caption(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table caption tag"""
    return air.Caption(*content, **kwargs)

def Col(**kwargs: Any) -> air.Tag:
    """Pass-through column tag"""
    return air.Col(**kwargs)

def Colgroup(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through column group tag"""
    return air.Colgroup(*content, **kwargs)

def Data(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through data tag"""
    return air.Data(*content, **kwargs)

def Datalist(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through datalist tag"""
    return air.Datalist(*content, **kwargs)

def Dfn(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through definition tag"""
    return air.Dfn(*content, **kwargs)

def Dialog(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through dialog tag"""
    return air.Dialog(*content, **kwargs)

def Div(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through div tag"""
    return air.Div(*content, **kwargs)

def Em(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through emphasis tag"""
    return air.Em(*content, **kwargs)

def Embed(**kwargs: Any) -> air.Tag:
    """Pass-through embed tag"""
    return air.Embed(**kwargs)

def Fieldset(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through fieldset tag"""
    return air.Fieldset(*content, **kwargs)

def Footer(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through footer tag"""
    return air.Footer(*content, **kwargs)

def Form(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through form tag"""
    return air.Form(*content, **kwargs)

def Head(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through head tag"""
    return air.Head(*content, **kwargs)

def Header(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through header tag"""
    return air.Header(*content, **kwargs)

def Hgroup(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through heading group tag"""
    return air.Hgroup(*content, **kwargs)

def Html(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through html tag"""
    return air.Html(*content, **kwargs)

def Iframe(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through iframe tag"""
    return air.Iframe(*content, **kwargs)

def Img(**kwargs: Any) -> air.Tag:
    """Pass-through image tag"""
    return air.Img(**kwargs)

def Input(**kwargs: Any) -> air.Tag:
    """Pass-through input tag"""
    return air.Input(**kwargs)

def Ins(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through insertion tag"""
    return air.Ins(*content, **kwargs)

def Label(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through label tag"""
    return air.Label(*content, **kwargs)

def Legend(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through legend tag"""
    return air.Legend(*content, **kwargs)

def Li(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through list item tag"""
    return air.Li(*content, **kwargs)

def Link(**kwargs: Any) -> air.Tag:
    """Pass-through link tag"""
    return air.Link(**kwargs)

def Main(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through main tag"""
    return air.Main(*content, **kwargs)

def Map(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through map tag"""
    return air.Map(*content, **kwargs)

def Menu(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through menu tag"""
    return air.Menu(*content, **kwargs)

def Meta(**kwargs: Any) -> air.Tag:
    """Pass-through meta tag"""
    return air.Meta(**kwargs)

def Meter(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through meter tag"""
    return air.Meter(*content, **kwargs)

def Nav(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through navigation tag"""
    return air.Nav(*content, **kwargs)

def Noscript(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through noscript tag"""
    return air.Noscript(*content, **kwargs)

def Object(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through object tag"""
    return air.Object(*content, **kwargs)

def Ol(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through ordered list tag"""
    return air.Ol(*content, **kwargs)

def Optgroup(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through option group tag"""
    return air.Optgroup(*content, **kwargs)

def Option(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through option tag"""
    return air.Option(*content, **kwargs)

def Output(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through output tag"""
    return air.Output(*content, **kwargs)

def P(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through paragraph tag"""
    return air.P(*content, **kwargs)

def Param(**kwargs: Any) -> air.Tag:
    """Pass-through parameter tag"""
    return air.Param(**kwargs)

def Picture(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through picture tag"""
    return air.Picture(*content, **kwargs)

def Progress(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through progress tag"""
    return air.Progress(*content, **kwargs)

def Q(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through quotation tag"""
    return air.Q(*content, **kwargs)

def Rp(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through ruby parenthesis tag"""
    return air.Rp(*content, **kwargs)

def Rt(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through ruby text tag"""
    return air.Rt(*content, **kwargs)

def Ruby(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through ruby tag"""
    return air.Ruby(*content, **kwargs)

def S(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through strikethrough tag"""
    return air.S(*content, **kwargs)

def Script(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through script tag"""
    return air.Script(*content, **kwargs)

def Search(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through search tag"""
    return air.Search(*content, **kwargs)

def Section(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through section tag"""
    return air.Section(*content, **kwargs)

def Select(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through select tag"""
    return air.Select(*content, **kwargs)

def Source(**kwargs: Any) -> air.Tag:
    """Pass-through source tag"""
    return air.Source(**kwargs)

def Span(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through span tag"""
    return air.Span(*content, **kwargs)

def Style(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through style tag"""
    return air.Style(*content, **kwargs)

def Sub(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through subscript tag"""
    return air.Sub(*content, **kwargs)

def Sup(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through superscript tag"""
    return air.Sup(*content, **kwargs)

def Table(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table tag"""
    return air.Table(*content, **kwargs)

def Tbody(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table body tag"""
    return air.Tbody(*content, **kwargs)

def Td(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table data tag"""
    return air.Td(*content, **kwargs)

def Template(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through template tag"""
    return air.Template(*content, **kwargs)

def Textarea(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through textarea tag"""
    return air.Textarea(*content, **kwargs)

def Tfoot(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table footer tag"""
    return air.Tfoot(*content, **kwargs)

def Th(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table header tag"""
    return air.Th(*content, **kwargs)

def Thead(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table head tag"""
    return air.Thead(*content, **kwargs)

def Title(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through title tag"""
    return air.Title(*content, **kwargs)

def Tr(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through table row tag"""
    return air.Tr(*content, **kwargs)

def Track(**kwargs: Any) -> air.Tag:
    """Pass-through track tag"""
    return air.Track(**kwargs)

def U(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through underline tag"""
    return air.U(*content, **kwargs)

def Ul(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through unordered list tag"""
    return air.Ul(*content, **kwargs)

def Video(*content: Any, **kwargs: Any) -> air.Tag:
    """Pass-through video tag"""
    return air.Video(*content, **kwargs)

def Wbr(**kwargs: Any) -> air.Tag:
    """Pass-through word break opportunity tag"""
    return air.Wbr(**kwargs)