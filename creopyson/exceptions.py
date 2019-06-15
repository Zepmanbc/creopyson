"""Creopyson exceptions."""


class Error(Exception):
    """Base class for other exceptions."""

    pass


class MissingKey(Error):
    """Raised when the input value is too small."""

    pass


class ErrorJsonDecode(Error):
    """Raised when creoson result cannot be decoded."""

    pass
