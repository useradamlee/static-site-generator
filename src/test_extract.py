import unittest

from generatepage import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simpleTitle(self):
        md = """
# Hello
"""
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_complexTitle(self):
        md = """
why is

# Hello

- not for uoy

## nope

### maybe?
"""
        title = extract_title(md)
        self.assertEqual(title, "Hello")
