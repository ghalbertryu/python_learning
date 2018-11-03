from bs4 import BeautifulSoup
from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')

soup = BeautifulSoup(html, features='html.parser')
# print(soup.prettify())

# $('[href]')
find = soup.find_all(href=True)
# print(find)

# $('*').not('[href]')
find = soup.find_all(href=False)
# print(find)

# $('[class='month']')
find = soup.find_all(class_='month')
# print([ele.string for ele in find])

# $('li[class="month"]')
# use class to narrow search
month = soup.find_all('li', attrs={"class": "month"})
month = soup.find_all('li', {"class": "month"})
# for m in month:
    # print(m.get_text())
    # print(m.string)

# $('ul.jan li')
# $('ul.jan').find('li')
# jan = soup.find('ul', class_='jan')
# d_jan = jan.find_all('li')              # use jan as a parent
# for d in d_jan:
#     print(d.get_text())

jan = soup.select('.month')
for d in jan:
    print(d.get_text())