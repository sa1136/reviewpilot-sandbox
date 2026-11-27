from accounts.models import User


def normalize_email(email: str) -> str:
    return email.strip().lower()


def get_user_by_email(email: str) -> User | None:
    """The user with this email address, or None if there is no account."""
    return User.objects.filter(email=normalize_email(email)).first()


def create_guest_user(email: str) -> User:
    """An inactive account for a customer who checked out without signing up."""
    email = normalize_email(email)
    user = User(username=email, email=email, is_active=False)
    user.set_unusable_password()
    user.save()
    return user
