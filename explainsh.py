#!/usr/bin/env python3

import html
import re
import sys
import urllib.parse
import urllib.request

CYAN = '\x1b[36m'
GREEN = '\x1b[32m'
RED = '\x1b[31m'
RESET = '\x1b[0m'
YELLOW = '\x1b[33m'


def explainsh():
    cmd = urllib.parse.quote(' '.join(sys.argv[1:]))

    res = get_url(f'https://explainshell.com/explain?cmd={cmd}')

    if 'missing man page' in res.lower():
        return missing_manpages(res)

    params = re.findall(
        r'<pre.*?>([\s\S]*?)</pre>', res, re.MULTILINE)
    manpages = re.findall(
        r'source manpages:\s*\n<a href="(.*?)">.*?</a>', res, re.MULTILINE)

    results = []
    results += map(parse_params, params)
    results += map(parse_manpages, manpages)

    print()
    print('\n\n'.join(results))


def print_help():
    print(f'\n{RED}Usage: explainsh <command>{RESET}')
    print('\nWrap <command> between single quotes if it contains')
    print('special characters: ! " # $ & \' ( ) * ; < > ? [ \\ ] ` { | } ~')

    res = get_url('https://explainshell.com/')
    res = res[res.index('<h3>examples</h3>'):]

    examples = re.findall(r'<li><a.*?>(.*?)</a></li>', res)
    examples = list(map(wrap_with_quotes, examples))

    print(f'\nExamples:')
    print('\n       explainsh '.join([''] + examples))


def get_url(url: str) -> str:
    try:
        return html.unescape(urllib.request.urlopen(url).read().decode())
    except:
        print(f'\n{RED}Some error ocurred while fetching {url}{RESET}')
        sys.exit(1)


def parse_params(res: str) -> str:
    res = res.replace('<u>', CYAN).replace('<b>', RED)
    res = re.sub(r'<a.*?>', YELLOW, res)
    return re.sub(r'</a>|</b>|</u>', RESET, res)


def parse_manpages(res: str) -> str:
    return GREEN + res + RESET


def wrap_with_quotes(cmd: str) -> str:
    if len(re.findall(r'[!"#\$&\'\(\)\*;<>\?\[\\\]`\{\|\}~]', cmd)) > 1:
        cmd = "'" + cmd.replace("'", "''") + "'"

    return cmd


def missing_manpages(res: str):
    program = re.findall(r'<span class="program-text">(.*?)</span>', res)[0]
    print(f'\n{RED}MISSING MAN PAGE{RESET}')
    print(f'\nNo man page found for {CYAN}{program}{RESET}.')


def main():
    if len(sys.argv) == 1:
        print_help()
        sys.exit(1)

    explainsh()


if __name__ == '__main__':
    main()
