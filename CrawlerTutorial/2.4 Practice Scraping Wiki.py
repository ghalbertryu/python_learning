from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


base_url = "https://zh.wikipedia.org"
his = ["/wiki/taiwan"]

for i in range(10):
    # dealing with Chinese symbols
    url = base_url + his[i]

    html = urlopen(url).read().decode('utf-8')
    soup = BeautifulSoup(html, features='html.parser')
    print(i, soup.find('h1').get_text(), '    url: ', his[i])

    # find valid urls
    sub_urls = soup.find_all("a", {"href": re.compile("/wiki/(%.{2})+$")})

    if len(sub_urls) != 0:
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:
        # no valid sub link found
        his.pop()