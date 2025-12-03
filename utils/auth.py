import hashlib

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify(password, password_hash):
    return hash_password(password) == password_hash