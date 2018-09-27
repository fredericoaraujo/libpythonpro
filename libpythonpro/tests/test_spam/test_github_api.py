from unittest.mock import Mock

import pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url_avatar = "https://avatars3.githubusercontent.com/u/3457115?v=4"
    resp_mock.json.return_value = {
        "login": "renzon",
        "avatar_url": url_avatar,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url_avatar
    github_api.requests.get = get_original


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('renzon')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars3.githubusercontent.com/u/402714?v=4' == url