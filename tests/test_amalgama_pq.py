import pytest
from amalgama import amalgama
import pickle


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


@pytest.fixture
def load_pickle():
    def _load_pickle(file_path):
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    return _load_pickle


def test_get_all_translates_lines(html, load_pickle):
    assert amalgama.get_all_translates_lines(html) == load_pickle('tests/tests_data/get_all_translates_lines')


def test_get_all_translates(html, load_pickle):
    assert amalgama.get_all_translates(html) == load_pickle('tests/tests_data/get_all_translates')


def test_get_first_translate_text(html, load_pickle):
    assert amalgama.get_first_translate_text(html) == load_pickle('tests/tests_data/get_first_translate_text')
