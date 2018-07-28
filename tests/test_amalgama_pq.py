import json
import pytest
from amalgama import amalgama


@pytest.fixture
def html():
    with open('tests/tests_data/lyrics.html', 'r', encoding='cp1251') as f:
        return f.read()


@pytest.fixture
def result_html():
    with open('tests/tests_data/result.html', 'r') as f:
        return f.read()


def test_get_html(html, result_html):
    assert amalgama.get_html(html) == result_html


def load_json(file_path):
    with open(file_path, 'rb') as f:
        return json.load(f)


parse_functions = [amalgama.get_all_translates_lines, amalgama.get_all_translates, amalgama.get_first_translate_text]
params = {i.__name__: (i, load_json(f'tests/tests_data/{i.__name__}.json'))for i in parse_functions}


@pytest.mark.parametrize('f, data', params.values(), ids=list(params.keys()))
def test_pq(f, data, html):
    assert f(html) == data
