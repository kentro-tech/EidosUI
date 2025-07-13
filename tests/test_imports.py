"""Test various import patterns for EidosUI."""


def test_star_import():
    """Test that star import works and provides expected symbols."""
    # Use exec to test star import at runtime
    namespace = {}
    exec("from eidos import *", namespace)

    # Check that common components are available
    assert "DataTable" in namespace
    assert "Table" in namespace  # HTML tag
    assert "Button" in namespace
    assert "H1" in namespace
    assert "Div" in namespace

    # Check that styles are available
    assert "styles" in namespace
    assert "buttons" in namespace
    assert "typography" in namespace
    assert "semantic" in namespace
    assert "tables" in namespace

    # Verify they're not None
    assert namespace["DataTable"] is not None
    assert namespace["Table"] is not None  # HTML tag
    assert namespace["Button"] is not None
    assert namespace["styles"] is not None


def test_direct_imports():
    """Test direct imports from main module."""
    from eidos import H1, Button, DataTable, Div, Table, styles

    assert DataTable is not None
    assert Table is not None  # HTML tag
    assert Button is not None
    assert H1 is not None
    assert Div is not None
    assert styles is not None


def test_submodule_imports():
    """Test imports from submodules."""
    from eidos.components import DataTable
    from eidos.styles import buttons, semantic, tables, typography
    from eidos.tags import H1, Button, Div, Table

    assert DataTable is not None
    assert Table is not None  # HTML tag from tags
    assert Button is not None
    assert H1 is not None
    assert Div is not None
    assert buttons is not None
    assert typography is not None
    assert semantic is not None
    assert tables is not None


def test_style_namespace_access():
    """Test accessing styles through the namespace."""
    from eidos import styles

    # Check style groups exist
    assert hasattr(styles, "buttons")
    assert hasattr(styles, "typography")
    assert hasattr(styles, "semantic")
    assert hasattr(styles, "tables")

    # Check specific style classes exist
    assert hasattr(styles.buttons, "primary")
    assert hasattr(styles.typography, "h1")
    assert hasattr(styles.semantic, "strong")
    assert hasattr(styles.tables, "table")


def test_version_info():
    """Test that version information is available."""
    import eidos

    assert hasattr(eidos, "__version__")
    assert isinstance(eidos.__version__, str)
    assert eidos.__version__ == "0.4.0"


def test_all_exports():
    """Test that __all__ is properly defined."""
    import eidos

    assert hasattr(eidos, "__all__")
    assert isinstance(eidos.__all__, list)
    assert len(eidos.__all__) > 0

    # Check that key exports are in __all__
    assert "DataTable" in eidos.__all__
    assert "Table" in eidos.__all__  # HTML tag
    assert "Button" in eidos.__all__
    assert "styles" in eidos.__all__
    assert "__version__" in eidos.__all__
