from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
import urllib

baseUrl = 'https://www.google.com/search?q='
plusUrl = '강아지상+얼굴'

url = baseUrl + quote_plus(plusUrl)
hdr = {'User-Agent': 'Mozilla/5.0', 'referer': 'http://www.google.com'}
req = Request(url, headers=hdr)
html = urlopen(req)

# script 를 다 긁어옴
soup = BeautifulSoup(html, "html.parser")
# print(soup.select('div.islrc'))
a = soup.find_all('img', 'rg_i.Q4LuWd.tx8vctf')
# a = soup.find_all('div', 'BNeawe vvjwJb AP7Wnd')
# a = soup.find_all('a', class_='wXeWr_islib_nfEiy_mM5pbd')
# a = soup.find_all(class_='WddBJd')
# print(soup)  # 웹 문서 전체가 출력됩니다.

for i in a:
    print(i.get('alt'))

print(a)
for i in range(len(a)):
    print("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    print(a[i])
print(len(a))

