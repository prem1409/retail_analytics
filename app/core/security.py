from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "super-secret"

pwd_context = CryptContext(
    schemes=["bcrypt"]
)

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)

def create_access_token(data):
    return jwt.encode(
        data,
        SECRET_KEY,
        algorithm="HS256"
    )