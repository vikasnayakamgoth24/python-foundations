"""Searching algorithms with clear complexity characteristics."""


def linear_search(items: list[int], target: int) -> int:
    """Return the index of target using linear search.

    Returns:
        The target index if found, otherwise -1.

    Complexity:
        Time: O(n)
        Space: O(1)
    """
    for index, value in enumerate(items):
        if value == target:
            return index

    return -1


def binary_search(items: list[int], target: int) -> int:
    """Return the index of target using iterative binary search.

    The input list must be sorted in ascending order.

    Returns:
        The target index if found, otherwise -1.

    Complexity:
        Time: O(log n)
        Space: O(1)
    """
    left = 0
    right = len(items) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if items[middle] == target:
            return middle

        if items[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def binary_search_recursive(
    items: list[int],
    target: int,
    left: int = 0,
    right: int | None = None,
) -> int:
    """Return the index of target using recursive binary search.

    The input list must be sorted in ascending order.

    Complexity:
        Time: O(log n)
        Space: O(log n) due to recursion.
    """
    if right is None:
        right = len(items) - 1

    if left > right:
        return -1

    middle = left + (right - left) // 2

    if items[middle] == target:
        return middle

    if items[middle] < target:
        return binary_search_recursive(
            items,
            target,
            middle + 1,
            right,
        )

    return binary_search_recursive(
        items,
        target,
        left,
        middle - 1,
    )