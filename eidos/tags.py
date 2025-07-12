from typing import Optional, Literal, Any, Union
import air
from . import styles
from .utils import stringify

def Button(*content: Any, class_: Optional[Union[str, list[str]]] = styles.buttons.primary, **kwargs: Any) -> air.Tag:
    return air.Button(*content, class_=stringify(styles.buttons.base, class_), **kwargs)

def H1(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H1(*content, class_=stringify(styles.typography.h1, class_), **kwargs)

def H2(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
    return air.H2(*content, class_=stringify(styles.typography.h2, class_), **kwargs)

def H3(*content: Any, class_: Optional[Union[str, list[str]]] = None, **kwargs: Any) -> air.Tag:
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