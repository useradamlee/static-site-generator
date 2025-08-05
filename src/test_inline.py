import unittest

from inline import split_nodes_delimiter
from textnode import TextNode, TextType

class TestInline(unittest.TestCase):
    def test_delimiter(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )

    def test_delimiter_plain(self):
        node = TextNode("plain text only", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
              TextNode("plain text only", TextType.TEXT)
            ]
        )


    def test_delimiter_multiple(self):
        node = TextNode("`a` b `c`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            result,
            [
              TextNode("a", TextType.CODE),
              TextNode(" b ", TextType.TEXT),
              TextNode("c", TextType.CODE),
            ]
        )
