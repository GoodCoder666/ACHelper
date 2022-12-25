# -*- coding: utf-8 -*-
import re
from html import unescape
from http.cookiejar import CookieJar
from urllib.request import Request, urlopen

from .utils import HEADERS, decompress_response, extract_cookies

__all__ = ['get_contest_problems']

row_pattern = re.compile(r'<tr>\W+?<td.*?href=".+?tasks/(.+?)">(.+?)<.+?<td>.+?>(.+?)</a>.*?<td.*?>(.+?)</td>.+?>(.*?)<', re.S)
def get_contest_problems(contest: str, cookiejar: CookieJar=None) -> list:
    '''
    Returns a list of problems in a contest.

    Example:
    ```
    >>> get_contest_problems('abc123')
    [
        ('abc123_a', 'A', 'Five Antennas', '2 sec', '1024 MB'),
        ('abc123_b', 'B', 'Five Dishes', '2 sec', '1024 MB'),
        ('abc123_c', 'C', 'Five Transportations', '2 sec', '1024 MB'),
        ('abc123_d', 'D', 'Cake 123', '2 sec', '1024 MB')
    ]
    ```
    '''
    request = Request(f'https://atcoder.jp/contests/{contest}/tasks', headers=HEADERS)
    if cookiejar:
        request.add_header('cookie', extract_cookies(cookiejar))
    with urlopen(request) as response:
        html = decompress_response(response)
    return [
        (pid, taskid, unescape(title), tl, ml)
        for pid, taskid, title, tl, ml in row_pattern.findall(html)
    ]