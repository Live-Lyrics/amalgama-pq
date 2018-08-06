import requests
from chopper.extractor import Extractor

HTML = requests.get("https://www.amalgama-lab.com/songs/a/adele/hello.html").text
CSS = requests.get("https://www.amalgama-lab.com/style.css?v=1.7").text

extractor = Extractor.keep('//div[@class="texts col"]').discard('//div[@class="noprint"]').discard('//div[@id="quality"]')
html, css = extractor.extract(HTML, CSS)

with open('amalgama_lyrics.html', 'w') as f:
    f.write(html)

with open('amalgama_lyrics.css', 'w') as f:
    f.write(css)
