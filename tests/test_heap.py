"""Tests for the MinHeap data structure."""

import pytest

from data_structures.heap import MinHeap


def test_heap_starts_empty():
    heap = MinHeap()

    assert heap.is_empty()
    assert len(heap) == 0


def test_insert_and_peek():
    heap = MinHeap()

    heap.insert(30)
    heap.insert(10)
    heap.insert(20)

    assert heap.peek() == 10
    assert len(heap) == 3


def test_extract_min_returns_sorted_order():
    heap = MinHeap()

    for value in [50, 20, 40, 10, 30]:
        heap.insert(value)

    assert heap.extract_min() == 10
    assert heap.extract_min() == 20
    assert heap.extract_min() == 30
    assert heap.extract_min() == 40
    assert heap.extract_min() == 50


def test_extract_empty_heap_raises_error():
    heap = MinHeap()

    with pytest.raises(
        IndexError,
        match="Cannot extract from an empty heap.",
    ):
        heap.extract_min()


def test_peek_empty_heap_raises_error():
    heap = MinHeap()

    with pytest.raises(
        IndexError,
        match="Cannot peek at an empty heap.",
    ):
        heap.peek()