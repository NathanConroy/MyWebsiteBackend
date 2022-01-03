"""
Fetches Blog posts.
"""

import pathlib as pl
import yaml

TITLE = 'TITLE'
POSTS_DIR = './content/posts'
ABOUT_PAGE = './content/about.yml'

ID = 'id'
ACTIVE = 'active'
AUTHOR = 'author'
DATE = 'date'
# TODO: change name from 'content' (now used as the name for this pkg)
CONTENT = 'content'


def fetch_posts() -> list:
    posts = []
    for f in pl.Path(POSTS_DIR).iterdir():
        if f.is_file():
            _add_post(_parse_file(f), posts)
    return posts


def fetch_about() -> dict:
    return _parse_file(pl.Path(ABOUT_PAGE))


def _parse_file(file: pl.Path) -> dict:
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
