"""Tests for the Stack data structure."""

import pytest

from data_structures.stack import Stack


def test_stack_starts_empty():
    stack = Stack()

    assert stack.is_empty()
    assert len(stack) == 0


def test_push_and_peek():
    stack = Stack()

    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20
    assert len(stack) == 2


def test_pop_returns_last_item():
    stack = Stack()

    stack.push(10)
    stack.push(20)

    assert stack.pop() == 20
    assert stack.pop() == 10
    assert stack.is_empty()


def test_empty_stack_errors():
    stack = Stack()

    with pytest.raises(IndexError, match="Cannot pop from an empty stack."):
        stack.pop()

    with pytest.raises(IndexError, match="Cannot peek at an empty stack."):
        stack.peek()