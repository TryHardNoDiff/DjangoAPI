# api/services.py
from .models import User

def create_user(username: str, email: str) -> User:
    return User.objects.create(username=username, email=email)

def get_user(user_id: int) -> User:
    return User.objects.get(id=user_id)

def update_user(user_id: int, username: str = None, email: str = None) -> User:
    user = get_user(user_id)
    if username is not None:
        user.username = username
    if email is not None:
        user.email = email
    user.save()
    return user

def delete_user(user_id: int) -> bool:
    try:
        user = get_user(user_id)
        user.delete()
        return True
    except User.DoesNotExist:
        return False