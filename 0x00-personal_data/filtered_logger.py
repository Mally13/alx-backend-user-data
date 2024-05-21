#!/usr/bin/env python3
"""
Contains a function filter_datum that returns the logs
message obfuscated
"""
import logging
from typing import List
import mysql.connector
import os
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns a obfuscated log message"""
    for f in fields:
        message = re.sub(rf"{f}=(.*?)\{separator}",
                         f'{f}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values of incoming log records"""
        return filter_datum(self.fields, RedactingFormatter.REDACTION,
                            super().format(record),
                            RedactingFormatter.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_logger() -> logging.Logger:
    """Returns a logger object that contains user data"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Establishes a database connection"""
    host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password=os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    database=os.getenv('PERSONAL_DATA_DB_NAME')
    try:
        personal_db = mysql.connector.connect(
            host=host,
            user=user,
            database=database,
            password=password
        )
        return personal_db
    except mysql.connector.Error as e:
        raise RuntimeError("Failed to connext to the database")
