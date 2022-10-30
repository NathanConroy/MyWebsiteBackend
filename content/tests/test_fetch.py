"""
Tests the fetch module.
"""

import copy

import content.fetch as ft


TEST_POST = {
    ft.ID: 1,
    ft.ACTIVE: True,
    ft.AUTHOR: "Nathan Conroy",
    ft.DATE: '2021-09-20',
    ft.TITLE: "Test post title.",
    ft.CONTENT: "Test post content."
}


INACT_TEST_POST = {
    ft.ID: 1,
    ft.ACTIVE: False,
    ft.AUTHOR: "Nathan Conroy",
    ft.DATE: '2021-09-20',
    ft.TITLE: "Test post title.",
    ft.CONTENT: "Test post content."
}

ID_OF_POST_IN_DB = 1


def get_test_post(post):
    """
    Prepare a test post for use in a test.
    """
    return copy.deepcopy(post)


def test_fetch_posts():
    """
    Test fetching posts.
    """
    assert isinstance(ft.fetch_posts(), list)


def test_fetch_posts_v2():
    """
    Test fetching v2 posts.
    """
    assert isinstance(ft.fetch_posts(version=ft.V2), list)


def test_fetch_post():
    """
    Test fetching a single post.
    """
    res = ft.fetch_post(ID_OF_POST_IN_DB)
    assert isinstance(res, dict)


def test_fetch_post_v2():
    """
    Test fetching a single v2 post.
    """
    res = ft.fetch_post(ID_OF_POST_IN_DB, version=ft.V2)
    assert isinstance(res, dict)


def test_fetch_about():
    """
    Test fetching about page.
    """
    assert isinstance(ft.fetch_about(), dict)


def test_is_active():
    """
    Test checking that a post is active.
    """
    assert ft.is_active(get_test_post(TEST_POST))
    assert not ft.is_active(get_test_post(INACT_TEST_POST))
