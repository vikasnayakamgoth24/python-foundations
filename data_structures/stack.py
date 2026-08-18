"""Stack data structure implementation."""

from typing import Generic, TypeVar


T = TypeVar("T")


class Stack(Generic[T]):
    """A simple LIFO (Last-In, First-Out) stack."""

    def __init__(self) -> None:
        """Initialize an empty stack."""
        self._items: list[T] = []

    def push(self, item: T) -> None:
        """Add an item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack.")

        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("Cannot peek at an empty stack.")

        return self._items[-1]

    def is_empty(self) -> bool:
        """Return True if the stack contains no items."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)