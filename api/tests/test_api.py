
import http.client as http_client

import api.endpoints as api_ep

def test_call(client):
    """
    Tests that we can make call to the test endpoint.
    """
    resp = client.get(api_ep.TEST_ROUTE)
    assert resp.status_code == http_client.OK


def test_posts(client):
    """
    Tests that we can retreive blog posts.
    """
    resp = client.get(api_ep.POSTS_ROUTE)
    assert resp.status_code == http_client.OK

