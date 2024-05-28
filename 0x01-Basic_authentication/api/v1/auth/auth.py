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
        if path is None:
            return True
        elif not exclude_paths or len(exclude_paths) == 0:
            return True
        else:
            path = path.rstrip('/') + '/'
            for excluded_path in exclude_paths:
                excluded_path = excluded_path.strip()
                if path.lower() == excluded_path.lower():
                    return False
            return True

    def authorization_header(self, request=None) -> str:
        """Handles flask request object"""
        if request is None:
            return None
        elif 'Authorization' in request.headers:
            return request.headers.get('Authorization')
        else:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
