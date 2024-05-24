#!/usr/bin/env python3
""" Manages API authentication
"""
from flask import request
from typing import List, TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """A class to manage the API authentication"""
    pass
