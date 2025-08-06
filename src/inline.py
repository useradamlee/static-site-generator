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

def split_nodes_image(old_nodes):
    new_nodes = []
    if len(old_nodes) < 1:
        raise ValueError("no nodes found or incorrect formatting")
    for old_node in old_nodes:
        split_nodes = []
        extracted_node = extract_markdown_images(old_node.text)
        if not extracted_node:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for node in extracted_node:
            sections = original_text.split(f"![{node[0]}]({node[1]})", 1)
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(node[0], TextType.IMAGE, node[1]))
            original_text = sections[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    if len(old_nodes) < 1:
        raise ValueError("no nodes found or incorrect formatting")
    for old_node in old_nodes:
        split_nodes = []
        extracted_node = extract_markdown_links(old_node.text)
        if not extracted_node:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        for node in extracted_node:
            sections = original_text.split(f"[{node[0]}]({node[1]})", 1)
            if sections[0] != "":
                split_nodes.append(TextNode(sections[0], TextType.TEXT))
            split_nodes.append(TextNode(node[0], TextType.LINK, node[1]))
            original_text = sections[1]
        if original_text != "":
            split_nodes.append(TextNode(original_text, TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes
