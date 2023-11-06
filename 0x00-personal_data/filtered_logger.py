#!/usr/bin/env python3
"""
Obfuscate a string
"""

import re
from typing import List
import logging

def filter_datum(fields: List, redaction: str, message: str, separator: str) -> str:
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all fields in the log line (message)

    Return: A log message
    """
    pattern = '|'.join(fields)
    return re.sub(f'({pattern})=.*?{separator}',\
                  f'\\1={redaction}{separator}', message)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List):
        """ Create fields variables
            """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Using filter_datum find return a obfuscated log message
            """
        message = super(RedactingFormatter, self).format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)

