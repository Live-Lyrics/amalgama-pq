from amalgama import amalgama
import pytest

split_before_params = {
    'starts_with_sep': ('xooxoo', [['x', 'o', 'o'], ['x', 'o', 'o']]),
    'ends_with_sep': ('ooxoox', [['o', 'o'], ['x', 'o', 'o'], ['x']]),
    'no_sep': ('ooo', [['o', 'o', 'o']])
}


@pytest.mark.parametrize("iterable,expected", split_before_params.values(), ids=list(split_before_params.keys()))
def test_split_before(iterable, expected):
    actual = list(amalgama.split_before(iterable, lambda c: c == 'x'))
    assert actual == expected
