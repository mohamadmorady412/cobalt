from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_users = {
    "admin": {"username": "admin", "hashed_password": pwd_context.hash("123456")}
}


def verify_user(username: str, password: str):
    user = fake_users.get(username)
    if not user:
        return None
    if not pwd_context.verify(password, user["hashed_password"]):
        return None
    return user
