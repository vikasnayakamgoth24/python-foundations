"""Basic file handling operations."""


def write_file(filename: str, content: str) -> None:
    """Write content to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def read_file(filename: str) -> str:
    """Read and return the contents of a file."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def append_file(filename: str, content: str) -> None:
    """Append content to a file."""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)
