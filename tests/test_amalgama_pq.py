import json
import pytest
from amalgama import amalgama


@pytest.fixture
def html():
    with open("tests/tests_data/lyrics.html", "r", encoding="cp1251") as f:
        return f.read()


@pytest.fixture
def result_html():
    with open("tests/tests_data/result.html", "r") as f:
        return f.read()


def test_get_html(html, result_html):
    assert amalgama.get_html(html) == result_html


def load_json(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


parse_functions = [amalgama.get_all_translates_lines, amalgama.get_all_translates, amalgama.get_first_translate_text,
                   amalgama.get_all_original_lines]
params = {i.__name__: (i, load_json("tests/tests_data/{}.json".format(i.__name__))) for i in parse_functions}


@pytest.mark.parametrize("f, data", params.values(), ids=list(params.keys()))
def test_pq_translate(f, data, html):
    assert f(html) == data


parse_originals = [amalgama.get_all_originals, amalgama.get_first_original_text]
params_originals = {i.__name__: (i, load_json("tests/tests_data/{}.json".format(i.__name__))) for i in parse_originals}
song = "Californication"


@pytest.mark.parametrize("f, data", params_originals.values(), ids=list(params_originals.keys()))
def test_pq_original(f, data, html):
    assert f(html, song) == data
