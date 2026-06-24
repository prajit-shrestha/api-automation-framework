import pytest
import config
from utils.api_client import APIClient


@pytest.fixture
def headers():
    return config.HEADERS

@pytest.fixture
def client():
    return APIClient()