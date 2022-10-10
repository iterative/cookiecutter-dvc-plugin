import pytest
from dvc.testing.api_tests import (  # noqa, pylint: disable=unused-import
    TestAPI,
)
from dvc.testing.remote_tests import (  # noqa, pylint: disable=unused-import
    TestRemote,
)
from dvc.testing.workspace_tests import TestAdd as _TestAdd
from dvc.testing.workspace_tests import (  # noqa, pylint: disable=unused-import
    TestGetUrl,
)
from dvc.testing.workspace_tests import TestImport as _TestImport
from dvc.testing.workspace_tests import (  # noqa, pylint: disable=unused-import
    TestLsUrl,
)


@pytest.fixture
def cloud(make_cloud):
    yield make_cloud(typ="{{ cookiecutter.plugin_name }}")


@pytest.fixture
def remote(make_remote, cloud_name):
    yield make_remote(name="upstream", typ="{{ cookiecutter.plugin_name }}")


@pytest.fixture
def workspace(make_workspace, cloud_name):
    yield make_workspace(name="workspace", typ="{{ cookiecutter.plugin_name }}")


class TestImport(_TestImport):
    @pytest.fixture
    def stage_md5(self):
        raise NotImplementedError


    @pytest.fixture
    def is_object_storage(self):
        raise NotImplementedError


    @pytest.fixture
    def dir_md5(self):
        raise NotImplementedError


class TestAdd(_TestAdd):
    @pytest.fixture
    def hash_name():
        raise NotImplementedError


    @pytest.fixture
    def hash_value():
        raise NotImplementedError


    @pytest.fixture
    def dir_hash_value(dir_md5):
        raise NotImplementedError
