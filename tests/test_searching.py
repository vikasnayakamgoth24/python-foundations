"""Tests for searching algorithms."""

from algorithms.searching import (
    binary_search,
    binary_search_recursive,
    linear_search,
)


def test_linear_search_finds_target():
    items = [10, 20, 30, 40, 50]

    assert linear_search(items, 30) == 2


def test_linear_search_returns_minus_one_when_missing():
    items = [10, 20, 30, 40, 50]

    assert linear_search(items, 99) == -1


def test_binary_search_finds_target():
    items = [10, 20, 30, 40, 50]

    assert binary_search(items, 40) == 3


def test_binary_search_returns_minus_one_when_missing():
    items = [10, 20, 30, 40, 50]

    assert binary_search(items, 99) == -1


def test_recursive_binary_search_finds_target():
    items = [10, 20, 30, 40, 50]

    assert binary_search_recursive(items, 10) == 0


def test_recursive_binary_search_returns_minus_one_when_missing():
    items = [10, 20, 30, 40, 50]

    assert binary_search_recursive(items, 99) == -1


def test_search_empty_list():
    items = []

    assert linear_search(items, 10) == -1
    assert binary_search(items, 10) == -1
    assert binary_search_recursive(items, 10) == -1