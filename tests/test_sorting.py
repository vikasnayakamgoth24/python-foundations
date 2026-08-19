"""Tests for sorting algorithms."""

from algorithms.sorting import bubble_sort, merge_sort, quick_sort


def test_bubble_sort():
    items = [5, 2, 8, 1, 3]

    assert bubble_sort(items) == [1, 2, 3, 5, 8]


def test_merge_sort():
    items = [5, 2, 8, 1, 3]

    assert merge_sort(items) == [1, 2, 3, 5, 8]


def test_quick_sort():
    items = [5, 2, 8, 1, 3]

    assert quick_sort(items) == [1, 2, 3, 5, 8]


def test_sorting_empty_list():
    items = []

    assert bubble_sort(items) == []
    assert merge_sort(items) == []
    assert quick_sort(items) == []


def test_sorting_single_item():
    items = [42]

    assert bubble_sort(items) == [42]
    assert merge_sort(items) == [42]
    assert quick_sort(items) == [42]


def test_sorting_duplicates():
    items = [4, 2, 4, 1, 2]

    expected = [1, 2, 2, 4, 4]

    assert bubble_sort(items) == expected
    assert merge_sort(items) == expected
    assert quick_sort(items) == expected


def test_sorting_does_not_modify_original_list():
    items = [3, 1, 2]

    bubble_sort(items)
    merge_sort(items)
    quick_sort(items)

    assert items == [3, 1, 2]