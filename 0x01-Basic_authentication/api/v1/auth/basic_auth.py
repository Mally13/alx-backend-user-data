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

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from the base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        elif not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        elif ':' not in decoded_base64_authorization_header:
            return (None, None)
        email = ''
        for c in decoded_base64_authorization_header:
            if c != ':':
                email += c
            else:
                break
        password = decoded_base64_authorization_header[(len(email) + 1):]
        return (email, password)

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """Returns the User instance based on his email and password"""
        if user_email is None or user_pwd is None:
            return None
        elif not isinstance(user_email, str):
            return None
        elif not isinstance(user_pwd, str):
            return None
        try:
            user_list = User.search({'email': user_email})
        except Exception:
            return None
        if not user_list:
            return None
        for user in user_list:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth and retrieves the User instance for a request
        """
        auth_h = self.authorization_header(request)
        base64_auth_h = self.extract_base64_authorization_header(auth_h)
        decoded_base64_auth_h = self.decode_base64_authorization_header(
            base64_auth_h
        )
        if decoded_base64_auth_h is None:
            return None
        user_creds = self.extract_user_credentials(decoded_base64_auth_h)
        if user_creds is None or any(cred is None for cred in user_creds):
            return None
        user_email, user_pwd = user_creds
        return self.user_object_from_credentials(user_email, user_pwd)
