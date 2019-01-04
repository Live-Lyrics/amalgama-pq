from typing import List, Callable, Iterable

from pyquery import PyQuery as pq
from slugify import slugify


def get_url(artist: str, title: str) -> str:
    title = slugify(title, replacements=[["&", "and"]], separator="_")
    if artist.lower().startswith("the"):
        artist = artist[4:]
        artist = slugify(artist, replacements=[[".", "_"], ["$", "s"], ["+", "and"]], separator="_")
    else:
        artist = slugify(artist, replacements=[[".", ""], ["$", "s"], ["+", "and"]], separator="_")
    amalgama_url = f"https://www.amalgama-lab.com/songs/{artist[0].lower()}/{artist}/{title}.html"
    return amalgama_url


def get_html(html: str) -> str:
    d = pq(html)
    d("script").remove()
    text = d(".texts.col")
    text("div#quality").remove()
    text("div.noprint").remove()
    return text.html()


def get_all_translates_lines(html: str) -> List[str]:
    d = pq(html)
    lines = [f"{d('h2.translate').text()}\n\n"]
    for i in d("div.translate"):
        t = pq(i).text()
        if t:
            if t[0].isdigit():
                lines.append(t)
            else:
                lines.append(f"{t}\n")
        else:
            lines.append("\n")
    return lines


def get_all_original_lines(html: str) -> List[str]:
    d = pq(html)
    lines = [f"{d('h2.original').text()}\n\n"]
    for i in d("div.original"):
        t = pq(i).text()
        if t:
            lines.append(f"{t}\n")
        else:
            lines.append("\n")
    return lines


def split_before(iterable: Iterable[str], pred: Callable[[str], bool]) -> Iterable[List[str]]:
    buf: List[str] = []
    for item in iterable:
        if pred(item) and buf:
            yield buf
            buf = []
        buf.append(item)
    yield buf


def get_all_translates(html: str) -> List[List[str]]:
    lines = get_all_translates_lines(html)
    translations = list(split_before(lines, lambda s: "(перевод" in s))
    return translations


def get_all_originals(html: str,  song: str) -> List[List[str]]:
    lines = get_all_original_lines(html)
    translations = list(split_before(lines, lambda s: song in s))
    return translations


def get_first_translate_text(html: str) -> str:
    translations = get_all_translates(html)
    return "".join(translations[0])


def get_first_original_text(html: str, song: str) -> str:
    translations = get_all_originals(html, song)
    return "".join(translations[0])


if __name__ == "__main__":
    import requests

    artist_name, song_name = "Pink Floyd", "Time"
    url = get_url(artist_name, song_name)
    try:
        response = requests.get(url)
        response.raise_for_status()
        lyrics = get_first_original_text(response.text, song_name)
        lyrics_translate = get_first_translate_text(response.text)
        print(lyrics)
        print(lyrics_translate)
    except requests.exceptions.HTTPError:
        print(f"{artist_name}-{song_name} not found in amalgama {url}")
