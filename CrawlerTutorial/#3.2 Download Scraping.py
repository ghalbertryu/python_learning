import os
os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png"
# IMAGE_URL = "https://www.google.com.tw/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png"


def urllib_download():
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './img/image1.png')      # whole document


def request_download():
    import requests
    r = requests.get(IMAGE_URL)
    # print(r.headers)
    # print(r.content)
    # print(r.text)
    with open('./img/image2.png', 'wb') as f:
        f.write(r.content)                      # whole document
    # f = open('./img/image2.png', 'wb')
    # f.write(r.content)
    # f.close()


def chunk_download():
    import requests
    r = requests.get(IMAGE_URL, stream=True)    # stream loading

    with open('./img/image4.png', 'wb') as f:
        for chunk in r.iter_content(chunk_size=10000):
            f.write(chunk)


# urllib_download()
# print('download image1')
# request_download()
# print('download image2')
chunk_download()
print('download image3')