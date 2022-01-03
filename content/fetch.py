"""
Fetches Blog posts.
"""

import pathlib
import yaml

TITLE = 'TITLE'
FILES_DIR = './content/files'

ID = 'id'
ACTIVE = 'active'
AUTHOR = 'author'
DATE = 'date'
# TODO: change name from 'content' (now used as the name for this pkg)
CONTENT = 'content'


def fetch_posts():
    posts = []
    for f in pathlib.Path(FILES_DIR).iterdir():
        if f.is_file():
            _add_post(_parse_file(f), posts)
    return posts


def _parse_file(file: pathlib.Path):
    return yaml.safe_load(
        file.read_text()
    )


def _add_post(post, posts):
    if is_active(post):
        posts.append(post)


def is_active(post):
    return post[ACTIVE]


if __name__ == '__main__':
    print(fetch())
