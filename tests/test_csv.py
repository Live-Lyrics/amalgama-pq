import csv

import pytest

from amalgama.amalgama import get_url


def get_amalgama():
    with open("tests/test.csv") as f:
        records = csv.DictReader(f)
        l = [(row['artist'], row['title'], row['amalgama']) for row in records]
    return l


@pytest.mark.parametrize("artist, title, amalgama", get_amalgama())
def test_amalgama(artist, title, amalgama):
    assert get_url(artist, title) == amalgama
