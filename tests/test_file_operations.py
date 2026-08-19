"""Tests for file handling operations."""

from file_handling.file_operations import (
    append_file,
    read_file,
    write_file,
)


def test_write_and_read_file(tmp_path):
    file_path = tmp_path / "example.txt"

    write_file(file_path, "Hello, Python!")

    assert read_file(file_path) == "Hello, Python!"


def test_append_file(tmp_path):
    file_path = tmp_path / "example.txt"

    write_file(file_path, "Hello")
    append_file(file_path, " World")

    assert read_file(file_path) == "Hello World"


def test_write_empty_file(tmp_path):
    file_path = tmp_path / "empty.txt"

    write_file(file_path, "")

    assert read_file(file_path) == ""


def test_append_multiple_times(tmp_path):
    file_path = tmp_path / "example.txt"

    write_file(file_path, "A")
    append_file(file_path, "B")
    append_file(file_path, "C")

    assert read_file(file_path) == "ABC"