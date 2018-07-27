import pickle
from amalgama import amalgama


def update_html():
    import requests
    response = requests.get('https://www.amalgama-lab.com/songs/r/red_hot_chili_peppers/californication.html')
    with open('tests/tests_data/lyrics.html', 'w', encoding='cp1251') as f:
        f.write(response.text)

    with open('tests/tests_data/lyrics.html', 'r', encoding='cp1251') as f:
        result_html = amalgama.get_html(f.read())
        with open('tests/pickle_data/result.html', 'w') as f:
            f.write(result_html)

    return response.text


# html = update_html()

with open('tests/tests_data/lyrics.html', 'r', encoding='cp1251') as f:
    html = f.read()

parse_functions = [amalgama.get_all_translates_lines, amalgama.get_all_translates, amalgama.get_first_translate_text]

for f in parse_functions:
    with open(f'tests/tests_data/{f.__name__}', 'wb') as file:
        pickle.dump(f(html), file)
