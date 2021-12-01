import requests

import sys

def shortener(target_url):

    shrt_url = "http://qps.ru/api?url={tg_url}"

    req = requests.get(shrt_url.format(tg_url=target_url))

    

    shortened_url = req.content.decode("utf-8")

    return shortened_url
