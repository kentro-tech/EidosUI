from typing import Optional, Literal
import air
from . import styles
from .utils import stringify

def Button(*content, cls = styles.buttons.primary, **kwargs):
    return air.Button(*content, cls=stringify(styles.buttons.base, cls), **kwargs)

def H1(*content, cls = styles.typography.h1, **kwargs):
    return air.H1(*content, cls=cls, **kwargs)

def H2(*content, cls = styles.typography.h2, **kwargs):
    return air.H2(*content, cls=cls, **kwargs)

def H3(*content, cls = styles.typography.h3, **kwargs):
    return air.H3(*content, cls=cls, **kwargs)

def H4(*content, cls = styles.typography.h4, **kwargs):
    return air.H4(*content, cls=cls, **kwargs)

def H5(*content, cls = styles.typography.h5, **kwargs):
    return air.H5(*content, cls=cls, **kwargs)

def H6(*content, cls = styles.typography.h6, **kwargs):
    return air.H6(*content, cls=cls, **kwargs)

def Body(*content, cls = styles.Theme.body, **kwargs):
    return air.Body(*content, cls=cls, **kwargs)