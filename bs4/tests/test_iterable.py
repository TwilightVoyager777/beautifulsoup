from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString, Comment


def test_iter_simple_html():
    """Test iterating through a simple HTML structure (DFS)."""
    html = "<html><body><p>Hello</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    tag_names = [node.name for node in soup if isinstance(node, Tag)]
    assert tag_names == ["html", "body", "p"]

def test_iter_includes_text_nodes():
    """Text nodes (NavigableString) should appear in iteration."""
    html = "<p>Hi <b>there</b></p>"
    soup = BeautifulSoup(html, "html.parser")

    strings = [str(node) for node in soup if isinstance(node, NavigableString)]
    assert "Hi " in strings
    assert "there" in strings

def test_iter_deep_nested():
    """Test DFS order in a deeply nested structure."""
    html = "<div><a><span><b>text</b></span></a></div>"
    soup = BeautifulSoup(html, "html.parser")

    tag_names = [node.name for node in soup if isinstance(node, Tag)]
    assert tag_names == ["div", "a", "span", "b"]

def test_iter_multiple_siblings():
    """Test iteration over multiple sibling nodes in DFS order."""
    html = "<ul><li>1</li><li>2</li><li>3</li></ul>"
    soup = BeautifulSoup(html, "html.parser")

    tag_names = [node.name for node in soup if isinstance(node, Tag)]
    assert tag_names == ["ul", "li", "li", "li"]

def test_iter_mixed_nodes():
    """DFS should include Tags, Strings, and Comments"""
    html = "<div><!--c--><p>hello</p>world</div>"
    soup = BeautifulSoup(html, "html.parser")

    tag_names = [node.name for node in soup if isinstance(node, Tag)]
    assert tag_names == ["div", "p"]

    comments = [node for node in soup if isinstance(node, Comment)]
    assert len(comments) == 1
    assert str(comments[0]) == "c"

    strings = [str(node) for node in soup if isinstance(node, NavigableString)]
    assert "hello" in strings
    assert "world" in strings
