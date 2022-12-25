# -*- coding: utf-8 -*-
import re
from http.cookiejar import LWPCookieJar
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener

from .utils import ADDHEADERS, decompress_response

__all__ = ['login']

csrf_pattern = re.compile(r'var csrfToken = "(.*?)"')
def login(username: str, password: str) -> LWPCookieJar:
    '''
    Login with given username and password.

    Parameters:
    - `username`: Handle or email.
    - `password`: User's password.

    Returns an `http.cookiejar.LWPCookieJar` instance which stores the cookies after logged in.
    '''
    cookiejar = LWPCookieJar()
    opener = build_opener(HTTPCookieProcessor(cookiejar))
    opener.addheaders = ADDHEADERS
    url = 'https://atcoder.jp/login'
    with opener.open(url) as response:
        csrf_token = csrf_pattern.search(decompress_response(response))[1]
    data = {'username': username, 'password': password, 'csrf_token': csrf_token}
    with opener.open(url, urlencode(data).encode('utf-8')) as response:
        if 'Username or Password is incorrect.' in decompress_response(response):
            raise ValueError('Username or Password is incorrect.')
        return cookiejar