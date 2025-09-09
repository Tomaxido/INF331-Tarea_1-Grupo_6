import os

def login(user: str, pwd: str) -> bool:
    expected_user = os.getenv("ADMIN_USER", "admin")
    expected_pwd  = os.getenv("ADMIN_PASS", "admin")
    return user == expected_user and pwd == expected_pwd
