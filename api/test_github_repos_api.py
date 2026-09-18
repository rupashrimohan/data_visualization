import requests
import pytest


def get_status_code(language):
    url = "https://api.github.com/search/repositories"
    url += f"?q=language:{language}+sort:stars+stars:>1000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    return r.status_code


@pytest.mark.parametrize("language", ["python", "javascript", "ruby"])
def test_status_code_languages(language):
    status_code = get_status_code(language)
    assert status_code == 200
