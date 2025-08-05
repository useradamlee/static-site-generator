import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
        elif len(old_node.text.split(delimiter)) % 2 == 0:
            raise Exception("Invalid Markdown syntax")
        else:
            split_nodes = old_node.text.split(delimiter)
            for i in range(len(split_nodes)):
                curr_val = split_nodes[i]
                if curr_val:
                    if i % 2 == 0:
                        new_nodes.append(TextNode(curr_val, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(curr_val, text_type))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
