import os

import pytest


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(os.path.dirname(__file__), "docker-compose.yml")


@pytest.fixture
def make_{{ cookiecutter.plugin_name }}():
    def _make_{{ cookiecutter.plugin_name }}():
        raise NotImplementedError

    return _make_{{ cookiecutter.plugin_name }}


@pytest.fixture
def {{ cookiecutter.plugin_name }}(make_{{ cookiecutter.plugin_name }}):
    return make_{{ cookiecutter.plugin_name }}()
