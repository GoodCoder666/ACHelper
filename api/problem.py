# -*- coding: utf-8 -*-
import re
from html import unescape
from http.cookiejar import CookieJar
from urllib.request import Request, urlopen

from latex2mathml.converter import convert
from lxml import etree

from .utils import HEADERS, decompress_response, extract_cookies

__all__ = ['get_markdown', 'get_html']

title_pattern = re.compile(r'<title>(.*?)</title>')
limits_pattern = re.compile(r'<p>\W*(Time Limit:.*?)\W*</p>')
problem_pattern = re.compile(r'<span class="lang-en">(.*?)</span>\W*</span>', re.S)

replace_patterns = [
    (re.compile(r'<var>(.*?)</var>'), r'$\1$'), # LaTex
    (re.compile(r'<span class="label.*?>(.*?)</span>'), r'**`\1`**'), # Verdict
    (re.compile(r'<strong>(.*?)</strong>'), r'**\1**'), # Strong
    (re.compile(r'<code>(.*?)</code>'), r'`\1`') # Code
]

def _parse_table(table):
    return '**WARNING: AtCoder Contest Helper recognized a table here, but it is unable to parse it.**\n**Some characters of the table might appear later.**\n\n'

def get_markdown(url: str, output_file, cookiejar: CookieJar=None) -> None:
    '''
    Returns the markdown representation of the given atcoder problem.

    Parameters:
    - `url`: The url of the problem (e.g. `https://atcoder.jp/contests/abc123/tasks/abc123_a`)
    - `output_file`: The output file (e.g. `open('abc123_a.md', 'w')`).
    - `cookiejar`: The `http.cookiejar.CookieJar` instance storing cookies, defaults to none (no cookies).
    '''
    request = Request(url, headers=HEADERS)
    if cookiejar:
        request.add_header('cookie', extract_cookies(cookiejar))
    with urlopen(request) as response:
        html = decompress_response(response).replace('\r\n', '\n')
    output_file.write(f'## {title_pattern.search(html)[1]}\n\n{limits_pattern.search(html)[1]}\n')
    problem_html = problem_pattern.search(html)[1].replace('<br />', '')
    for pattern, repl in replace_patterns:
        problem_html = pattern.sub(repl, problem_html)
    tree = etree.HTML(problem_html)
    title = None
    is_li = False
    for tag in tree.iter():
        if not tag.text:
            if tag.tag == 'img':
                if is_li:
                    output_file.write('\n')
                    is_li = False
                alt = tag.get('alt', '')
                src = tag.get('src')
                output_file.write(f'![{alt}]({src})\n\n')
            continue
        _tag = tag
        text, tag = tag.text.strip(), tag.tag
        if tag == 'li':
            output_file.write(f'- {text}\n')
            is_li = True
        else:
            if is_li:
                output_file.write('\n')
                is_li = False
            if tag == 'h3':
                output_file.write(f'### {text}\n\n')
                title = text
            elif tag == 'p':
                output_file.write(text + '\n\n')
            elif tag == 'summary':
                output_file.write(f'> {text}\n')
            elif tag == 'blockquote':
                output_file.write('> ')
            elif tag == 'pre':
                output_file.write(text + '\n\n' if title in ('Input', 'Output', 'Input and Output') else f'```\n{text}\n```\n\n')
            elif tag == 'table':
                output_file.write(_parse_table(_tag))

def _format_latex(match):
    return convert(unescape(match[1]))

def get_html(url: str, cookiejar: CookieJar=None) -> str:
    '''
    Returns the HTML representation of the given atcoder problem.

    Parameters:
    - `url`: The url of the problem (e.g. `https://atcoder.jp/contests/abc123/tasks/abc123_a`)
    - `cookiejar`: The `http.cookiejar.CookieJar` instance storing cookies, defaults to none (no cookies).
    '''
    request = Request(url, headers=HEADERS)
    if cookiejar:
        request.add_header('cookie', extract_cookies(cookiejar))
    with urlopen(request) as response:
        html = decompress_response(response)
    html = re.sub(r'<var>(.*?)</var>', _format_latex, html)
    title_html = f'<h2>{title_pattern.search(html)[1]}</h2>'
    limits_html = f'<p>{limits_pattern.search(html)[1]}</p>'
    problem_html = problem_pattern.search(html)[1]
    return f'{title_html}<hr/>{limits_html}{problem_html}'