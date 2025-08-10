from copystatic import copystatic
from generatepage import generate_page
def main():
    copystatic("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
