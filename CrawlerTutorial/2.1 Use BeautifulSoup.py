from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')
# print(soup)
# print(soup.h1.name)
# print(soup.a.string)
# print('\n', soup.p)

# $('a')
all_href = soup.find_all('a')
# print('\n', all_href)
all_href = [element['href'] for element in all_href]
print('\n', all_href)