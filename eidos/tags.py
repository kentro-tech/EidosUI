from typing import Optional, Literal
import air
from . import styles
from .utils import stringify

def Button(*content, class_ = styles.buttons.primary, **kwargs):
    return air.Button(*content, class_=stringify(styles.buttons.base, class_), **kwargs)

def H1(*content, class_ = None, **kwargs):
    return air.H1(*content, class_=stringify(styles.typography.h1, class_), **kwargs)

def H2(*content, class_ = None, **kwargs):
    return air.H2(*content, class_=stringify(styles.typography.h2, class_), **kwargs)

def H3(*content, class_ = None, **kwargs):
    return air.H3(*content, class_=stringify(styles.typography.h3, class_), **kwargs)

def H4(*content, class_ = None, **kwargs):
    return air.H4(*content, class_=stringify(styles.typography.h4, class_), **kwargs)

def H5(*content, class_ = None, **kwargs):
    return air.H5(*content, class_=stringify(styles.typography.h5, class_), **kwargs)

def H6(*content, class_ = None, **kwargs):
    return air.H6(*content, class_=stringify(styles.typography.h6, class_), **kwargs)

def Body(*content, class_ = None, **kwargs):
    return air.Body(*content, class_=stringify(styles.Theme.body, class_), **kwargs)

# Semantic HTML Elements

def Strong(*content, class_ = None, **kwargs):
    return air.Strong(*content, class_=stringify(styles.semantic.strong, class_), **kwargs)

def I(*content, class_ = None, **kwargs):
    return air.I(*content, class_=stringify(styles.semantic.i, class_), **kwargs)

def Small(*content, class_ = None, **kwargs):
    return air.Small(*content, class_=stringify(styles.semantic.small, class_), **kwargs)

def Del(*content, class_ = None, **kwargs):
    return air.Del(*content, class_=stringify(styles.semantic.del_, class_), **kwargs)

def Abbr(*content, class_ = None, **kwargs):
    return air.Abbr(*content, class_=stringify(styles.semantic.abbr, class_), **kwargs)

def Var(*content, class_ = None, **kwargs):
    return air.Var(*content, class_=stringify(styles.semantic.var, class_), **kwargs)

def Mark(*content, class_ = None, **kwargs):
    return air.Mark(*content, class_=stringify(styles.semantic.mark, class_), **kwargs)

def Time(*content, class_ = None, **kwargs):
    return air.Time(*content, class_=stringify(styles.semantic.time, class_), **kwargs)

def Code(*content, class_ = None, **kwargs):
    return air.Code(*content, class_=stringify(styles.semantic.code, class_), **kwargs)

def Pre(*content, class_ = None, **kwargs):
    return air.Pre(*content, class_=stringify(styles.semantic.pre, class_), **kwargs)

def Kbd(*content, class_ = None, **kwargs):
    return air.Kbd(*content, class_=stringify(styles.semantic.kbd, class_), **kwargs)

def Samp(*content, class_ = None, **kwargs):
    return air.Samp(*content, class_=stringify(styles.semantic.samp, class_), **kwargs)

def Blockquote(*content, class_ = None, **kwargs):
    return air.Blockquote(*content, class_=stringify(styles.semantic.blockquote, class_), **kwargs)

def Cite(*content, class_ = None, **kwargs):
    return air.Cite(*content, class_=stringify(styles.semantic.cite, class_), **kwargs)

def Address(*content, class_ = None, **kwargs):
    return air.Address(*content, class_=stringify(styles.semantic.address, class_), **kwargs)

def Hr(class_ = None, **kwargs):
    return air.Hr(class_=stringify(styles.semantic.hr, class_), **kwargs)

def Details(*content, class_ = None, **kwargs):
    return air.Details(*content, class_=stringify(styles.semantic.details, class_), **kwargs)

def Summary(*content, class_ = None, **kwargs):
    return air.Summary(*content, class_=stringify(styles.semantic.summary, class_), **kwargs)

def Dl(*content, class_ = None, **kwargs):
    return air.Dl(*content, class_=stringify(styles.semantic.dl, class_), **kwargs)

def Dt(*content, class_ = None, **kwargs):
    return air.Dt(*content, class_=class_, **kwargs)

def Dd(*content, class_ = None, **kwargs):
    return air.Dd(*content, class_=stringify(styles.semantic.dd, class_), **kwargs)

def Figure(*content, class_ = None, **kwargs):
    return air.Figure(*content, class_=stringify(styles.semantic.figure, class_), **kwargs)

def Figcaption(*content, class_ = None, **kwargs):
    return air.Figcaption(*content, class_=stringify(styles.semantic.figcaption, class_), **kwargs)