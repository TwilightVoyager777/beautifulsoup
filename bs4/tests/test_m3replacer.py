from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer


#Test 1: Tag name replacement
def test_tag_name_replacement():
    #Verify name_xformer correctly renames <b> → <blockquote>
    html = """
        <html>
          <body>
            <p>Normal text</p>
            <b>Important text</b>
          </body>
        </html>
        """
    replacer = SoupReplacer(name_xformer=lambda t: "blockquote" if t.name == "b" else t.name)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.blockquote is not None


#Test 2: Attribute replacement
def test_attribute_replacement():
    #Verify attrs_xformer replaces attributes as expected
    html = """
        <html>
          <body>
            <p class="note">Paragraph 1</p>
            <div id="keep">Block</div>
          </body>
        </html>
        """
    replacer = SoupReplacer(attrs_xformer=lambda t: {"id": "new"} if "class" in t.attrs else t.attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "id" in soup.p.attrs


#Test 3: Attribute deletion
def test_delete_attribute():
    #Verify xformer can remove the 'class' attribute
    def remove_class(tag):
        if "class" in tag.attrs:
            del tag.attrs["class"]

    html = """
        <html>
          <body>
            <p class="remove-me">A</p>
            <span>B</span>
          </body>
        </html>
        """
    replacer = SoupReplacer(xformer=remove_class)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert "class" not in soup.p.attrs


#Test 4: Combined transformations
def test_combined_transformations():
    #Verify name_xformer and attrs_xformer work together correctly
    def rename(tag): return "div" if tag.name == "span" else tag.name
    def replace_attrs(tag): return {"style": "bold"}

    html = """
        <html>
          <body>
            <span>Hello</span>
            <span>World</span>
          </body>
        </html>
        """
    replacer = SoupReplacer(name_xformer=rename, attrs_xformer=replace_attrs)
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.div["style"] == "bold"


#Test 5: No replacer provided
def test_no_replacer_no_effect():
    #Ensure parsing behaves normally when no replacer is given
    html = """
        <html>
          <body>
            <b>bold</b>
            <p>plain</p>
          </body>
        </html>
        """
    soup = BeautifulSoup(html, "html.parser")
    assert soup.b is not None


#Test 6: Legacy interface compatibility
def test_old_style_replacer_still_works():
    #Verify backward compatibility with the (og_tag, alt_tag) interface
    replacer = SoupReplacer("b", "blockquote")
    html = """
        <html>
          <body>
            <b>bold</b>
            <p>plain</p>
          </body>
        </html>
        """
    soup = BeautifulSoup(html, "html.parser", replacer=replacer)
    assert soup.blockquote is not None
