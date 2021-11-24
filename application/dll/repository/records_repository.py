from application.dll.db import session
from application.dll.models.user import User


def get_all_records():
    return session.query(User).all()
