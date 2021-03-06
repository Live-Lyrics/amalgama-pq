# Amalgama-pq 
[![image](https://img.shields.io/pypi/v/amalgama.svg)](https://pypi.org/project/amalgama/)
[![image](https://img.shields.io/pypi/l/amalgama.svg)](https://pypi.org/project/amalgama/)
[![image](https://img.shields.io/pypi/pyversions/amalgama.svg)](https://pypi.org/project/amalgama/)
[![Build Status](https://travis-ci.org/Live-Lyrics/amalgama-pq.svg?branch=master)](https://travis-ci.org/Live-Lyrics/amalgama-pq)
[![codecov](https://codecov.io/gh/Live-Lyrics/amalgama-pq/branch/master/graph/badge.svg)](https://codecov.io/gh/Live-Lyrics/amalgama-pq)

Amalgama lyrics scraping

### Requirements
* Python 3.5 and up

## Installation
from PyPI
```
$ pip install amalgama
```

from git repository
```
$ pip install git+https://github.com/andriyor/amalgama-pq.git#egg=amalgama-pq
```

from source
```
$ git clone https://github.com/andriyor/amalgama-pq.git
$ cd amalgama-pq
$ python setup.py install
```

## Usage

```python
import requests

import amalgama

artist, song = 'Pink Floyd', 'Time'
url = amalgama.get_url(artist, song)
try:
    response = requests.get(url)
    response.raise_for_status()
    text = amalgama.get_first_translate_text(response.text)
    print(f'{text}{url}')
except requests.exceptions.HTTPError:
    print(f'{artist}-{song} not found in amalgama {url}')
```

Expected output 
```
Time (оригинал Pink Floyd)

Ticking away the moments that make up a dull day
You fritter and waste the hours in an off hand way
Kicking around on a piece of ground in your home town
Waiting for someone or something to show you the way
...

Время (перевод Дмитрий Попов из Новокузнецка)

Тикают секунды, наполняя скучный день,
Ты разбрасываешься по мелочам и понапрасну тратишь время,
Вертишься вокруг клочка земли родного города,
В ожидании, что кто-то или что-то укажет тебе путь.
...
```

## Development setup
Using [Poetry](https://poetry.eustace.io/docs/)   
```
$ poetry install
```
run tests
```
$ poetry run pytest
```
or [Pipenv](https://docs.pipenv.org/)   
```
$ pipenv install --dev -e .
```

## License
[MIT](https://choosealicense.com/licenses/mit/)