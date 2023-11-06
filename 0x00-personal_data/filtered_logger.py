#!/usr/bin/env python3
"""
Obfuscate a string
"""

import re
from typing import List


def filter_datum(fields: List, redaction: str, message: str, separator: str) -> str:
    """
    fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating all fields in the log line (message)

    Retunr: A log message
    """
    pattern = '|'.join(fields)
    return re.sub(f'({pattern})=.*?{separator}',\
		  f'\\1={redaction}{separator}', message)

