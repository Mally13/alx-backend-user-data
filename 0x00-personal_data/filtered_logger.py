#!/usr/bin/env python3
"""
Contains a function filter_datum that returns the logs
message obfuscated
"""
import re
import logging



def filter_datum(fields, redaction, message, separator) -> str:
    """Returns a obfuscated log message"""
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*",
                  lambda match: match.group(1) + "=" + redaction, message)


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