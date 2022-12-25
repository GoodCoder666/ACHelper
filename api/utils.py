# -*- coding: utf-8 -*-
import re
from gzip import GzipFile
from http.cookiejar import CookieJar, LWPCookieJar

__all__ = ['decompress_response', 'extract_cookies', 'load_cookies', 'get_username_from_cookiejar', 'HEADERS', 'ADDHEADERS']

UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip',
    'accept-language': 'zh-CN,zh;q=0.9',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
    'user-agent': UA
}

ADDHEADERS = list(HEADERS.items())

def decompress_response(response, encoding: str='utf-8') -> str:
    '''
    Decompress given response with specified encoding. Returns the decoded html.
    '''
    if response.getheader('Content-Encoding') == 'gzip':
        with GzipFile(fileobj=response) as gz:
            return gz.read().decode(encoding)
    return response.read().decode(encoding)

def extract_cookies(cookiejar):
    return '; '.join(f'{item.name}={item.value}' for item in cookiejar)

def load_cookies(filename: str) -> LWPCookieJar:
    cookiejar = LWPCookieJar(filename)
    cookiejar.load()
    return cookiejar

def get_username_from_cookiejar(cookiejar: CookieJar) -> str:
    return re.search(
        r'UserScreenName%3A(.*?)%00',
        cookiejar._cookies['atcoder.jp']['/']['REVEL_SESSION'].value
    )[1]