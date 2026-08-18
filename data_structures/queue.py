"""Queue data structure implementation."""

from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class Queue(Generic[T]):
    """A FIFO (First-In, First-Out) queue."""

    def __init__(self) -> None:
        self._items: deque[T] = deque()

    def enqueue(self, item: T) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self) -> T:
        """Remove and return the front item."""
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")

        return self._items.popleft()

    def peek(self) -> T:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty queue.")

        return self._items[0]

    def is_empty(self) -> bool:
        """Return True if the queue contains no items."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)