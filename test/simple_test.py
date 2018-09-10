from bs4 import BeautifulSoup

from modules.collection import crawler

url = 'http://www.mnet.com/artist/1'
html = crawler.crawling(url)
bs = BeautifulSoup(html, 'html.parser')
print(bs)