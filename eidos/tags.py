from typing import Optional, Literal
import air
from . import styles
from .utils import stringify

def Button(*content, cls = styles.buttons.primary, **kwargs):
    return air.Button(*content, cls=stringify(styles.buttons.base, cls), **kwargs)

def H1(*content, cls = None, **kwargs):
    return air.H1(*content, cls=stringify(styles.typography.h1, cls), **kwargs)

def H2(*content, cls = None, **kwargs):
    return air.H2(*content, cls=stringify(styles.typography.h2, cls), **kwargs)

def H3(*content, cls = None, **kwargs):
    return air.H3(*content, cls=stringify(styles.typography.h3, cls), **kwargs)

def H4(*content, cls = None, **kwargs):
    return air.H4(*content, cls=stringify(styles.typography.h4, cls), **kwargs)

def H5(*content, cls = None, **kwargs):
    return air.H5(*content, cls=stringify(styles.typography.h5, cls), **kwargs)

def H6(*content, cls = None, **kwargs):
    return air.H6(*content, cls=stringify(styles.typography.h6, cls), **kwargs)

def Body(*content, cls = None, **kwargs):
    return air.Body(*content, cls=stringify(styles.Theme.body, cls), **kwargs)

# Semantic HTML Elements

def Strong(*content, cls = None, **kwargs):
    return air.Strong(*content, cls=stringify(styles.semantic.strong, cls), **kwargs)

def I(*content, cls = None, **kwargs):
    return air.I(*content, cls=stringify(styles.semantic.i, cls), **kwargs)

def Small(*content, cls = None, **kwargs):
    return air.Small(*content, cls=stringify(styles.semantic.small, cls), **kwargs)

def Del(*content, cls = None, **kwargs):
    return air.Del(*content, cls=stringify(styles.semantic.del_, cls), **kwargs)

def Abbr(*content, cls = None, **kwargs):
    return air.Abbr(*content, cls=stringify(styles.semantic.abbr, cls), **kwargs)

def Var(*content, cls = None, **kwargs):
    return air.Var(*content, cls=stringify(styles.semantic.var, cls), **kwargs)

def Mark(*content, cls = None, **kwargs):
    return air.Mark(*content, cls=stringify(styles.semantic.mark, cls), **kwargs)

def Time(*content, cls = None, **kwargs):
    return air.Time(*content, cls=stringify(styles.semantic.time, cls), **kwargs)

def Code(*content, cls = None, **kwargs):
    return air.Code(*content, cls=stringify(styles.semantic.code, cls), **kwargs)

def Pre(*content, cls = None, **kwargs):
    return air.Pre(*content, cls=stringify(styles.semantic.pre, cls), **kwargs)

def Kbd(*content, cls = None, **kwargs):
    return air.Kbd(*content, cls=stringify(styles.semantic.kbd, cls), **kwargs)

def Samp(*content, cls = None, **kwargs):
    return air.Samp(*content, cls=stringify(styles.semantic.samp, cls), **kwargs)

def Blockquote(*content, cls = None, **kwargs):
    return air.Blockquote(*content, cls=stringify(styles.semantic.blockquote, cls), **kwargs)

def Cite(*content, cls = None, **kwargs):
    return air.Cite(*content, cls=stringify(styles.semantic.cite, cls), **kwargs)

def Address(*content, cls = None, **kwargs):
    return air.Address(*content, cls=stringify(styles.semantic.address, cls), **kwargs)

def Hr(cls = None, **kwargs):
    return air.Hr(cls=stringify(styles.semantic.hr, cls), **kwargs)

def Details(*content, cls = None, **kwargs):
    return air.Details(*content, cls=stringify(styles.semantic.details, cls), **kwargs)

def Summary(*content, cls = None, **kwargs):
    return air.Summary(*content, cls=stringify(styles.semantic.summary, cls), **kwargs)

def Dl(*content, cls = None, **kwargs):
    return air.Dl(*content, cls=stringify(styles.semantic.dl, cls), **kwargs)

def Dt(*content, cls = None, **kwargs):
    return air.Dt(*content, cls=cls, **kwargs)

def Dd(*content, cls = None, **kwargs):
    return air.Dd(*content, cls=stringify(styles.semantic.dd, cls), **kwargs)

def Figure(*content, cls = None, **kwargs):
    return air.Figure(*content, cls=stringify(styles.semantic.figure, cls), **kwargs)

def Figcaption(*content, cls = None, **kwargs):
    return air.Figcaption(*content, cls=stringify(styles.semantic.figcaption, cls), **kwargs)