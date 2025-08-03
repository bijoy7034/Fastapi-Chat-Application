from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password (plain: str):
    return pwd_context.hash(plain)

def verify_password(plain: str, hash: str):
    return pwd_context.verify(plain, hash)