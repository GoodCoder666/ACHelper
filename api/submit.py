# -*- coding: utf-8 -*-
import re
from html import unescape
from http.cookiejar import CookieJar
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener, Request, urlopen
from .utils import HEADERS, ADDHEADERS, decompress_response, extract_cookies

__all__ = ['submit', 'get_submission_status', 'getAvailableLanguages']

csrf_pattern = re.compile(r'var csrfToken = "(.*?)"')
sid_pattern = re.compile(r'<a href=".*?/submissions/(\d+)">')
status_pattern = re.compile(r'<td id="judge-status".*?><span.*?title="(.*?)">(.*?)</span>')
language_pattern = re.compile(r'<option value="(.*?)".*?>(.*?)</option>')

def getAvailableLanguages(contest: str, problem: str, cookiejar: CookieJar) -> list:
    '''
    Returns a list of available languages to submit.

    Parameters:
    - `contest`: The contest id (e.g. `abc123`).
    - `problem`: The problem to submit code to (e.g. `abc123_a`).
    - `cookiejar`: `http.cookiejar.CookieJar` instance storing the user cookies (must be logged in).

    Returns a list of tuples, such as:
    ```
    [
        ('4001', 'C (GCC 9.2.1)'),
        ('4002', 'C (Clang 10.0.0)'),
        ('4003', 'C++ (GCC 9.2.1)'),
        ('4004', 'C++ (Clang 10.0.0)'),
        ('4005', 'Java (OpenJDK 11.0.6)'),
        ...
    ]
    ```
    '''
    request = Request(f'https://atcoder.jp/contests/{contest}/submit', headers=HEADERS)
    if cookiejar:
        request.add_header('cookie', extract_cookies(cookiejar))
    with urlopen(request) as response:
        html = decompress_response(response)
    html = re.search(f'<div id="select-lang-{problem}">(.*?)</div>', html, re.S)[1]
    return [
        (lid, unescape(language))
        for lid, language in language_pattern.findall(html)
    ]

def submit(contest: str, problem: str, code: str, language: str, cookiejar: CookieJar) -> str:
    '''
    Submit code to a specified problem in a contest.

    Parameters:
    - `contest`: The contest id (e.g. `abc123`).
    - `problem`: The problem to submit code to (e.g. `abc123_a`).
    - `code`: The code to submit.
    - `language`: The language of the code (e.g. `4003`).
    - `cookiejar`: `http.cookiejar.CookieJar` instance storing the user cookies (must be logged in).

    About the `language` parameter, in most cases:
    - `4001` stands for `C (GCC 9.2.1)`.
    - `4003` stands for `C++ (GCC 9.2.1)`.
    - `4006` stands for `Python (3.8.2)`.
    - `4047` stands for `PyPy3 (7.3.0)`.

    Available languages can be get with the `getAvailableLanguages()` method.

    Returns the submission ID of the submitted code.
    '''
    opener = build_opener(HTTPCookieProcessor(cookiejar))
    opener.addheaders = ADDHEADERS
    url = f'https://atcoder.jp/contests/{contest}/submit'
    with opener.open(url) as response:
        csrf_token = csrf_pattern.search(decompress_response(response))[1]
    data = urlencode({
        'data.TaskScreenName': problem,
        'data.LanguageId': language,
        'sourceCode': code,
        'csrf_token': csrf_token
    }).encode('utf-8')
    with opener.open(url, data) as response:
        try:
            return sid_pattern.search(decompress_response(response))[1]
        except TypeError:
            raise ValueError('Submission failed.')

def get_submission_status(contest: str, submission_id: str, cookiejar: CookieJar=None) -> tuple:
    '''
    Returns the status of some submission in a contest.
    When the contest has not ended, cookies are required to look at the submission.

    Parameters:
    - `contest`: Contest ID.
    - `submission_id`: Submission ID.
    - `cookiejar`: `http.cookiejar.CookieJar` instance storing the user's cookies.
    '''
    opener = build_opener()
    if cookiejar:
        opener.add_handler(HTTPCookieProcessor(cookiejar))
    opener.addheaders = ADDHEADERS
    with opener.open(f'https://atcoder.jp/contests/{contest}/submissions/{submission_id}') as response:
        html = decompress_response(response)
    return status_pattern.search(html).groups()