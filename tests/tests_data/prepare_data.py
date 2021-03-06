import json
from amalgama import amalgama


def update_html():
    import requests

    response = requests.get("https://www.amalgama-lab.com/songs/r/red_hot_chili_peppers/californication.html")
    with open("tests/tests_data/lyrics.html", "w", encoding="cp1251") as f:
        f.write(response.text)

    with open("tests/tests_data/lyrics.html", "r", encoding="cp1251") as f:
        result_html = amalgama.get_html(f.read())
        with open("tests/pickle_data/result.html", "w") as f:
            f.write(result_html)

    return response.text


# html = update_html()

with open("tests/tests_data/lyrics.html", "r", encoding="cp1251") as f:
    html = f.read()

parse_functions = [amalgama.get_all_translates_lines, amalgama.get_all_translates, amalgama.get_first_translate_text,
                   amalgama.get_all_original_lines]

for f in parse_functions:
    with open("tests/tests_data/{}.json".format(f.__name__), "w", encoding="utf-8") as outfile:
        json.dump(f(html), outfile, ensure_ascii=False)


parse_originals = [amalgama.get_all_originals, amalgama.get_first_original_text]
song = "Californication"
for f in parse_originals:
    with open("tests/tests_data/{}.json".format(f.__name__), "w", encoding="utf-8") as outfile:
        json.dump(f(html, song), outfile, ensure_ascii=False)
