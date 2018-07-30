from typing import List, Callable, Iterable

from pyquery import PyQuery as pq


class Amalgama:
    def __init__(self, artist: str, title: str) -> None:
        self.artist = artist
        self.title = title

    @staticmethod
    def _build_url(s: str) -> str:
        s = s.lower()
        s = s.replace(" ", "_")
        s = s.replace("$", "s")
        s = s.replace("/", "and")
        s = s.replace("&", "and")
        s = s.replace(".", "")
        s = s.replace("'", "_")
        s = s.replace("__", "_")
        return s

    @property
    def url(self) -> str:
        artist, title = map(self._build_url, [self.artist, self.title])
        if "the" in artist:
            artist = artist[4:]
        amalgama_url = f"https://www.amalgama-lab.com/songs/{artist[0]}/{artist}/{title}.html"
        return amalgama_url

    @staticmethod
    def get_html(html: str) -> str:
        d = pq(html)
        d("script").remove()
        text = d(".texts.col")
        text("div#quality").remove()
        text("div.noprint").remove()
        return text.html()

    @staticmethod
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

    @staticmethod
    def _split_before(iterable: Iterable[str], pred: Callable[[str], bool]) -> Iterable[List[str]]:
        buf: List[str] = []
        for item in iterable:
            if pred(item) and buf:
                yield buf
                buf = []
            buf.append(item)
        yield buf

    def get_all_translates(self, html: str) -> List[List[str]]:
        lines = self.get_all_translates_lines(html)
        translations = list(self._split_before(lines, lambda s: "(перевод" in s))
        return translations

    def get_first_translate_text(self, html: str) -> str:
        translations = self.get_all_translates(html)
        return "".join(translations[0])


if __name__ == '__main__':
    import requests

    amalgama = Amalgama('Pink Floyd', 'Time')
    try:
        response = requests.get(amalgama.url)
        response.raise_for_status()
        text = amalgama.get_first_translate_text(response.text)
        print(f"{text}{amalgama.url}")
    except requests.exceptions.HTTPError:
        print(f"{amalgama.artist}-{amalgama.title} not found in amalgama {amalgama.url}")
