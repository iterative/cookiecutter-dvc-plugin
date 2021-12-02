import locale
import os
import uuid

import pytest
from dvc.testing.cloud import Cloud
from dvc.testing.fixtures import *  # noqa, pylint: disable=wildcard-import,unused-import
from dvc.testing.path_info import CloudURLInfo
from funcy import cached_property

class {{ cookiecutter.plugin_name|upper }}S3(Cloud, CloudURLInfo):
    @property
    def config(self):
        return {"url": self.url}

    def is_file(self):
        raise NotImplementedError

    def is_dir(self):
        raise NotImplementedError

    def exists(self):
        raise NotImplementedError

    def mkdir(self, mode=0o777, parents=False, exist_ok=False):
        raise NotImplementedError

    def write_bytes(self, contents):
        raise NotImplementedError

    def read_bytes(self):
        raise NotImplementedError

    @property
    def fs_path(self):
        raise NotImplementedError


@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return os.path.join(
        str(pytestconfig.rootdir), "dvc_{{ cookiecutter.plugin_name }}", "tests", "docker-compose.yml"
    )


@pytest.fixture
def make_{{ cookiecutter.plugin_name }}():
    def _make_{{ cookiecutter.plugin_name }}():
        raise NotImplementedError

    return _make_{{ cookiecutter.plugin_name }}


@pytest.fixture
def {{ cookiecutter.plugin_name }}s3(make_{{ cookiecutter.plugin_name }}):
    return make_{{ cookiecutter.plugin_name }}()

