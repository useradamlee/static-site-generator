from copystatic import copystatic

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith("# "):
            return line.split("# ")[1].strip()
    raise Exception("No h1 header found")

def main():
    copystatic("static", "public")


if __name__ == "__main__":
    main()
