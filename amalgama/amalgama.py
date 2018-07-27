from pyquery import PyQuery as pq


def build_url(s):
    s = s.lower()
    s = s.replace(' ', '_')
    s = s.replace('$', 's')
    s = s.replace('/', 'and')
    s = s.replace('&', 'and')
    s = s.replace('.', '')
    s = s.replace("'", '_')
    s = s.replace("__", '_')
    return s


def get_url(artist, title):
    artist, title = map(build_url, [artist, title])
    if 'the' in artist:
        artist = artist[4:]
    amalgama_url = f"https://www.amalgama-lab.com/songs/{artist[0]}/{artist}/{title}.html"
    return amalgama_url


def get_html(html):
    d = pq(html)
    d('script').remove()
    text = d(".texts.col")
    text('div#quality').remove()
    text('div.noprint').remove()
    return text.html()


def get_all_translates_lines(html):
    d = pq(html)
    lines = [f"{d('h2.translate').text()}\n\n"]
    for i in d('div.translate'):
        t = pq(i).text()
        if t:
            if t[0].isdigit():
                lines.append(t)
            else:
                lines.append(f"{t}\n")
        else:
            lines.append('\n')
    return lines


def split_before(iterable, pred):
    buf = []
    for item in iterable:
        if pred(item) and buf:
            yield buf
            buf = []
        buf.append(item)
    yield buf


def get_all_translates(html):
    lines = get_all_translates_lines(html)
    translations = list(split_before(lines, lambda s: '(перевод' in s))
    return translations


def get_first_translate_text(html):
    translations = get_all_translates(html)
    return ''.join(translations[0])


if __name__ == '__main__':
    import requests
    artist, song = 'Pink Floyd', 'Time'
    url = get_url(artist, song)
    try:
        response = requests.get(url)
        response.raise_for_status()
        text = get_first_translate_text(response.text)
        print(f'{text}{url}')
    except requests.exceptions.HTTPError:
        print(f'{artist}-{song} not found in amalgama {url}')
