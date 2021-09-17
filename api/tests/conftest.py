"""
This file contains commonly used pytest fixtures.
"""
import pytest

from api.endpoints import app


@pytest.fixture
def client():
    """
    This fixture allows us to call our app's endpoints as a client.
    """
    return app.test_client()
