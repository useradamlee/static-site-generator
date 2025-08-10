import os
from pathlib import Path
from textblock import markdown_to_html_node

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    abs_content = os.path.abspath(dir_path_content)
    content = os.listdir(dir_path_content)
    print(f"Contents of content directory: {content}")
    for item in content:
        item_path = os.path.join(abs_content, item)
        item_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item_path):
            print(f"File being generated: {item_path}")
            # rel_path = os.path.relpath(item_path, root_content_dir)
            # rel_path_html = os.path.splitext(rel_path)[0] + ".html"
            # output_path = os.path.join(abs_dest, rel_path_html)
            generate_page(item_path, template_path, Path(item_dest_path).with_suffix(".html"), base_path)
            continue
        print(f"Directory being copied: {item_dest_path}")
        os.makedirs(os.path.join(dest_dir_path, item), exist_ok=True)
        generate_pages_recursive(item_path, template_path, item_dest_path, base_path)

def generate_page(from_path, template_path, dest_path, base_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_path_content = file.read()
    with open(template_path) as file:
        template_path_content = file.read()
    HTMLstring = markdown_to_html_node(from_path_content).to_html()
    page_title = extract_title(from_path_content)
    full_html_page = template_path_content.replace('{{ Title }}', page_title).replace('{{ Content }}', HTMLstring).replace('href="/', f'href="{base_path}').replace('src="/', f'src="{base_path}')
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(full_html_page)

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith("# "):
            return line.split("# ")[1].strip()
    raise Exception("No h1 header found")
