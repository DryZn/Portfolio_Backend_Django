import pytest
from django.conf import settings


@pytest.fixture(scope="session", autouse=True)
def setup_test_database(django_db_setup, django_db_blocker):
    """Override database settings for tests to disable connection pooling."""
    with django_db_blocker.unblock():
        # Disable connection pooling for tests
        settings.DATABASES["default"]["CONN_MAX_AGE"] = 0
        settings.DATABASES["default"].pop("CONN_HEALTH_CHECKS", None)
