"""Binary Search Tree data structure."""


class Node:
    """A node in a binary search tree."""

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """A binary search tree."""

    def __init__(self):
        self.root = None

    def insert(self, data) -> None:
        """Insert a value into the tree."""
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)

        return node

    def search(self, data) -> bool:
        """Return True if data exists in the tree."""
        current = self.root

        while current is not None:
            if data == current.data:
                return True

            if data < current.data:
                current = current.left
            else:
                current = current.right

        return False

    def inorder(self) -> list:
        """Return values using inorder traversal."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return

        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

    def __len__(self) -> int:
        """Return the number of nodes."""
        return len(self.inorder())