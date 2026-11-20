from unittest import mock

import inventory
from reports import export_report, report_rows


def setup_function():
    inventory.stock.clear()


def test_format_sku():
    assert inventory.format_sku("  ab-1 ") == "AB-1"


def test_adjust_stock_adds_units():
    assert inventory.adjust_stock("ab-1", 5) == 5
    assert inventory.adjust_stock("AB-1", 2) == 7


def test_reserved_units_for_open_order():
    orders = {"o1": {"quantity": 3}}
    assert inventory.reserved_units(orders, "o1") == 3


def test_low_stock():
    inventory.stock.update({"A": 10, "B": 1})
    assert inventory.low_stock(2) == ["B"]


def test_warehouse_headers():
    assert inventory.warehouse_headers("t") == {"Authorization": "Bearer t"}


def test_report_rows_sorted():
    assert report_rows({"b": 1, "a": 2}) == [("a", 2), ("b", 1)]


def test_export_report_runs_tar():
    with mock.patch("reports.subprocess.run") as run:
        export_report("daily")
    assert run.called
