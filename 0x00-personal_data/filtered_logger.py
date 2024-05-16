#!/usr/bin/env python3
"""
Contains a function filter_datum that returns the log message obfuscated
"""
import re


def filter_datum(fields, redaction, message, separator):
    return re.sub(rf"({'|'.join(fields)})=[^{separator}]*",
                   lambda match: match.group(1) + "=" + redaction, message)
