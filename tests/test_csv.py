import csv

import pytest

from amalgama import amalgama

with open("tests/tests_data/test.csv") as f:
    records = csv.DictReader(f)
    csv_data = [(row['artist'], row['title'], row['url']) for row in records]


@pytest.mark.parametrize("artist,title,url",  csv_data)
def test_amalgama(artist, title, url):
    assert amalgama.get_url(artist, title) == url

