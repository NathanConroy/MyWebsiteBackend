"""
Tests the fetch module.
"""

import posts.fetch as ft

def test_fetch():
    assert isinstance(ft.fetch(), list)
