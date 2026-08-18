"""Min Heap data structure."""


class MinHeap:
    """A min heap implementation."""

    def __init__(self):
        self._items = []

    def insert(self, value) -> None:
        """Insert a value into the heap."""
        self._items.append(value)
        self._bubble_up(len(self._items) - 1)

    def peek(self):
        """Return the minimum value without removing it."""
        if self.is_empty():
            raise IndexError("Cannot peek at an empty heap.")

        return self._items[0]

    def extract_min(self):
        """Remove and return the minimum value."""
        if self.is_empty():
            raise IndexError("Cannot extract from an empty heap.")

        if len(self._items) == 1:
            return self._items.pop()

        minimum = self._items[0]
        self._items[0] = self._items.pop()
        self._bubble_down(0)

        return minimum

    def is_empty(self) -> bool:
        """Return True if the heap is empty."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Return the number of items in the heap."""
        return len(self._items)

    def _bubble_up(self, index: int) -> None:
        while index > 0:
            parent = (index - 1) // 2

            if self._items[index] >= self._items[parent]:
                break

            self._items[index], self._items[parent] = (
                self._items[parent],
                self._items[index],
            )

            index = parent

    def _bubble_down(self, index: int) -> None:
        size = len(self._items)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self._items[left] < self._items[smallest]:
                smallest = left

            if right < size and self._items[right] < self._items[smallest]:
                smallest = right

            if smallest == index:
                break

            self._items[index], self._items[smallest] = (
                self._items[smallest],
                self._items[index],
            )

            index = smallest