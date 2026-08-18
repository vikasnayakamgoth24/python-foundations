"""Tests for the Binary Search Tree data structure."""

from data_structures.binary_search_tree import BinarySearchTree


def test_tree_starts_empty():
    tree = BinarySearchTree()

    assert tree.root is None
    assert len(tree) == 0


def test_insert():
    tree = BinarySearchTree()

    tree.insert(50)
    tree.insert(30)
    tree.insert(70)

    assert tree.root.data == 50
    assert tree.root.left.data == 30
    assert tree.root.right.data == 70


def test_search():
    tree = BinarySearchTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    assert tree.search(50) is True
    assert tree.search(20) is True
    assert tree.search(80) is True
    assert tree.search(99) is False


def test_inorder_traversal():
    tree = BinarySearchTree()

    for value in [50, 30, 70, 20, 40, 60, 80]:
        tree.insert(value)

    assert tree.inorder() == [20, 30, 40, 50, 60, 70, 80]


def test_duplicate_values_are_ignored():
    tree = BinarySearchTree()

    tree.insert(50)
    tree.insert(50)

    assert tree.inorder() == [50]
    assert len(tree) == 1