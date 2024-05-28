#!/usr/bin/env python3
""" Manages API authentication
"""
from flask import request
from typing import List, TypeVar
from models.user import User
from api.v1.auth.auth import Auth


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
