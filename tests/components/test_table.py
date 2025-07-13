"""Tests for the DataTable component."""

from eidos.components import DataTable


def test_table_from_lists_basic(sample_data_lists):
    """Test creating a table from lists without headers."""
    table = DataTable.from_lists(sample_data_lists)

    # Convert to string to check HTML structure
    table_html = table.render()

    # Check that it contains table tag with the right class
    assert 'class="eidos-table"' in table_html
    assert "<table" in table_html
    assert "</table>" in table_html

    # Check tbody exists
    assert '<tbody class="eidos-tbody">' in table_html

    # Check data is present
    assert "Alice" in table_html
    assert "Engineer" in table_html


def test_table_from_lists_with_headers(sample_data_lists, sample_headers):
    """Test creating a table from lists with headers."""
    table = DataTable.from_lists(sample_data_lists, headers=sample_headers)

    table_html = table.render()

    # Check thead exists
    assert '<thead class="eidos-thead">' in table_html

    # Check headers are present
    assert "name" in table_html
    assert "age" in table_html
    assert "role" in table_html

    # Check th tags
    assert '<th class="eidos-th">' in table_html


def test_table_from_dicts_basic(sample_data_dicts):
    """Test creating a table from dictionaries without explicit headers."""
    table = DataTable.from_dicts(sample_data_dicts)

    table_html = table.render()

    # Check that headers were auto-generated from keys
    assert '<thead class="eidos-thead">' in table_html
    assert "name" in table_html  # Dict keys become headers

    # Check data is present
    assert "Alice" in table_html
    assert "28" in table_html


def test_table_from_dicts_with_headers(sample_data_dicts, sample_headers):
    """Test creating a table from dictionaries with explicit headers."""
    # Use lowercase headers that match the dictiona∂ry keys
    table = DataTable.from_dicts(sample_data_dicts, headers=sample_headers)

    table_html = table.render()

    # Check headers are used
    assert "name" in table_html
    assert "age" in table_html
    assert "role" in table_html

    # Check data is present
    assert "Alice" in table_html
    assert "Engineer" in table_html


def test_table_from_empty_lists():
    """Test creating a table from empty data."""
    table = DataTable.from_lists([])

    table_html = table.render()

    # Should still have table structure
    assert "<table" in table_html
    assert "<tbody" in table_html


def test_table_from_empty_dicts():
    """Test creating a table from empty dictionary data."""
    table = DataTable.from_dicts([])

    table_html = table.render()

    # Should still have table structure
    assert "<table" in table_html


def test_table_custom_class():
    """Test adding custom CSS classes to table."""
    table = DataTable.from_lists([["A", "B"]], class_="custom-table")

    table_html = table.render()

    # Should have both default and custom class
    assert "eidos-table" in table_html
    assert "custom-table" in table_html
