"""Printer Exception"""

class PrinterException(Exception):
    """Printer Exception"""

    def __init__(self, message: str):
        super().__init__(message)
