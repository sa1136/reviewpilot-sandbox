from accounts.services import create_guest_user, get_user_by_email


def resolve_customer(email: str):
    """The account for this email, creating an inactive guest account on a first purchase."""
    user = get_user_by_email(email)
    if user is None:
        user = create_guest_user(email)
    return user
