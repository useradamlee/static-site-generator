import os
import shutil

def copystatic(source, destination):
    abs_dest = os.path.abspath(destination)
    abs_source = os.path.abspath(source)
    if os.path.exists(abs_dest):
        print(f"Clearing contents of destination directory: {abs_dest}")
        shutil.rmtree(abs_dest)
    print(f"Adding back destination directory: {abs_dest}")
    os.mkdir(abs_dest)
    content = os.listdir(abs_source)
    print(f"Contents of source directory: {content}")
    for item in content:
        item_path = os.path.join(abs_source, item)
        if os.path.isfile(item_path):
            print(f"File being copied: {item_path}")
            shutil.copy(item_path, abs_dest)
        else:
            print(f"Directory being copied: {os.path.join(destination, item)}")
            os.mkdir(os.path.join(destination, item))
            copystatic(item_path, os.path.join(destination, item))

def main():
    copystatic("static", "public")


if __name__ == "__main__":
    main()
