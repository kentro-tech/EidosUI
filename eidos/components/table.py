from typing import Any

from air import Tag

from ..tags import Table as BaseTable
from ..tags import Tbody, Td, Th, Thead, Tr


class DataTable:
    """DataTable component that provides convenient methods for creating tables from data."""

    @classmethod
    def from_lists(
        cls,
        data: list[list],
        headers: list[str] | None = None,
        class_: str | list[str] | None = None,
        **kwargs: Any,
    ) -> Tag:
        """Create table from list of lists.

        Args:
            data: List of lists where each inner list is a row
            headers: Optional list of header strings
            class_: Optional CSS classes to add to the table
            **kwargs: Additional attributes to pass to the table element

        Returns:
            A rendered table element

        Example:
            Table.from_lists([["A", "B"], ["C", "D"]], headers=["Col1", "Col2"])
        """
        content = []

        if headers:
            thead = Thead(Tr(*[Th(header) for header in headers]))
            content.append(thead)

        tbody_rows = []
        for row_data in data:
            tbody_rows.append(Tr(*[Td(cell) for cell in row_data]))
        tbody = Tbody(*tbody_rows)
        content.append(tbody)

        return BaseTable(*content, class_=class_, **kwargs)

    @classmethod
    def from_dicts(
        cls,
        data: list[dict],
        headers: list[str] | None = None,
        class_: str | list[str] | None = None,
        **kwargs: Any,
    ) -> Tag:
        """Create table from list of dictionaries.

        Args:
            data: List of dictionaries where each dict is a row
            headers: Optional list of header strings. If not provided, uses keys from first dict
            class_: Optional CSS classes to add to the table
            **kwargs: Additional attributes to pass to the table element

        Returns:
            A rendered table element

        Example:
            Table.from_dicts([{"name": "John", "age": 25}], headers=["name", "age"])
        """
        if headers is None and data:
            headers = list(data[0].keys())

        content = []

        if headers:
            thead = Thead(Tr(*[Th(header) for header in headers]))
            content.append(thead)

        tbody_rows = []
        if data and headers:
            for row in data:
                tbody_rows.append(Tr(*[Td(row.get(key, "")) for key in headers]))
        tbody = Tbody(*tbody_rows)
        content.append(tbody)

        return BaseTable(*content, class_=class_, **kwargs)
