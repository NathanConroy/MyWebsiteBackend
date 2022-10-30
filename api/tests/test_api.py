
import http.client as http_client

import content.fetch as ft
import api.endpoints as ep

def test_call(client):
    """
    Tests that we can make call to the test endpoint.
    """
    resp = client.get(ep.TEST_ROUTE)
    assert resp.status_code == http_client.OK


def test_posts(client):
    """
    Tests that we can retreive blog posts.
    """
    resp = client.get(ep.POSTS_ROUTE)
    assert resp.status_code == http_client.OK


def test_posts_v2(client):
    """
    Tests that we can retreive blog posts.
    """
    resp = client.get(f'{ep.POSTS_ROUTE}?{ep.VERSION}={ft.V2}')
    assert resp.status_code == http_client.OK


def test_about(client):
    """
    Tests that we can retreive about page.
    """
    resp = client.get(ep.ABOUT_ROUTE)
    assert resp.status_code == http_client.OK
