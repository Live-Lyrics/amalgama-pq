from bs4 import BeautifulSoup


def get_html(html):
    soup = BeautifulSoup(html, "html5lib")
    texts_col = soup.find("div", {"class": "texts col"})
    title = texts_col.find("div", {"style": "overflow:hidden;"})
    lyrics = texts_col.find("div", {"id": "click_area"})
    lyrics.find("div", {"id": "quality"}).decompose()
    for script in lyrics("script"):
        script.decompose()
    return f"{title}\n{lyrics}"


def get_translate_text(html):
    soup = BeautifulSoup(html, "html.parser")
    s = ''
    for strong_tag in soup.find_all("div", class_="translate"):
        if '\n' in strong_tag.text:
            s += strong_tag.text
        else:
            s += strong_tag.text + '\n'
    return s

