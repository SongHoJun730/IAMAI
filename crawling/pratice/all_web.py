from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import urllib

# html = urlopen("http://www.google.com")
# html = urlopen("https://www.google.com/search?q=강아지상+얼굴")
baseUrl = 'https://www.google.com/search?q='
plusUrl = '강아지상+얼굴'
# crawl_num = int(input('크롤링할 갯수 입력(최대 50개): '))

url = baseUrl + quote_plus(plusUrl)

hdr = {'User-Agent':'Mozilla/5.0', 'referer':'http://www.google.com'}

req = Request(url, headers=hdr)


html = urlopen(req)

bsObject = BeautifulSoup(html, "html.parser")


print(bsObject) # 웹 문서 전체가 출력됩니다.