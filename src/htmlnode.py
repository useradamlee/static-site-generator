from textnode import TextType

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        if children == None:
            self.children = []
        else:
            self.children = children
        if props == None:
            self.props = {}
        else:
            self.props = props
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props == {}:
            return ""
        HTML_attributes = []
        for prop in self.props.keys():
            HTML_attributes.append(f'{prop}="{self.props[prop]}"')
        return " "+" ".join(HTML_attributes)
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("No value provided")
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if not self.tag:
            raise ValueError("No tag provided")
        if not self.children:
            raise ValueError("Missing children")
        content = ""
        for child in self.children:
            content += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{content}</{self.tag}>"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINKS:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    if text_node.text_type == TextType.IMAGES:
        return LeafNode("img", "", props={"src": text_node.url, "alt": text_node.text})
    raise Exception("TextNode is none of the valid types")
