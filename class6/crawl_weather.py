import requests
import time
from io import open

region = 'Hsinchu'
#url = 'https://www.cwb.gov.tw/V7/observe/24real/Data/C0D58.htm'
url = "https://www.cwb.gov.tw/V7/observe/24real/Data/46757.htm"
url1 = "https://tw.futures.finance.yahoo.com/future/options.html?opmr=optionfull&opcm=WTX1&opym=201811W1"


def f(url, fn):
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
    }
    res = requests.get(url1, headers=headers)
    res.encoding = 'utf-8'

    open(fn, 'wb').write(res.text.encode('utf-8'))


fn = region + '.html'.format(0, 0)
f(url, fn)
