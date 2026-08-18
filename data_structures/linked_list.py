"""Singly linked list data structure."""


class Node:
    """A node in a singly linked list."""

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A singly linked list."""

    def __init__(self):
        self.head = None

    def append(self, data) -> None:
        """Add an item to the end of the list."""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def prepend(self, data) -> None:
        """Add an item to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def find(self, data) -> Node | None:
        """Return the first node containing data."""
        current = self.head

        while current is not None:
            if current.data == data:
                return current

            current = current.next

        return None

    def delete(self, data) -> bool:
        """Delete the first node containing data."""
        if self.head is None:
            return False

        if self.head.data == data:
            self.head = self.head.next
            return True

        current = self.head

        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return True

            current = current.next

        return False

    def __len__(self) -> int:
        """Return the number of nodes."""
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count