import unittest

from htmlnode import HTMLNode, LeafNode


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
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_href(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

if __name__ == "__main__":
    unittest.main()
