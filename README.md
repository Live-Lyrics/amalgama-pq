# Amalgama-pq 
[![Build Status](https://travis-ci.org/andriyor/amalgama-pq.svg?branch=master)](https://travis-ci.org/andriyor/amalgama-pq)
[![codecov](https://codecov.io/gh/andriyor/amalgama-pq/branch/master/graph/badge.svg)](https://codecov.io/gh/andriyor/amalgama-pq)

Amalgama lyrics scraping

## Installation
```
$ pip install git+https://github.com/andriyor/amalgama-pq.git#egg=amalgama-pq
```

### Requirements
* Python 3.6 and up

### Installation from source
```
$ git clone https://github.com/andriyor/amalgama-pq.git
$ cd amalgama
$ python setup.py install
```

## Usage

```
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

## Development
Install [Pipenv](https://docs.pipenv.org/)   
```
$ pipenv install --dev -e .
```