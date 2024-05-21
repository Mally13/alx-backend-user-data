#!/usr/bin/env python3
"""
Contains hash_password function to encrypt passwords
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts passwords"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes, salt)
    return hashed
