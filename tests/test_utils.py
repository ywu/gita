import pytest

from gita import utils


@pytest.mark.parametrize('test_input, has_remote, expected', [
    ({
        'abc': '/root/repo/'
    }, True, 'abc               \x1b[31mrepo *+   \x1b[0m msg'),
    ({
        'repo': '/root/repo2/'
    }, False, 'repo              \x1b[37mrepo *+   \x1b[0m msg'),
])
def test_describe(test_input, has_remote, expected, monkeypatch):
    monkeypatch.setattr(utils, 'get_head', lambda x: 'repo')
    monkeypatch.setattr(utils, 'has_remote', lambda: has_remote)
    monkeypatch.setattr(utils, 'get_commit_msg', lambda: "msg")
    monkeypatch.setattr('os.chdir', lambda x: None)
    # Returns of os.system determine the repo status
    monkeypatch.setattr('os.system', lambda x: True)
    print('expected: ', repr(expected))
    print('got:      ', repr(utils.describe(test_input)))
    assert expected == utils.describe(test_input)