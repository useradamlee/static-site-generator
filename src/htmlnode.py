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
        if not self.value:
            raise ValueError("No value provided")
        if not self.tag:
            return str(self.value)
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
