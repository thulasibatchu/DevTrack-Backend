from passlib.context import CryptContext

# create password hashing context
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# function to hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# function to verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)