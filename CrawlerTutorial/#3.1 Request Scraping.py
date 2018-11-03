import requests
from bs4 import BeautifulSoup



def get():
    print('\nget')
    param = {"q": "台灣"}
    r = requests.get('https://www.google.com.tw/search', params=param)
    print(r.url)
    print(r.text)
    # soup = BeautifulSoup(r.text, features='html.parser')
    # print(soup.prettify())


def post_name():
    print('\npost name')
    # http://pythonscraping.com/pages/files/form.html
    data = {'firstname': 'Albert', 'lastname': 'Ryu'}
    r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
    print(r.url)
    # print(r.headers)
    print(r.text)


def post_image():
    print('\npost image')
    file = {'uploadFile': open('D:\\AlbertRyu\\Pictures\\mico.jpg', 'rb')}
    r = requests.post('http://httpbin.org/post', files=file)
    print(r.text)
    # print(r.json()['files'])
    print(r.json()['files'])


def post_login():
    print('\npost login')
    payload = {'username': 'albertryu', 'pass': 'albertryu'}
    r = requests.post('https://my.freecycle.org/login', data=payload)
    # print(r.cookies.get_dict())
    # r = requests.get('http://my.freecycle.org/home/info')
    r = requests.get('http://my.freecycle.org/home/info', cookies=r.cookies)
    print(r.text)



def session_login():
    print('\nsession login')
    session = requests.Session()
    payload = {'username': 'albertryu', 'pass': 'albertryu'}
    r = session.post('https://my.freecycle.org/login', data=payload)
    print(r.cookies.get_dict())
    r = session.get("http://my.freecycle.org/home/info")
    print(r.text)


# get()
# post_name()
# post_image()
# post_login()
session_login()