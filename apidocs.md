## AtCoder API 文档

### 基础知识

##### `http.cookiejar.LWPCookieJar`

存储用户Cookies的对象。登录后会产生Cookies，登录API会返回一个 `http.cookiejar.LWPCookieJar`对象。此对象可以传给其他需要登录使用的API函数（如提交）。

用法：

- `http.cookiejar.LWPCookieJar.save(filename)`：将cookies保存至filename。
- `http.cookiejar.LWPCookieJar.load(filename)`：从filename读取cookies。
- `api.utils.load_cookies(filename)`：从filename读取cookies，并返回读取的 `LWPCookieJar`对象。

示例：

```python
from api.login import login # 登录API

cookiejar = login('username', 'password') # 登录AtCoder并获取Cookie
cookiejar.save('cookies.txt') # 保存Cookies至cookies.txt
```

此时已成功登录，并保存Cookies。下次使用时直接读取cookie即可，无需再次登录：

```python
from http.cookiejar import LWPCookieJar # 导入LWPCookieJar类

cookiejar = LWPCookieJar() # 创建新的CookieJar
cookiejar.load('cookies.txt') # 从cookies.txt读取cookies

# ---或者：---
from api.utils import load_cookies # 已封装好的读取cookies
cookiejar = load_cookies('cookies.txt') # 与上面等效
```

### api.login.login

登录到AtCoder，返回cookie。示例：

```python
from api.login import login
cookiejar = login('username', 'password') # 指定用户名和密码，返回登录获取的cookiejar
```

请妥善保存cookiejar对象以便后续使用。

### api.submit.submit

向AtCoder提交代码，返回提交记录ID。示例：

```python
from api.login import login
from api.submit import submit

# 准备必需的参数
contest = 'abc123' # 提交的比赛号
problem = 'abc123_a' # 提交的题目编号
code = '（要提交的代码）'
language = '4003' # 提交的语言，4003代表C++ (GCC 9.2.1)
cookiejar = login('username', 'password') # 登录，获取cookie

# 提交代码，获取提交记录ID
sid = submit(contest, problem, code, language, cookiejar)
print(sid)
```

### api.submit.getAvailableLanguages

获取一道题可用的语言。返回值示例：

```python
[
    ('4001', 'C (GCC 9.2.1)'),
    ('4002', 'C (Clang 10.0.0)'),
    ('4003', 'C++ (GCC 9.2.1)'),
    ('4004', 'C++ (Clang 10.0.0)'),
    ('4005', 'Java (OpenJDK 11.0.6)'),
    ...
] # [(语言编号, 语言名称)]
```

### api.submit.get_submission_status

获取提交状态。返回一个元组 `(details, summary)`，其中：

- `details`：细节描述，如 `Accepted`、`Wrong Answer`、`Time Limit Exceeded`、`Waiting for Judging`。
- `summary`：简单概括，如 `AC`、`WA`、`TLE`、`5/12`、`WJ`。

调用方式：`api.submit.get_submission_status(比赛ID, 提交记录ID, cookiejar)`。cookiejar参数可为None，表示不使用cookies。此函数较为简单，故此处不提供示例。

### api.problem.get_markdown

将题面转换为Markdown并保存。示例：

```py
from api.markdown import get_markdown
with open('282-A.md', 'w') as file: # 打开文件
    get_markdown('https://atcoder.jp/contests/abc282/tasks/abc282_a', file) # 保存Markdown至文件
```

若想转换为字符串，可以使用 `io.StringIO`：

```python
from api.markdown import get_markdown
from io import StringIO
with StringIO() as file:
    get_markdown('https://atcoder.jp/contests/abc282/tasks/abc282_a', file)
    file.seek(0)
    markdown = file.read()
print(markdown)
```

### api.problem.get_html

获取题面HTML，数学公式会由`latex2mathml`模块自动转换为mathml。

### api.contest.get_contest_problems

获取一场比赛的题目信息。示例：

```python
>>> get_contest_problems('abc123')
[
    ('abc123_a', 'A', 'Five Antennas', '2 sec', '1024 MB'),
    ('abc123_b', 'B', 'Five Dishes', '2 sec', '1024 MB'),
    ('abc123_c', 'C', 'Five Transportations', '2 sec', '1024 MB'),
    ('abc123_d', 'D', 'Cake 123', '2 sec', '1024 MB')
] # [(题目编号, 题目标题, 时间限制, 空间限制)]
```

### Note

- `api.utils`文件为部分API调用的辅助函数集合，**不要直接调用**。（`load_cookies`方法除外）
- “题目编号”指题目链接中的最后一部分，如 `abc123_a`（而不是 `A`）。
