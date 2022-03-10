import pytest
from factory.main_factory import create_app


@pytest.fixture()
def app():
    server = create_app()
    server.config.update(
        {
            "TESTING": True,
        }
    )

    yield server


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
