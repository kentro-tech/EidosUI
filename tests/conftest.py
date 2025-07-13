"""Pytest configuration and fixtures for EidosUI tests."""

import pytest


@pytest.fixture
def sample_data_lists():
    """Sample data in list format for testing."""
    return [
        ["Alice", "28", "Engineer"],
        ["Bob", "32", "Designer"],
        ["Charlie", "25", "Product Manager"]
    ]


@pytest.fixture
def sample_data_dicts():
    """Sample data in dictionary format for testing."""
    return [
        {"name": "Alice", "age": 28, "role": "Engineer"},
        {"name": "Bob", "age": 32, "role": "Designer"},
        {"name": "Charlie", "age": 25, "role": "Product Manager"}
    ]


@pytest.fixture
def sample_headers():
    """Sample headers for table testing."""
    return ["name", "age", "role"]