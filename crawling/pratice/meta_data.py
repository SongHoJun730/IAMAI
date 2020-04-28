from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.python.org/about")
bsObject = BeautifulSoup(html, "html.parser")


for meta in bsObject.head.find_all('meta'):
    print(meta.get('content'))