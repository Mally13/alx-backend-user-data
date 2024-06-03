#!/usr/bin/env python3
""" Manages API authentication
"""
from api.v1.auth.auth import Auth
import base64
from flask import request
from typing import List, TypeVar
from models.user import User


class BasicAuth(Auth):
    """A class to manage the API authentication"""

    def extract_base64_authorization_header(self, authorization_header: str):
        """Returns Base64 part of the authorization header"""
        if authorization_header is None:
            return None
        elif not isinstance(authorization_header, str):
            return None
        elif authorization_header[0:6] != 'Basic ':
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns a decoded value of Base64 string"""
        try:
            if base64_authorization_header is None:
                return None
            elif not isinstance(base64_authorization_header, str):
                return None
            auth_decoded = base64.b64decode(base64_authorization_header)
            decoded_string = auth_decoded.decode('utf-8')
            return decoded_string
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
