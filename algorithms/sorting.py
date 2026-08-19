"""Sorting algorithms."""


def bubble_sort(items: list[int]) -> list[int]:
    """Sort a list using the bubble sort algorithm."""
    result = items.copy()

    for i in range(len(result)):
        for j in range(0, len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]

    return result


def merge_sort(items: list[int]) -> list[int]:
    """Sort a list using the merge sort algorithm."""
    if len(items) <= 1:
        return items.copy()

    middle = len(items) // 2

    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result


def quick_sort(items: list[int]) -> list[int]:
    """Sort a list using the quick sort algorithm."""
    if len(items) <= 1:
        return items.copy()

    pivot = items[len(items) // 2]

    left = [item for item in items if item < pivot]
    middle = [item for item in items if item == pivot]
    right = [item for item in items if item > pivot]

    return quick_sort(left) + middle + quick_sort(right)