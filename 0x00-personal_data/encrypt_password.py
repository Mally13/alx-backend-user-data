#!/usr/bin/env python3
"""
Contains hash_password and is_valid functions to encrypt
passwords and check their validity
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Encrypts passwords"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(bytes, salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks whether a password is valid"""
    pswd_bytes = password.encode('utf-8')
    return bcrypt.checkpw(pswd_bytes, hashed_password)
