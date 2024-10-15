from script.deploy import deploy_favorites
import pytest


@pytest.fixture(scope="session")
def favorites():
    return deploy_favorites()
