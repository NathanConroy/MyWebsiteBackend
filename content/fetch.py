"""
Fetches Blog posts.
"""
import typing as typ
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
V1 = 'v1'
V2 = 'v2'

V1_POSTS_DIR = './content/posts'
V2_POSTS_DIR = './content/posts_v2'
ABOUT_PAGE = './content/about.yml'

VERSION_DIR = {
    V1: V1_POSTS_DIR,
    V2: V2_POSTS_DIR,
}


def fetch_posts(version=V1) -> list:
    posts = []
    for f in _iter_post_files(version):
        _add_post(_parse_file(f), posts)
    return posts


def fetch_post(post_id, version=V1) -> typ.Optional[dict]:
    for f in _iter_post_files(version):
        if _file_matches_id(f, post_id):
            return _parse_file(f)
    return None


def _iter_post_files(version):
    posts_dir = VERSION_DIR[version] # TODO: handle error if no version
    yield from filter(lambda f: f.is_file(), _iter_files_in_dir(posts_dir))


def _iter_files_in_dir(directory):
    yield from pl.Path(directory).iterdir()


def _file_matches_id(f, fid):
    file_dict = _parse_file(f)
    return fid == file_dict[ID]


def fetch_about() -> dict:
    return _parse_file(pl.Path(ABOUT_PAGE))


def _parse_file(f: pl.Path) -> dict:
    return yaml.safe_load(
        f.read_text()
    )


def _add_post(post, posts):
    if is_active(post):
        posts.append(post)


def is_active(post):
    return post[ACTIVE]


if __name__ == '__main__':
    print(fetch())
