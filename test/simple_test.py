# from bs4 import BeautifulSoup
#
# from modules.collection import crawler
#
# url = 'http://www.mnet.com/artist/1'
# html = crawler.crawling(url)
# bs = BeautifulSoup(html, 'html.parser')
# print(bs)
#
#
from datetime import datetime

asd = '2000.12.00'
asd.split('.')
if len(asd.split('.')) == 3:
    result = datetime.strptime(asd, '%Y.%m.%d')
elif len(asd.split('.')) == 2:
    result = datetime.strptime(asd, '%Y.%m')
elif len(asd.split('.')) == 1:
    result = datetime.strptime(asd, '%Y')

print(result)