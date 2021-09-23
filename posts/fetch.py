"""
Fetches Blog posts.
"""

import pathlib
import yaml

TITLE = 'TITLE'
FILES_DIR = './posts/files'


def fetch():
    posts = []
    for x in pathlib.Path(FILES_DIR).iterdir():
        if x.is_file():
            posts.append(_parse_file(x))
    return posts


def _parse_file(file: pathlib.Path):
    return yaml.safe_load(
        file.read_text()
    )
