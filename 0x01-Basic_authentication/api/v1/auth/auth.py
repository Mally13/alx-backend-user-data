#!/usr/bin/env python3
""" Manages API authentication
"""
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth:
    """A class to manage the API authentication"""
    def __init__(self) -> None:
        """initializes the auth class"""
        pass

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        """For paths that require auth"""
        return False

    def authorization_header(self, request=None) -> str:
        """Handles flask request object"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
