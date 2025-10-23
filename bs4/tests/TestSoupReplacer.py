import unittest
from bs4 import BeautifulSoup
from bs4.filter import SoupReplacer

class TestSoupReplacer(unittest.TestCase):
    def test_basic_replacement(self):
        html = "<html><body><b>bold</b></body></html>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertEqual(str(soup.blockquote.string), "bold")

    def test_no_effect_on_other_tags(self):
        html = "<p>text</p>"
        replacer = SoupReplacer("b", "blockquote")
        soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        self.assertTrue(soup.p is not None)
        self.assertIsNone(soup.blockquote)

if __name__ == "__main__":
    unittest.main()
