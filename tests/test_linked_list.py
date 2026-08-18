"""Tests for the LinkedList data structure."""

from data_structures.linked_list import LinkedList


def test_linked_list_starts_empty():
    linked_list = LinkedList()

    assert linked_list.head is None
    assert len(linked_list) == 0


def test_append():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 20
    assert linked_list.head.next.next.data == 30
    assert len(linked_list) == 3


def test_prepend():
    linked_list = LinkedList()

    linked_list.append(20)
    linked_list.prepend(10)

    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 20


def test_find():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)

    assert linked_list.find(20).data == 20
    assert linked_list.find(99) is None


def test_delete():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.delete(20) is True
    assert linked_list.find(20) is None
    assert len(linked_list) == 2


def test_delete_missing_item():
    linked_list = LinkedList()

    linked_list.append(10)

    assert linked_list.delete(99) is False
    assert len(linked_list) == 1