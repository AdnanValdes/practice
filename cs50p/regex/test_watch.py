import pytest
from watch import parse

HTML1 = '<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>'
HTML2 = '<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
HTML3 = (
    '<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>'
)


def test_parse():
    assert parse(HTML1) == "https://youtu.be/xvFZjo5PgG0"
    assert parse(HTML2) == "https://youtu.be/xvFZjo5PgG0"
    assert parse(HTML3) == None
