from copystatic import copystatic
from generatepage import generate_pages_recursive

def main():
    copystatic("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
