import os
from textblock import markdown_to_html_node

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_path_content = file.read()
    with open(template_path) as file:
        template_path_content = file.read()
    HTMLstring = markdown_to_html_node(from_path_content).to_html()
    page_title = extract_title(from_path_content)
    full_html_page = template_path_content.replace('{{ Title }}', page_title).replace('{{ Content }}', HTMLstring)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(full_html_page)

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith("# "):
            return line.split("# ")[1].strip()
    raise Exception("No h1 header found")
