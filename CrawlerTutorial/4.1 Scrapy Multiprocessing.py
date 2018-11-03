from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import multiprocessing as mp
import re
import time

# 回傳 url 的 response
def crawl(url):
    response = urlopen(url)
    # time.sleep(0.1)             # 爬 local 時模擬連外往延遲速度
    return response.read().decode()

# 解析此 response 回傳頁面 title, 此頁面 url, 此頁所有其他 urls
def parse(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')

    title = soup.find('h1').get_text().strip()
    # title = soup.find('title')

    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # remove duplication

    url = soup.find('meta', {'property': "og:url"})['content']
    return title, url, page_urls


if __name__ == '__main__':
    base_url = 'https://morvanzhou.github.io/'
    # base_url = "http://127.0.0.1:4000/"

    unseen = set([base_url,])
    seen = set()

    pool = mp.Pool(2)                       # number strongly affected
    count, t1 = 1, time.time()
    # count = 1
    # t1 = time.time()

    while len(unseen) != 0:              # still get some url to visit
        if len(seen) > 20:               # 測試只爬 20 頁，爬太多可能會被鎖 IP
            break

        # crawling
        print('\nDistributed Crawling...')
        crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
        htmls = [j.get() for j in crawl_jobs]                                       # request connection
        htmls = [h for h in htmls if h is not None]     # remove None

        # parsing
        print('\nDistributed Parsing...')
        parse_jobs = [pool.apply_async(parse, args=(html, base_url,)) for html in htmls]
        results = [j.get() for j in parse_jobs]                                     # parse html
        # for j in parse_jobs:
        #     print(j)
        print(results)
        print('\nAnalysing...')
        seen.update(unseen)
        unseen.clear()

        for title, url, page_urls in results:
                print(count, title, url)
                count += 1
                unseen.update(page_urls - seen)

    print('Total time: %.1f s' % (time.time()-t1, ))