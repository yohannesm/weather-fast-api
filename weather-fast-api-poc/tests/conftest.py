from os import environ
from fastapi.testclient import TestClient
import pytest


environ.setdefault('DEBUG', 'True')


@pytest.fixture(scope='session')
def client():
    from weather-fast-api-poc.main import app

    with TestClient(app) as client:
        yield client
