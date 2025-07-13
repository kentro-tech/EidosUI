"""Tests for the styles module."""

from eidos import styles
from eidos.styles import buttons, semantic, tables, typography


def test_button_styles():
    """Test that button style constants are defined."""
    assert buttons.base == "eidos-btn"
    assert buttons.primary == "eidos-btn-primary"
    assert buttons.secondary == "eidos-btn-secondary"
    assert buttons.ghost == "eidos-btn-ghost"


def test_typography_styles():
    """Test that typography style constants are defined."""
    assert typography.h1 == "eidos-h1"
    assert typography.h2 == "eidos-h2"
    assert typography.h3 == "eidos-h3"


def test_semantic_styles():
    """Test that semantic style constants are defined."""
    assert semantic.strong == "eidos-strong"
    assert semantic.code == "eidos-code"
    assert semantic.mark == "eidos-mark"


def test_table_styles():
    """Test that table style constants are defined."""
    assert tables.table == "eidos-table"
    assert tables.thead == "eidos-thead"
    assert tables.tbody == "eidos-tbody"
    assert tables.tr == "eidos-tr"
    assert tables.th == "eidos-th"
    assert tables.td == "eidos-td"


def test_styles_namespace():
    """Test accessing styles through the main styles module."""
    assert styles.buttons.primary == "eidos-btn-primary"
    assert styles.typography.h1 == "eidos-h1"
    assert styles.semantic.strong == "eidos-strong"
    assert styles.tables.table == "eidos-table"
