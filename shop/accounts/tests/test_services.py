import pytest

from accounts.services import create_guest_user, get_user_by_email

pytestmark = pytest.mark.django_db


def test_get_user_by_email_ignores_case_and_spaces(django_user_model):
    user = django_user_model.objects.create(username="ana", email="ana@example.com")
    assert get_user_by_email("  Ana@Example.com ") == user


def test_get_user_by_email_unknown():
    assert get_user_by_email("nobody@example.com") is None


def test_create_guest_user_is_inactive():
    user = create_guest_user("Guest@Example.com")
    assert user.email == "guest@example.com"
    assert not user.is_active
    assert not user.has_usable_password()
