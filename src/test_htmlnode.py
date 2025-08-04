import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_prop(self):
        prop = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=prop)
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank"')
    def test_prop_many(self):
        prop = {"href": "https://www.google.com", "target": "_blank", "new": "https://www.google.com", "far": "_blank"}
        node = HTMLNode(props=prop)
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com" target="_blank" new="https://www.google.com" far="_blank"')
    def test_prop_blank(self):
        prop = None
        node = HTMLNode(props=prop)
        result = node.props_to_html()
        self.assertEqual(result, '')

if __name__ == "__main__":
    unittest.main()
