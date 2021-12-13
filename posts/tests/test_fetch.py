"""
Tests the fetch module.
"""

import copy

import posts.fetch as ft


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


def get_test_post(post):
    """
    Prepare a test post for use in a test.
    """
    return copy.deepcopy(post)


def test_fetch():
    """
    Test fetching posts.
    """
    assert isinstance(ft.fetch(), list)


def test_is_active():
    """
    Test checking that a post is active.
    """
    assert ft.is_active(get_test_post(TEST_POST))
    assert not ft.is_active(get_test_post(INACT_TEST_POST))
