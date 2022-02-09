"""
Fetches Blog posts.
"""

import pathlib as pl
import yaml

TITLE = 'TITLE'

ID = 'id'
ACTIVE = 'active'
AUTHOR = 'author'
DATE = 'date'
# TODO: change name from 'content' (now used as the name for this pkg)
CONTENT = 'content'

# Post Versions
V1 = 1
V2 = 2

V1_POSTS_DIR = './content/posts'
V2_POSTS_DIR = './content/posts_v2'
ABOUT_PAGE = './content/about.yml'

VERSION_DIR = {
    V1: V1_POSTS_DIR,
    V2: V2_POSTS_DIR,
}


def fetch_posts(version=V1) -> list:
    posts = []
    posts_dir = VERSION_DIR[version]  # TODO: raise error if no version
    for f in pl.Path(posts_dir).iterdir():
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
