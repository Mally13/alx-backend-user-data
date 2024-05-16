#!/usr/bin/env python3
"""
Contains a function filter_datum that returns the logs
message obfuscated
"""
import re
import logging



def filter_datum(fields, redaction, message, separator) -> str:
    """Returns a obfuscated log message"""
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                            f'{f}={redaction}{separator}', message)
    return message
    


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError