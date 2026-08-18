"""Tests for the Queue data structure."""

import pytest

from data_structures.queue import Queue


def test_queue_starts_empty():
    queue = Queue()

    assert queue.is_empty()
    assert len(queue) == 0


def test_enqueue_and_peek():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)

    assert queue.peek() == 10
    assert len(queue) == 2


def test_dequeue_follows_fifo():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.dequeue() == 10
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30


def test_dequeue_empty_queue_raises_error():
    queue = Queue()

    with pytest.raises(IndexError, match="Cannot dequeue from an empty queue."):
        queue.dequeue()


def test_peek_empty_queue_raises_error():
    queue = Queue()

    with pytest.raises(IndexError, match="Cannot peek at an empty queue."):
        queue.peek()