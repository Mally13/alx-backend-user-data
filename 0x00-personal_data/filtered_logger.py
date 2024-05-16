#!/usr/bin/env python3
"""
Contains a function filter_datum that returns the logs
message obfuscated
"""
import re
import logging
from typing import List



def filter_datum(fields, redaction, message, separator):
    """Returns a obfuscated log message"""
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                            f'{f}={redaction}{separator}', message)
    return message
